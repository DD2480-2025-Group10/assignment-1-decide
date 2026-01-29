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

# Running the project
The project runs through the `main.py` file located in the `src` directory. As input it takes one command line argument, pointing to a filename containing the required input data. The input file must be in `.json` format and follow the structure as described in the example below:
```json
{
  "NUMPOINTS": 2,
  "X": [0.0, 1.0],
  "Y": [0.0, 0.0],

  "PARAMETERS": {
    "length1": 5.0,
    "radius1": 1.0,
    "epsilon": 0.1,
    "area": 1.0,
    "q_pts": 2,
    "quads": 1,
    "dist": 1.0,
    "n_pts": 3,
    "k_pts": 1,
    "a_pts": 1,
    "b_pts": 1,
    "c_pts": 1,
    "d_pts": 1,
    "e_pts": 1,
    "f_pts": 1,
    "g_pts": 1,
    "length2": 2.0,
    "radius2": 2.0,
    "area2": 2.0
  },

  "LCM": {
    "default": "NOTUSED",
    "overrides": [
      { "i": 0, "j": 0, "value": "ANDD" }
    ]
  },

  "PUV": [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
}
```

To run the project with a file use the following command: 
```bash
python3 src/main.py path/to/input_file.json
```

*For convenience there are a number of files to try out inside of tests/whole_program_cases*

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


## Principles Established

Principles and constraints are committed to by the team. ✅

Principles and constraints are agreed to by the stakeholders. ✅

The tool needs of the work and its stakeholders are agreed.  ✅

A recommendation for the approach to be taken is available. ✅

The context within which the team will operate is understood ✅

The constraints that apply to the selection, acquisition, and use of practices and tools are
known. ✅

## Foundation Established

The key practices and tools that form the foundation of the way-of-working are
selected. ✅

Enough practices for work to start are agreed to by the team. ✅

All non-negotiable practices and tools have been identified. ✅

The gaps that exist between the practices and tools that are needed and the practices and
tools that are available have been analyzed and understood. ✅

The capability gaps that exist between what is needed to execute the desired way of
working and the capability levels of the team have been analyzed and understood. ✅

The selected practices and tools have been integrated to form a usable way-of-working. ✅


## In Use

The practices and tools are being used to do real work. ✅

The use of the practices and tools selected are regularly inspected. ✅

The practices and tools are being adapted to the team’s context. ✅

The use of the practices and tools is supported by the team. ✅

Procedures are in place to handle feedback on the team’s way of working. ❌

The practices and tools support team communication and collaboration. ✅

Based on the checklist in the Essence Standard v1.2, we assess our current way of working as being in the In Use state because we set up a good foundation and came up with a standard, but it was kind of hard to assess due to the assignment being too short. The main obstacles to reaching the next state, In Place, are that we need to set up a system that makes us feel comfortable giving constructive feedback to the team. For this exercise, we didn’t really need to do this too much, as it went quite smoothly, but in the future it will be very valuable.
