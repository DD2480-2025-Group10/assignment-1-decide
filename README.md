Launch-Interceptor is a Python implementation of the Launch Interceptor decision logic described in `decide.pdf`.

It processes radar tracking data as 2D points, evaluates a set of geometric Launch Interceptor Conditions (LICs), and computes a final boolean launch/no-launch decision.

# Contributing
Please read the guidelines on git-workflow in [`CONTRIBUTING.md`](CONTRIBUTING.md) to ensure consistency.

# Setting up the project

- **Language**: Python 3.11

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

Run the decision function:
```bash
python -m src.main
# or
python src/main.py
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

To check if code is properly formatted (without making changes):
```bash
ruff format --check .
ruff check .
```

# Way of working
Based on the checklist in the Essence standard v1.2, we assess our current way of working as being in the Collaborating state because we consistently met our commitments and worked efficiently both independently and together, which built trust and kept us focused on the mission. The main obstacles to reaching the next state, Performing, are becoming even more accustomed to one another’s working styles and improving how we assign and prepare work, while also identifying potential problems earlier.
