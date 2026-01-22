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
pip install -r requirements.txt
```

## Adding dependencies
Add the dependency using pip:
```bash
pip install <package-name>
```

Freeze the current dependencies:
```bash
pip freeze > requirements.txt
```

