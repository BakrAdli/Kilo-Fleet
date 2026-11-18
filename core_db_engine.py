import sqlite3
from pathlib import Path
from typing import Any, List, Optional, Tuple, Union


class DatabaseEngine:
    """Manages thread-safe local SQLite connections and atomic transactions."""

    def __init__(self, db_path: Union[str, Path]) -> None:
        self._db_path: Path = Path(db_path)
        self._connection: Optional[sqlite3.Connection] = None

    def __enter__(self) -> sqlite3.Cursor:
        self._connection = sqlite3.connect(self._db_path)
        self._connection.row_factory = sqlite3.Row
        # Enforce foreign key constraints at the engine level
        self._connection.execute("PRAGMA foreign_keys = ON;")
        return self._connection.cursor()

    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> None:
        if self._connection is not None:
            if exc_type is not None:
                self._connection.rollback()
            else:
                self._connection.commit()
            self._connection.close()

    def execute_safe_query(
        self, query: str, params: Tuple[Any, ...] = ()
    ) -> List[sqlite3.Row]:
        """Executes a parameterized read query to prevent SQL injection."""
        with self as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()
