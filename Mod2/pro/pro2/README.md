# M2Pro2 - FTE
This program is used to generate enrollment and FTE reports.

## Install
1. Create a virtual environment
    - `python3 -m venv .venv` (linux convention)
    - `python -m venv venv` (windows)
2. Activate the venv
    - `source .venv/bin/activate` (linux)
    - `venv\Scripts\activate` (windows)
3. Update pip and install requirements
    - `pip install --upgrade pip`
    - `pip install -r requirements.txt`

or run the install script:
- Linux:
    1. `chmod +x install.sh`
    2. `./install.sh`

## Run
`python3 M2Pro2_FTE_HarleyCoughlin.py`


## Test
`python3 -m unittest test/*.py` where * is the test suite that you want to run
