# Contributing
Please read the guidelines on git-workflow in [`CONTRIBUTING.md`](CONTRIBUTING.md) to ensure consistency.

# Setting up the project
Create a virtual environment:
```bash
python -m venv .venv
```

Activate the virtual environment:
```bash
source .venv/bin/activate  # On Unix or MacOS
```

Install dependencies:
```bash
pip install -e ".[dev]" # Installs both main and development dependencies
```

## Adding dependencies
To add new dependencies, you need to update the **dependencies** list in `pyproject.toml`. After adding the new dependency, run the following command to install it:
```bash
pip install -e .
```


# Testing the project
Test files are located in the `tests` directory. Test files must be must be named according to the pattern `test_*.py` or `*_test.py`. To run the tests, use the following command:
```bash
pytest
```

# Code formatting
This project uses [Ruff](https://docs.astral.sh/ruff/) for code formatting and linting. The formatting configuration is defined in `pyproject.toml`.

To format all Python files in the project:
```bash
ruff format .
```

To check for linting issues and auto-fix them:
```bash
ruff check --fix .
```

To check if code is properly formatted (without making changes):
```bash
ruff format --check .
ruff check .
```
