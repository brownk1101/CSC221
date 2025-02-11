"""Utility functions."""

import os
import subprocess

def clear_screen() -> None:
    """OS sensitive clear command."""
    clear = "clear" if os.name == "posix" else "cls"
    subprocess.run(clear)
