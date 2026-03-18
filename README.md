WatchDawg 🐾
Overview

WatchDawg is a real-time directory monitoring system built using Python.
It detects file changes and logs them instantly using an event-driven architecture.

Features

Real-time file monitoring (create, modify, delete)

Modular architecture

Structured logging (console + file)

YAML-based configuration

Persistent log storage

Tech Stack

Python

Watchdog

PyYAML

Logging module



Project Evolution

Phase 1: Setup

Initialized Git and project structure

Configured virtual environment and .gitignore

Phase 2: Basic Monitoring

Implemented real-time directory monitoring

Detected file events using watchdog

Phase 3: Architecture Refactor

Modularized codebase

Introduced structured logging system

Phase 4: Production Upgrade

Added YAML configuration

Implemented file-based logging





How to Run
cd watchdawg
source venv/bin/activate
pip install -r requirements.txt
python main.py
Example Output
INFO | Watching: watch_dir
INFO | Created: watch_dir/test.txt
INFO | Deleted: watch_dir/test.txt


Future Improvements

CLI arguments support

Docker containerization

Alert system (email/Slack)

Web dashboard
