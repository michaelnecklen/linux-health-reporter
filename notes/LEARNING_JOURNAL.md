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

## Checkpoint 02 — Automated Tests and Input Validation

**Checkpoint commit:** `711e3d1`
**Completed:** July 27, 2026

### What I Built

- Added an automated test suite using Python's built-in `unittest` module.
- Added three tests for `bytes_to_gib()` and eight tests for
  `get_disk_status()`.
- Added input validation that raises `ValueError` when a percentage is below
  `0` or above `100`.
- Preserved valid boundary behavior at exactly `0` and `100`.
- Updated the public README to document testing, validation, project structure,
  verification commands, current limitations, and the revised roadmap.

### What the Tests Prove

- All eleven specified conversion, classification, boundary, and invalid-input
  examples currently produce their expected outcomes.
- `bytes_to_gib()` returns the expected GiB values for zero bytes, half a GiB,
  and one GiB.
- `get_disk_status()` changes classification at the intended 80% and 90%
  thresholds while accepting valid endpoints at 0% and 100%.
- Values below 0% and above 100% raise `ValueError` instead of receiving a
  misleading health classification.
- Rerunning the complete suite provides regression evidence that new validation
  did not break the previously tested behavior.
- These tests cover the behaviors we specified; they do not prove that the
  entire program contains no other defects.

### Red-to-Green Lesson

- Write a test for the desired behavior before implementing it.
- Run the test and confirm that it fails for the expected reason. This is the
  red stage and proves the missing behavior is detectable.
- Add the smallest production-code change that should satisfy the requirement.
- Rerun the complete suite. When every expected behavior passes, the suite is
  green.
- A failing test can expose either a production-code defect or a defective test.
  The `100.0` test was wrong because 100 is a valid endpoint; `100.1` correctly
  represents an invalid value above the range.
- `py_compile` checks whether Python can compile the source, while `unittest`
  executes specified behaviors and compares actual results with expected
  results.

### Corrections That Improved My Understanding

- The complete line `disk_used = bytes_to_gib(disk.used)` is an assignment
  statement. Only `bytes_to_gib(disk.used)` is the function call, and
  `disk_used` is the variable receiving the returned value.
- Parameter names appear in function definitions, not necessarily at call
  sites. `byte_count` is the parameter in the definition, while `disk.used` is
  the argument supplied by position during the call.
- Byte conversion and percentage calculation are separate operations.
  `byte_count / (1024 ** 3)` converts bytes to GiB, while
  `disk.used / (disk.used + disk.free) * 100` calculates utilization percent.

### Repetition Queue

- Trace assignment statements by evaluating the right-hand function call first,
  following its returned value, and identifying the left-hand receiving variable.
- Repeatedly match call-site arguments to definition-site parameters.
- Distinguish the outer `assertEqual()` method call from a nested function call
  used as its actual-value argument.
- Practice reading `unittest` classes, test methods, `self`, `assertEqual()`,
  and `assertRaises()`.
- Keep byte-to-GiB conversion separate from utilization-percentage calculation.
- Repeat the red-to-green cycle and diagnose whether a failure belongs to the
  production code or the test.

### Next Steps

- Commit and publish the Checkpoint 02 journal entry.
- Expand automated coverage to `get_uptime()` without depending on Serval's
  current uptime.
- Learn how test doubles and mocking can provide controlled filesystem data.
- Later add automated test execution on GitHub and continue the project roadmap.

## Checkpoint 03 — Controlled Uptime Testing with Mocking

**Checkpoint commit:** `bec066e`
**Completed:** July 30, 2026

### What I Built

- Added `TestGetUptime` and a controlled test for `get_uptime()`.
- Used `unittest.mock.patch` to temporarily replace
  `health_report.Path.read_text`.
- Supplied the controlled string `"3661.75 99999.00\n"` instead of reading
  Serval's changing `/proc/uptime` data.
- Verified that the real parsing and conversion logic returns
  `timedelta(seconds=3661)`, displayed as `1:01:01`.
- Increased the automated suite from eleven to twelve passing tests without
  changing production behavior.
- Updated the public README to describe controlled uptime coverage and revise
  the testing roadmap.

### What Mocking Means

- Mocking temporarily substitutes controlled behavior for a real dependency
  during a test.
- `patch()` does not edit `health_report.py`, `/proc/uptime`, or any file on
  disk; the substitution exists only in the running Python process.
- The production function still creates `Path("/proc/uptime")`, but the patched
  `read_text()` method intercepts the read and returns controlled text.
- The replacement is active only inside the indented `with patch(...):` block.
  The real method is restored automatically when that block exits.
- Patch the dependency where the production module looks it up, which is why
  the target is `health_report.Path.read_text`.
- Mocking makes tests deterministic, isolates external dependencies, and avoids
  changing the real system merely to create a test condition.

### Controlled Data Flow

1. The patched `read_text()` method returns the controlled string
   `"3661.75 99999.00\n"`.
2. `.split()` produces the list `["3661.75", "99999.00"]`.
3. `[0]` selects the string `"3661.75"`.
4. `float()` converts that string to the float `3661.75`.
5. `int()` discards the fractional part and returns the integer `3661`.
6. `timedelta(seconds=3661)` creates a duration displayed as `1:01:01`.
7. `assertEqual()` compares the actual duration returned by `get_uptime()` with
   the expected `timedelta(seconds=3661)` object.
8. Matching objects allow the assertion to continue; unequal objects raise an
   assertion failure.

### Debugging Lessons

- Test-only imports belong in `tests/test_health_report.py`, not in the
  production module.
- Importing `health_report` from inside `health_report.py` caused the module to
  import itself before its function definitions existed, producing a
  partially-initialized-module circular import error.
- `py_compile` accepted the code because the import statement was valid syntax;
  the failure appeared only when Python executed the import during testing.
- After removing the self-import, the test module also needed to import
  `get_uptime` alongside the other tested helper functions.
- VS Code diagnostics indicated that something was wrong, while the traceback
  identified the runtime path and failure reason.
- Running `git diff` after cleanup proved that production code was restored and
  only the intended test and README changes remained.
- Careful error reading, file inspection, correction, and retesting allowed me
  to diagnose and repair the mistakes rather than merely copy a fix.

### Repetition Queue

- Distinguish a value from its type: `3661.75` is a value of type `float`, while
  `3661` is a value of type `int`.
- Remember that `.split()` returns a list and that quoted elements inside the
  list remain strings.
- Practice identifying what a mock replaces, what controlled value it returns,
  where the patch target is looked up, and when restoration occurs.
- Trace nested calls inside `assertEqual(actual, expected)` without treating the
  assertion as returning the expected value.
- Reinforce the difference between syntax validation, runtime execution,
  editor diagnostics, tracebacks, and automated behavioral tests.
- Practice recognizing self-imports and partially initialized modules from
  circular-import tracebacks.

### Next Steps

- Commit and publish the Checkpoint 03 journal entry.
- Verify that the patched `read_text()` method was called as expected.
- Test controlled malformed uptime data and its failure behavior.
- Expand automated coverage to report coordination and formatted output.
- Add automatic test execution on GitHub later in the project.