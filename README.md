# Scalable API
This is project for studies. It's the simplest API example which is supposed to
work as "chat bot".

## Hot to install
Get [Poetry](https://python-poetry.org/) and then run:
`poetry install`

## How to run
`poetry run uvicorn main:app`

## How to test
`poetry run pytest`

## How to lint
### Linter (with autofix)
`poetry run black ./`

### Type checker
`poetry run mypy ./`
