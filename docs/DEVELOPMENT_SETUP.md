# Linux Health Reporter Development Setup

## 1. Enter the project directory.

From the Ubuntu desktop environment (KDE on my machine), press Ctrl+Alt+T
to open the terminal.

Navigate directly to the project directory:

`cd ~/projects/linux-health-reporter`

## 2. Activate the `.venv` virtual environment

Activate the project's virtual environment with:

`source .venv/bin/activate`

## 3. How to open the project in VS Code.

From inside the project directory, run:

`code .`

The dot represents the current directory. VS Code opens that directory as
the complete project workspace.

## 4. How to select the interpreter.

1. Press Ctrl+Shift+P.
2. Select Python: Select Interpreter.
3. Choose:

`.venv/bin/python`

or the full path:

`/home/michael/projects/linux-health-reporter/.venv/bin/python`

When a Python file is open, the selected interpreter should appear in VS Code's
lower status bar. For this project it should show Python 3.12.3 from `.venv`.

## 5. How to open the integrated terminal.

Press Ctrl plus the backtick key, usually located below Esc.

VS Code opens a terminal panel at the bottom of the window. If the selected
Python interpreter belongs to `.venv`, VS Code may activate that environment
automatically.

If it does not, run:

`source .venv/bin/activate`

## 6. How to verify Python and Git.

Run:

`pwd`

`pwd` should show `/home/michael/projects/linux-health-reporter`.

`which python`

`which python` should point inside the project's `.venv/bin/` directory.

`python --version`

`python --version` should show the intended Python version.

`python -m pip --version`

`python -m pip --version` should show pip running from inside `.venv`.

`git status`

`git status` should show the `main` branch and report any changed, added,
or untracked files.

## 7. Understand the three environment mechanisms

The `.venv` directory is a persistent directory stored inside the project.
It contains the project's isolated Python interpreter, installed packages,
and supporting files.

Running `source .venv/bin/activate` changes the current terminal session so
that commands such as `python` and `pip` use the versions inside `.venv`.
This activation applies only to that terminal session.

Selecting the interpreter in VS Code tells the editor, debugger, test
runner, and Python extension which Python installation belongs to the
project.

These mechanisms work together, but they are not the same thing:

- `.venv` directory = the isolated Python environment stored on disk

- Shell activation = the current terminal temporarily uses that environment

- VS Code interpreter selection = VS Code's Python tools use that environment

## 8. What happens when the terminal closes.

Closing a terminal ends that terminal session, including its temporary
`.venv` activation. It does not delete or damage the `.venv` directory.

To use the environment in a new terminal:

```bash
cd ~/projects/linux-health-reporter
source .venv/bin/activate
```

VS Code's integrated terminal is a separate session. Closing an outside
terminal does not close or deactivate the terminal already running inside
VS Code.

To leave the virtual environment without closing the terminal, run:

`deactivate`

This removes `.venv` from the current terminal session but does not delete
the environment.