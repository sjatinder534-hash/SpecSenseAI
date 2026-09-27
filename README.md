# SpecSenseAI
This is sample readme file

### GIT Commands
```
git status
git add . / git add <fielname>
git commit -m "message"
git push origin main
git pull
```

## UV Commands
This project uses [uv](https://docs.astral.sh/uv/) for Python environment and package management.

### 1. Create Virtual Environment
Create a Python 3.11 virtual environment in the `.venv` directory:
```powershell
uv venv .venv --python 3.11
```

### 2. Permissions
Allows your Windows user account to run PowerShell scripts, including the virtual environment activation script.
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### 3. Virtual environment activation
Activates the .venv virtual environment in the current PowerShell session.
```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install python package
Installs all Python packages listed in requirements.txt into the active virtual environment.
```powershell
uv pip install -r requirements.txt
```

### 4. Deactivates the currently active virtual environment.
```powershell
deactivate
```

### 5. Delete environment
Deletes the .venv folder and everything inside it, including all installed packages.
```powershell
Remove-Item -Recurse -Force .venv
```

### Project Structure
SpecSenseAI/
- experiments/
    - workflow.ipynb
- src/
    - specsense/
        - __init__.py
        - utils.py
        - llm/
            - __init__.py
    - images/
- tests/
- logs/
- .env
- pyproject.toml
- main.py

__init__.py tells Python that a directory should be treated as a Python package. It can also contain package initialization code.