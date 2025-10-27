# Setup for CSDS 413 Term Project Environment

## Pyenv

Install development dependencies required for building Python from source
```bash
sudo apt install make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Download and install pyenv
```bash
curl https://pyenv.run | bash
```

Configure shell environment to include pyenv in PATH and enable automatic initialization
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```

Reload shell configuration
```bash
source ~/.bashrc
```

Confirm pyenv is properly installed and accessible
```bash
pyenv --version
```

## LaTeX

Install TeXLive
```bash
sudo apt install texlive-full
```

Verify pdflatex is available and working
```bash
which pdflatex
pdflatex --version
```

## Poetry

Download and install Poetry using the official installer
```bash
curl -sSL https://install.python-poetry.org | python3 -
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
poetry --version
```

## Clone and Setup

Clone the repository
```bash
git clone https://github.com/jmanderson0119/csds413-term-project.git
cd csds413-term-project
```

Navigate to the csds413_term_project directory and install + set your local Python version to any 3.12.0 or higher
```bash
cd csds413_term_project
pyenv install 3.12.0
pyenv local 3.12.0
```

Configure Poetry to use the pyenv-managed Python version and install any project dependencies
```bash
poetry env use $(pyenv which python)
poetry install
```

## LaTeX Compilation

Navigate to a directory containing latex and compile your document
```bash
cd csds413_term_project/proposal/
latexmk -pdf main.tex
```

## Working in the Environment

To activate the environment
```bash
cd csds413_term_project
eval '$(poetry env activate)' or poetry shell
```

To update environment to current dependencies in the project config
```bash
poetry install
```

To inspect current dependencies
```bash
poetry list
```

To add packages
```bash
poetry add <name>
```

To remove packages
```bash
poetry remove <name>
```

Exit the Poetry environment when finished
```bash
deactivate
```