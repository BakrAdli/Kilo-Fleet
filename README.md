# Kilo Fleet — Core Architecture (Technical Showcase)

> **Status:** Active Prototype (Proprietary / Closed-Source)  
> **Note:** To protect intellectual property and domain-specific logic, business rules, predictive algorithms, and UI assets are excluded from this public repository. This showcase highlights the underlying software engineering standards and database infrastructure.

##  Architectural Design
Kilo Fleet is engineered as an offline-first desktop system. Instead of relying on heavy web frameworks, it uses a lightweight, decoupled architecture connecting a local relational database to an isolated rendering process.

```mermaid
graph LR
    A[PyWebView Frontend Layer] <-->|JSON-RPC / IPC Bridge| B(Python Backend Core)
    B <-->|Parameterized SQL Queries| C[(Local SQLite Engine)]
