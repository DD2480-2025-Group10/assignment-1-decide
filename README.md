<!-- Pytest Coverage Comment:Begin -->
<!-- Pytest Coverage Comment:End -->

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
