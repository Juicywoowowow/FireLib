"""
Firelib utility functions
"""

import os
import sys
import subprocess
import shutil

def run_command(cmd, shell=False, capture=True):
    """Run a command and return output"""
    try:
        if capture:
            result = subprocess.run(cmd, shell=shell, capture_output=True, text=True)
            return result.returncode, result.stdout, result.stderr
        else:
            result = subprocess.run(cmd, shell=shell)
            return result.returncode, "", ""
    except Exception as e:
        return -1, "", str(e)

def find_executable(name):
    """Find an executable in PATH"""
    return shutil.which(name)

def get_termux_prefix():
    """Get Termux PREFIX"""
    return os.environ.get('PREFIX', '/data/data/com.termux/files/usr')

def format_size(bytes):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} PB"

def is_termux():
    """Check if running in Termux"""
    return os.path.exists('/data/data/com.termux')
