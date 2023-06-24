# aoc-2022
## Advent of Code 2022

My solutions in Python and Rust.

### Python goals
Practicing good code structure, unit testing (`pytest`), and static typing (`mypy`).

Each day folder is treated as a stand-alone project.

Generally, speaking the commands for running each day would look like this:
```bash
cd day-05
pyenv local 3.11.3
poetry env use $(pyenv which python)  # create a venv
poetry install  # install project dependencies into a virtual env
poetry run pytest -vvv  # run pytest (config in pyproject.toml)
poetry run mypy main.py  # run mypy (config in pyproject.toml)
poetry run python main.py data/puzzle.txt  #  get puzzle answers
```

### Rust goals
Learning the language basics.
