#!/bin/bash

# Set the virtual environment directory name
VENV_DIR="venv"

# Create a virtual environment in the current directory if it doesn't already exist
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv $VENV_DIR
  echo "Virtual environment created at $(pwd)/$VENV_DIR"
else
  echo "Virtual environment already exists at $(pwd)/$VENV_DIR"
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install the required packages from requirements.txt if it exists
if [ -f "requirements.txt" ]; then
  echo "Installing dependencies from requirements.txt..."
  pip install -r requirements.txt
else
  echo "requirements.txt not found. Please ensure it exists in the current directory."
fi

# Confirm the environment setup
echo "Virtual environment setup complete and dependencies installed."

# Provide instructions to the user
echo "To activate the virtual environment manually, use: source $VENV_DIR/bin/activate"