#!/usr/bin/env bash


# Create the virtual environment
python3 -m venv .venv
# Wait until its finished
if [ $? -eq 0 ]; then
    echo "Virtual environment created successfully."
else
    echo "There was an error creating the virtual environment."
    exit 1
fi

# Enter the virtual environment
source .venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
if [ -f "./requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Requirements.txt not found in the current directory."
    exit 1
fi

# Exit the virtual environment
deactivate
