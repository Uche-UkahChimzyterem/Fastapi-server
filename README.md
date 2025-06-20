```
PROJECT STRUCTURE
```

```

app/
├── __init__.py
├── main.py                 # Entry point for the app
├── api/                    # All API route definitions
│   ├── __init__.py
│   ├── deps.py             # Common dependencies
│   └── v1/                 # Versioning (v1, v2, etc.)
│       ├── __init__.py
│       ├── endpoints/      # Actual route handlers
│       │   ├── __init__.py
│       │   ├── users.py
│       │   └── auth.py
│       └── routes.py       # Include routers here
├── core/                   # App-level configurations
│   ├── __init__.py
│   ├── config.py           # Settings via pydantic/BaseSettings
│   └── security.py         # JWT / OAuth2 utils
├── models/                 # SQLAlchemy models
│   ├── __init__.py
│   └── user.py
├── schemas/                # Pydantic schemas
│   ├── __init__.py
│   └── user.py
├── crud/                   # CRUD operations
│   ├── __init__.py
│   └── user.py
├── db/                     # Database setup and session management
│   ├── __init__.py
│   ├── base.py             # SQLAlchemy base class
│   └── session.py
├── services/               # Business logic layer
│   ├── __init__.py
│   └── user_service.py
├── utils/                  # Utility functions
│   └── helpers.py
tests/
├── __init__.py
├── conftest.py
└── test_users.py
.env                        # Environment variables
alembic/                    # (If using Alembic for migrations)
requirements.txt
README.md

```