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
### Initial setup - Admin
| Step | Command                                                               | One-line explanation                                     |
| ---- | --------------------------------------------------------------------- | -------------------------------------------------------- |
| 1    | `git branch -M main`                                                  | Rename the local default branch to `main`.               |
| 2    | `git add .`                                                           | Stage all project files for the first commit.            |
| 3    | `git commit -m "Initial commit"`                                      | Create the first local commit.                           |
| 4    | `git remote add origin https://github.com/<USERNAME>/SpecSenseAI.git` | Connect the local repository to GitHub.                  |
| 5    | `git push -u origin main`                                             | Push `main` to GitHub and establish the upstream branch. |

### Developer
| Step | Command                                     | One-line explanation                                |
| ---- | ------------------------------------------- | --------------------------------------------------- |
| 1    | `git checkout main`                         | Switch to the latest `main` branch.                 |
| 2    | `git pull origin main`                      | Download the latest approved changes from GitHub.   |
| 3    | `git checkout -b feature/<feature-name>`    | Create and switch to a new feature branch.          |
| 4    | `git status`                                | Check which files have changed.                     |
| 5    | `git add .`                                 | Stage the changes for commit.                       |
| 6    | `git commit -m "Add <feature>"`             | Save the changes as a local commit.                 |
| 7    | `git push -u origin feature/<feature-name>` | Push the feature branch to GitHub.                  |
| 8    | **Create Pull Request**                     | Create a PR from `feature/<feature-name>` → `main`. |
| 9    | **You review & approve**                    | Review the code and approve the PR.                 |
| 10   | **Merge Pull Request**                      | Merge the approved changes into `main`.             |

### Project Structure
SpecSenseAI
- experiments
    - workflow.ipynb
- src
    - specsense
        - __init__.py
        - utils.py
        - llm
            - __init__.py
    - images
- tests
- data
    - products.csv
    - product_attributes.csv
- logs
- .env
- pyproject.toml
- main.py

__init__.py tells Python that a directory should be treated as a Python package. It can also contain package initialization code.