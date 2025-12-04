# Firelib

A minimal, powerful enhancement library for Termux that supercharges your Android terminal experience.

## What is Firelib?

Firelib extends Termux with essential tools for pentesting, development, and system administration. Built with C/C++ for performance and Python for flexibility.

## Features

- **File System Tools**: Virtual mounts, snapshots, and advanced operations
- **Network Utilities**: Quick servers, tunneling, and sharing
- **Development Tools**: Environment management and build helpers
- **System Utilities**: Monitoring, cleanup, and configuration

## Installation

```bash
git clone https://github.com/yourusername/firelib.git
cd firelib
python install.py
```

The installer automatically detects your Python version and installs necessary dependencies.

## Requirements

- Termux (Android)
- Python 2 or Python 3
- Basic build tools (installed automatically if missing)

## Quick Start

```bash
# Start a quick web server
fire-serve

# Monitor system resources
fire-monitor

# Mount a virtual filesystem
fire-mount /path/to/mount

# Share files over local network
fire-share myfile.txt
```

## Configuration

All configuration is stored in `~/.firelib/`

## License

MIT
