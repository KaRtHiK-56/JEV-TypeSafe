# JEV_Expirements

![PyPI version](https://img.shields.io/pypi/v/python-boilerplate.svg)

This repo is a expirement to get hands dirty with the JEV package

* GitHub: https://github.com/KaRtHiK-56/python-boilerplate/
* PyPI package: https://pypi.org/project/python-boilerplate/
* Created by: **[Karthik](https://audrey.feldroy.com/)** | GitHub https://github.com/KaRtHiK-56 | PyPI https://pypi.org/user/KaRtHiK-56/
* Free software: MIT License

## Features

* TODO

## Documentation

Documentation is built with [Zensical](https://zensical.org/) and deployed to GitHub Pages.

* **Live site:** https://KaRtHiK-56.github.io/python_boilerplate/
* **Preview locally:** `just docs-serve` (serves at http://localhost:8000)
* **Build:** `just docs-build`

API documentation is auto-generated from docstrings using [mkdocstrings](https://mkdocstrings.github.io/).

Docs deploy automatically on push to `main` via GitHub Actions. To enable this, go to your repo's Settings > Pages and set the source to **GitHub Actions**.

## Development

To set up for local development:

```bash
# Clone your fork
git clone git@github.com:your_username/python-boilerplate.git
cd python-boilerplate

# Install in editable mode with live updates
uv tool install --editable .
```

This installs the CLI globally but with live updates - any changes you make to the source code are immediately available when you run `python_boilerplate`.

Run tests:

```bash
uv run pytest
```

Run quality checks (format, lint, type check, test):

```bash
just qa
```

## Author

JEV_Expirements was created in 2026 by Karthik.

Built with [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and the [audreyfeldroy/cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) project template.
