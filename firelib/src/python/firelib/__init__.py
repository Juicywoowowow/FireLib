"""
Firelib - Termux Enhancement Library
"""

__version__ = "0.1.0"

import os
import sys

# Firelib home directory
FIRELIB_HOME = os.path.expanduser("~/.firelib")
FIRELIB_CONFIG = os.path.join(FIRELIB_HOME, "config")
FIRELIB_DATA = os.path.join(FIRELIB_HOME, "data")
FIRELIB_LOGS = os.path.join(FIRELIB_HOME, "logs")

def get_config_path(name):
    """Get path to a config file"""
    return os.path.join(FIRELIB_CONFIG, name)

def get_data_path(name):
    """Get path to a data file"""
    return os.path.join(FIRELIB_DATA, name)

def get_log_path(name):
    """Get path to a log file"""
    return os.path.join(FIRELIB_LOGS, name)
