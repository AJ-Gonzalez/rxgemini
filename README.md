# RX Gemini

Python unit test automation toolkit. Generate real-world faithful unit tests with zero overhead.

RX Gemini empowers developers, testers, and management to focus on features and code quality.

## Current Features

## Installation

### Build from source

Please ensure you have [Python Poetry](https://python-poetry.org/) installed.

Build with:

`poetry build`

This will generate a wheel in the `dist` directory.

You can then install that wheel with pip:

`pip install dist\rxgemini-0.1.1-py3-none-any.whl`

Use `--force-reinstall` if the version in pyproject.toml has not been updated.

If your python packages are not on PATH, then you may need to use `python -m rxgemini`.

*To generate a requirements.txt please use:* `poetry export --without-hashes --format=requirements.txt > requirements.txt`

### Install from PyPI

Coming soon, still a WIP :)

## Usage

## Roadmap

- Smart Data Fetch
- Smart Data Injection
- Auto boilerplate
- Auto test imports
- Auto generate unit tests

## Contribute to RX Gemini

You can contribute in many ways, and any help is appreciated. The easiest and best way to start is to become a user and share any feedback you have.

Here are the main project needs:

- Test coverage, ironic I know.
- Documentation on usage and setup.
- Feature requests.
- A proper logo. (I have a couple ideas but cannot draw like that)

For now I am the sole developer, however this will change in the future.

### Coding standars

Pylint, flake8, and Black Formatter.

All methods and fucntions must have docstrings.

If there are any dependency changes please run:

`poetry export --without-hashes --format=requirements.txt > requirements.txt`

To update the requirements for github's pylint workflow.

### Commit message standards

We use a prefix followed by a colon.

Example `feat: added smart scanner`

| Prefix | Indicates                                   |
|--------|---------------------------------------------|
| feat   | Adding to a feature or adding functionality |
| fix    | Bug fix or Hot Fix                          |
| docs   | Changes to Documentation, or docstrings     |
| fmt    | Formatting (no logic changed)               |
| ref    | Refactor or rework                          |

### Branch Naming Convention

`main` is the release branch, at this time the rest of the branch conventions is still being decided.

## Notes

The RX in the name is inspired by both the RX-78-2 Mobile Suit from Gundam, and the Mazda FC Rx7 sportscar.
Gemini refers to the constellation and the NASA Program.

### Useful links

- [Markdown Tables](https://www.tablesgenerator.com/markdown_tables#)

- [Typer Documentation](https://typer.tiangolo.com/)

- [Python Poetry Documentation](https://python-poetry.org/docs/)
