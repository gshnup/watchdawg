<div align="center">

# 🐾 WatchDawg

**Event-driven directory monitoring — real-time, structured, production-ready.**

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Watchdog](https://img.shields.io/badge/Watchdog-4.0.1-FF6B6B?style=flat)
![PyYAML](https://img.shields.io/badge/PyYAML-6.0-F5C518?style=flat)
![Status](https://img.shields.io/badge/Status-Active-22C55E?style=flat)

</div>

---

## What is WatchDawg?

WatchDawg watches any directory and instantly logs every file system event — creates, modifications, deletions, moves — using OS-level hooks (`inotify` on Linux, `FSEvents` on macOS) via the `watchdog` library.

No polling. No CPU waste. Pure event-driven.

> Built to demonstrate file system observability, modular Python architecture, and production-grade logging — core skills in any DevOps/SRE role.

---

## Features

- ⚡ Event-driven — reacts instantly, not on a timer
- 📂 Recursive directory watching
- 🗂️ Dual logging — formatted console output + persistent log file
- ⚙️ YAML-based config — zero hardcoded values
- 🧱 Modular codebase — watcher, handler, logger cleanly separated
- 🛑 Graceful shutdown on `Ctrl+C`

---

## Project Structure
```
watchdawg/
├── main.py          # Entry point
├── config.yaml      # All settings live here
├── requirements.txt
├── core/
│   ├── watcher.py   # Observer lifecycle
│   ├── handler.py   # Event processing
│   └── logger.py    # Console + file logging
└── logs/
    └── watchdawg.log
```

---

## Getting Started
```bash
git clone https://github.com/YOUR_USERNAME/watchdawg.git
cd watchdawg
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Configure via `config.yaml`:
```yaml
watch:
  path: ./watch_dir
  recursive: true
logging:
  log_to_file: true
  log_dir: ./logs
```

---

## Sample Output
```
2024-03-18 14:01:02 | INFO | WatchDawg started — Watching: ./watch_dir
2024-03-18 14:01:15 | INFO | [CREATED ] [FILE] watch_dir/report.csv
2024-03-18 14:01:43 | INFO | [MODIFIED] [FILE] watch_dir/config.yaml
2024-03-18 14:02:10 | INFO | [DELETED ] [FILE] watch_dir/old_notes.txt
```

---

## How It Was Built

| Phase | What happened |
|---|---|
| Foundation | Git setup, venv, project structure |
| Core | `watchdog` Observer + event handler for CREATE / MODIFY / DELETE / MOVE |
| Refactor | Broke monolithic script into `core/` modules |
| Production | YAML config, persistent logging, graceful shutdown |

---

## Why This Matters in DevOps

This pattern powers real tools — Filebeat watches directories to ship logs, CloudWatch Agent monitors for file changes, CI/CD pipelines trigger on artifact drops. WatchDawg is a ground-up implementation of that same primitive.

---

## Roadmap

- [ ] CLI args (`--path`, `--interval`)
- [ ] Periodic summary reports
- [ ] Slack / email alerts
- [ ] Docker support
- [ ] Prometheus metrics + Grafana dashboard

---

<div align="center">
  <sub>Part of a DevOps portfolio — built iteratively, documented intentionally</sub>
</div>
