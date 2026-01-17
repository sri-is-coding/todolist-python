# todolist-python

Simple, minimal TODO list application written in Python.

## Features

- Add, list, update and remove tasks
- Mark tasks as done/undone
- Persistent storage (SQLite / JSON / pick your storage)
- Simple CLI interface (or: basic Flask/FastAPI web UI)
- Unit tests included

## Getting started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites:
- Python 3.8+ (adjust if you target a different version)
- git

Clone the repo:

```bash
git clone https://github.com/sri-is-coding/todolist-python.git
cd todolist-python
```

Create and activate a virtual environment:

```bash
python -m venv .venv
# On macOS/Linux:
source .venv/bin/activate
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If you don't have a requirements.txt yet, create one when you add dependencies (e.g., Flask, Click, pytest, etc.).
