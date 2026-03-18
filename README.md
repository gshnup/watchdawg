WatchDawg 🐾
Overview

WatchDawg is a real-time directory monitoring system built using Python.
It observes file system changes and reacts instantly when files are created, modified, or deleted.

Objective

The goal of this project is to understand and implement:

Event-driven systems

File system monitoring

Clean project structuring

DevOps-style tooling fundamentals

Tech Stack

Python

Watchdog (file system monitoring)

Project Status

🚧 In Progress — Built step-by-step with structured phases

Phases
Phase 1: Project Setup

Initialized Git repository

Set up virtual environment

Created project structure

Configured .gitignore

Phase 2: Basic Monitoring System

Implemented real-time file monitoring using watchdog

Detected:

File creation

File modification

File deletion

Output events to terminal

Phase 3: Modular Architecture

* Refactored code into separate modules
* Introduced logging system (replaced print)
* `monitor.py` handles events
* `logger.py` handles output
* `main.py` controls execution

**Result:** Cleaner, scalable, and more professional structure


How to Run
cd watchdawg
source venv/bin/activate
python main.py

In another terminal:

cd watchdawg/watch_dir
touch test.txt
echo "hello" >> test.txt
rm test.txt
