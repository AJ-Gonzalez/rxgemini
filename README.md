# RX Gemini

Python unit test automation toolkit. Generate real-world faithful unit tests with zero overhead.

RX Gemini empowers developers, testers, and management to focus on features and code quality.

Cross platform and adaptable.

## Current Features

- Configuration generator

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

*To generate a requirements.txt please use:*

`poetry export --without-hashes --format=requirements.txt > requirements.txt`

### Install from PyPI

Coming soon, still a WIP :)

## Usage

This section covers Setup, Configuration, and Using RX Gemini.

### Setup

First ensure RX Gemini is working as intented with:

`rxgemini --help`

If it is not in `PATH` you can also call it with `python -m` like so:

`python -m rxgemini --help`

Once you know it works you can navigate to your project directory.
You will now genrerate a configuration file:

`rxgemini generate config`

Then press `y` to confirm.

Yay! You have now set up RX Gemini for your project, you can read below on how to customize your configuration, or skip to the [Using RX Gemini](#using-rx-gemini) section below.

### Configuration

Configuring RX Gemini is easy, below is an example of the default configuration file.

```yaml
DELIMITERS:
- _about_
- _regarding_
- _evaluates_
FORMALITY: 0
INPUT_SUFFIX: -input
LOG_PREFIX: '[RX_GEMINI]'
MARKER_KW: RXGEMINI
METADATA_SUFFIX: -meta
OUTPUT_SUFFIX: -output
SAVE_DIRECTORY: test_data_cache
TAGS:
  FETCHER:
  - fetcher
  - 'on'
  - 'off'

```

Although you do not need to alter the default configuration for it to work, you can tailor things to your specific workflow.

Here is a handy table of what each field does and its datatype.

| Field:          | Content:                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Type:                        | Example Value:                      |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|-------------------------------------|
| DELIMITERS      | Reserved words that separate a test method's name and its purpose. E.g. if your test method is named `test_my_fucntion` RX Gemini can  tell that `my function` is the one you are testing. However, if you  are using a more descriptive test method name, we use these delimiters  to be able to extract the function or method name. For example:  `test_my_function_regarding_error_handling` thanks to the delimiter we know we are still referring to `my_function`. | List of strings              | `["_about_", "_regarding_"]`        |
| FORMALITY       | (Not yet implemented) Formality level of log messages                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer                      | `0`                                 |
| INPUT_SUFFIX    | Suffix for input related pickle files                                                                                                                                                                                                                                                                                                                                                                                                                                     | String                       | `"-input"`                          |
| LOG_PREFIX      | (Not yet implemented) Prefix for log entries to denote the use of RX Gemini                                                                                                                                                                                                                                                                                                                                                                                               | String                       | `"[RX_GEMINI]"`                     |
| MARKER_KW       | Keyword to denote an action toggle such as `fetcher on`                                                                                                                                                                                                                                                                                                                                                                                                                   | String                       | `"RXGEMINI"`                        |
| METADATA_SUFFIX | Suffix for JSON metadata files                                                                                                                                                                                                                                                                                                                                                                                                                                            | String                       | `"-meta"`                           |
| OUTPUT_SUFFIX   | Suffix for output related pickle files                                                                                                                                                                                                                                                                                                                                                                                                                                    | String                       | `"-output"`                         |
| SAVE_DIRECTORY  | Name for data cache directory                                                                                                                                                                                                                                                                                                                                                                                                                                             | String                       | `"test_data"`                       |
| TAGS            | Key Value pairs for action toggles.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Key Value pair, (List Value) | `FETCHER: ["fetcher", "on", "off"]` |

> *Please note that some configuration items do not yet affect functionality, or belong to features further ahead in the roadmap*

### Using RX Gemini

It is expected that your project will have a `tests` folder, if it does not exists it will be created.

#### Data fetching

To fetch data two things are needed:

- Keyword Toggle for fetcher.
- `@fetcher` decorator on the target function or method.

The keyword is `RXGEMINI` by default, it needs to be placed in a comment, it can be anywhere in int python fil, however it is recommended you place it below the imports.

Should look something like this:

`# RXGEMINI fetcher on`

The *keyword*denotes a toggle is present, then the `fetcher` tag references the fetcher decorator, next you have either `on` or `off`, depending on whether the fetcher should be active or inactive.

The decorator is used like any other, right above the fucntion declaration.

Here is an example:

```python
from rxgemini.fetcher import data_fetcher

# RXGEMINI fetcher off


@data_fetcher
def add_numbers(num1: int, num2: int):
    """

    Example function to showcase fetcher decorator usage

    Args:
        num1 (int): Number
        num2 (int): Other number
    """
    example_sum = num1 + num2
    print("Sum: ", example_sum)


if __name__ == "__main__":
    print("RX Gemini showcase")
    add_numbers(1, 2)

```

> **Please note that for the fetcher to work properly you script, module, project, or program must be called from the project's root directory**

If your folder structure looks like this, you must call the module from `myproject` like `python3 src/main.py`.

```shell
my-project/
  src/
    └── main.py

```

#### Data injection

WIP

### Test Generation

WIP

## Roadmap

Please note that the current roadmap only supports `unittest` for test generation.

If there is interest in supporting automatig other kinds of test generaration and supporting PyTest or Nose2 please let me know. I would like to include support for those and for smart test automation.

- Smart Data Fetch
- Data Type validation
- Smart Data Injection
- Auto boilerplate
- Auto test imports
- Auto generate unit tests
- Adjustable formality level for logs and feedback
- Smart Docstring reader
- auto minifier for builds/production

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
