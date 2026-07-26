# Linux and Python Learning Journal

## Purpose

This journal records what I built, what I demonstrated, where I became
confused, and what I need to practice again. Its purpose is to preserve
understanding—not merely record completed commands.

## Checkpoint 01 — Linux Health Reporter Foundations

**Project:** `linux-health-reporter`
**Checkpoint commit:** `4ffd773`
**Completed:** July 25, 2026

### What I Built
- Built a Python command-line program that collects and displays useful Linux
  system-health information.
- The report displays the hostname, Linux kernel version, Python version,
  uptime, and root-filesystem capacity, usage, available space, utilization
  percentage, and health status.
- Disk utilization below 80% is classified as `OK`, utilization from 80% to
  below 90% as `WARNING`, and utilization at or above 90% as `CRITICAL`.
- Kept `health_report.py` as the clean portfolio program and created an
  annotated checkpoint that explains how the code works.
- Used Python's standard library and Linux's `/proc/uptime`, making the program
  reusable on other compatible Linux systems rather than useful only on Serval.

### What I Can Explain
- I can describe the report's overall flow: collect Linux information, convert
  and classify data, and format the results for display.
- I can trace a function call from an argument, into a parameter, through a
  `return` statement, and into the variable receiving the returned value.
- I can distinguish a function definition (`def name(...)`), a reference to the
  function (`name`), and a function call (`name(...)`) when examining code.
- I can distinguish `disk.total`, an attribute expression used as an argument,
  from `disk_total`, a variable that receives the converted GiB value.
- I can explain how `get_disk_status()` uses ordered `if`, `elif`, and `else`
  conditions to return `OK`, `WARNING`, or `CRITICAL`.
- I can explain that a plain string literal contains fixed text, while an
  f-string evaluates expressions inside braces and inserts their values.
- I can explain that `.1f` displays a number using fixed-point formatting with
  one digit after the decimal point.
- I can explain that the entry guard calls `main()` when the file runs directly
  but prevents `main()` from running when the file is imported.

### Evidence That It Works
- `python -m py_compile` completed silently, proving that Python found no syntax
  or indentation errors.
- Running the annotated file directly produced the complete system-health
  report.
- Importing the annotated module produced no report output, proving that the
  entry guard prevented `main()` from running during import.
- Boundary tests returned `OK` for `79.9`, `WARNING` for `80` and `89.9`, and
  `CRITICAL` for `90`.
- Tests with `-5` and `110` exposed the current assumption that the supplied
  percentage is valid and identified future input validation work.
- Git commit `4ffd773` preserved the annotated checkpoint, and a clean
  `git status` confirmed that all intended work was committed.
- The successful push created `origin/main`, and `git status -sb` confirmed
  that local `main` and GitHub's `origin/main` were synchronized.
- The project is publicly visible at
  <https://github.com/michaelnecklen/linux-health-reporter>.

### Corrections That Improved My Understanding
- A parameter is the placeholder named in a function definition, while an
  argument is the actual value or expression supplied in a function call. The
  call executes on the right side of an assignment, `return` sends back its
  result, and the variable on the left receives that returned value.
- A dot accesses an attribute belonging to an object or module, as in
  `disk.total`. An underscore simply joins words inside one Python name, as in
  `disk_total` or `get_disk_status`; it does not determine whether the name is
  a variable or function.
- The path `/` identifies the filesystem mounted at the Linux root directory.
  Its usage does not necessarily represent every physical disk, separate
  partition, or independently mounted filesystem in the machine.

### Repetition Queue
- Repeatedly trace this flow using different functions:
  argument → parameter → function processing → returned value → receiving variable.
- Practice recognizing a function definition, function reference, function call,
  argument, parameter, attribute expression, and receiving variable in unfamiliar
  code.
- Track how values and types change through a program, such as bytes becoming a
  GiB float or a numeric percentage becoming an `OK`, `WARNING`, or `CRITICAL`
  string.
- Reinforce module, class, function, and method terminology using Python standard
  library examples.
- Distinguish inspection commands such as `nl | sed` from verification commands
  such as `py_compile`, `git diff --check`, and direct execution tests.
- Practice the entry guard until direct execution versus importing can be
  explained without referring to notes.
- Add input validation and repeat boundary testing with valid and invalid values.

### Next Steps
- Commit and publish this learning journal.
- Create a professional `README.md` that explains the project's purpose,
  features, requirements, usage, output, structure, and current limitations.
- Begin Checkpoint 02 by adding repeatable automated tests for the helper
  functions and validation for percentages outside the valid 0–100 range.
- Build a reusable project launcher later as a separate Bash automation
  exercise.