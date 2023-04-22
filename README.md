# BuildMetaData
BuildMetaData is an app made for creating metadata from images individually. Also, with the app it is possible to add
a different background for the image depending on the rarity. The app is based on the TkInter-Lib. So that the project 
dependencies can be resolved correctly, Py-Poetry was used. 


# DEVELOPMENT
## RUN

    # start 
    # before each cmd run:
    make env # enables virtual env

    # the app runs 
    make run

    # the app tests 
    make test

    # the tests cov 
    make cov

## POETRY
    # install poetry 
    curl -sSL https://install.python-poetry.org | python3 -

    # activate poetry 
    poetry shell 

    # install dependencies
    poetry install

    # add further packages
    poetry add {package_name}

## VERSIONING

This repository strictly uses [conventional
commits](https://bitbucket.org/blog/pipelines-manual-steps-confidence-deployment-pipeline).
As such, a pre-commit hook checks your commit message.

## Pre-commit hooks

We highly encourage you to install pre-commit hooks and **also** enable access
to commit messages via:

    pre-commit install
    pre-commit install --hook-type commit-msg

Optionally, you may want to use
[commitizen](https://github.com/commitizen-tools/commitizen) and `cz c` to
construct your commit messages.
