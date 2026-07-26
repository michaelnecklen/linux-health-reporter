# Linux Health Reporter

## Overview

Linux Health Reporter is a lightweight Python command-line tool that collects
and summarizes essential information from a Linux system. It reports system
identity, software versions, uptime, root-filesystem usage, and a simple disk
health classification.

The project demonstrates practical Python scripting for Linux support and
operations using only the Python standard library.

## Features

- Reports the system hostname.
- Displays the Linux kernel and Python versions.
- Reads and formats system uptime from `/proc/uptime`.
- Reports total, used, and available space for the root filesystem in GiB.
- Calculates root-filesystem utilization as a percentage.
- Classifies utilization as `OK`, `WARNING`, or `CRITICAL`.
- Runs safely as a script without producing report output when imported.
- Requires no third-party Python packages.

## Example Output

A typical report looks like this:

```text
Linux System Health Report
==========================
Hostname:  Serval
Kernel:    7.0.11-76070011-generic
Python:    3.12.3
Uptime:    4:59:52

Root Filesystem
---------------
Total:        914.8 GiB
Used:         118.1 GiB
Available:    750.2 GiB
Utilized:     13.6%
Status:       OK
```

## Requirements

- A Linux system that provides `/proc/uptime`.
- Python 3. The project was developed and tested with Python 3.12.3.
- No third-party Python packages are required.

## Usage

Clone the repository and enter the project directory:

```bash
git clone https://github.com/michaelnecklen/linux-health-reporter.git
cd linux-health-reporter
```

Run the report with the system's Python 3 interpreter:

```bash
python3 health_report.py
```

For development in an isolated virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python health_report.py
```

The development environment and VS Code setup are documented in
[`docs/DEVELOPMENT_SETUP.md`](docs/DEVELOPMENT_SETUP.md).

## Project Structure

```text
linux-health-reporter/
├── health_report.py
├── README.md
├── docs/
│   └── DEVELOPMENT_SETUP.md
└── notes/
    ├── health_report_checkpoint_01_annotated.py
    └── LEARNING_JOURNAL.md
```

- `health_report.py` contains the clean executable program.
- `docs/` contains project setup documentation.
- `notes/` preserves the annotated checkpoint and evidence-based learning
  journal.

## How It Works

1. `socket`, `platform`, `/proc/uptime`, and `shutil` provide raw system data.
2. `get_uptime()` converts raw uptime seconds into a readable duration.
3. `bytes_to_gib()` converts filesystem byte counts into GiB.
4. The program calculates root-filesystem utilization as a percentage.
5. `get_disk_status()` classifies utilization using ordered thresholds.
6. `main()` coordinates data collection, processing, and presentation.
7. The entry guard runs `main()` only when the file is executed directly.

## Verification

Check Python syntax without running the report:

```bash
python -m py_compile health_report.py
```

Run the report directly:

```bash
python health_report.py
```

Verify that importing the module does not run the report:

```bash
python -c "import health_report; print('Imported without running report')"
```

Check pending Git changes for whitespace errors:

```bash
git diff --check
```

## Current Limitations

- The uptime implementation depends on Linux's `/proc/uptime`.
- Only the filesystem mounted at `/` is reported.
- Status thresholds are currently fixed at 80% and 90%.
- `get_disk_status()` assumes its percentage argument is within the valid
  0–100 range.
- Utilization is calculated from used plus free space and may differ from tools
  that account for reserved filesystem blocks differently.
- The program currently prints text only and has no command-line options,
  structured output, logging, or automated test suite.

## Roadmap

- Add automated tests for conversion and status-classification functions.
- Validate percentage inputs and test failure behavior.
- Add command-line options for filesystem paths and custom thresholds.
- Add structured output such as JSON for use by other tools.
- Return meaningful process exit codes for monitoring and automation.
- Expand the report with additional Linux health indicators.
