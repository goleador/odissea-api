#!/bin/bash

# Create core directories and files
mkdir alembic app app/api app/core app/tests

# Root level files
touch .env .gitignore requirements.txt Procfile README.md

# Alembic files
touch alembic.ini

# Alembic versions folder
mkdir alembic/versions

# App core files
touch app/__init__.py
touch app/main.py
touch app/models.py
touch app/crud.py
touch app/schemas.py
touch app/database.py

# App api folder files
touch app/api/__init__.py
touch app/api/users.py

# App core folder files
touch app/core/__init__.py
touch app/core/config.py
touch app/core/security.py

# App tests folder files
touch app/tests/__init__.py
touch app/tests/test_users.py

# Add initial content to .gitignore
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".pytest_cache/" >> .gitignore
echo "*.pyc" >> .gitignore

# Add initial content to README.md
echo "# FastAPI Project" >> README.md
echo "This is a FastAPI project scaffold." >> README.md

# Add initial content to Procfile
echo "web: uvicorn app.main:app --host 0.0.0.0 --port \$PORT" >> Procfile

# Print completion message
echo "Project folder structure created successfully."