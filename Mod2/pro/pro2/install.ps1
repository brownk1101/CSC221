# Create the venv
python -m venv venv

# Enter the venv
.\venv\Scripts\Activate.ps1

# Upgrade pip
pip install --upgrade pip

# Install Requirements
pip install -r requirements.txt

# Exit the venv
deactivate
