# BuildMetaData

BuildMetaData is an app made for creating metadata from images individually. Also, with the app it is possible to add
a different background for the image depending on the rarity. The app is based on the TkInter-Lib. So that the project
dependencies can be resolved correctly, Py-Poetry was used.

The folder structure is shown below. Note that the folders `image_bg_png`, `image_bg_webp` and `metadata` are generated
automatically. The folder, where the images (`image`) should be located and in which also a folder for the background
images (`background`) is, must be created manually. Keep in mind that the folder of the background images has to be a
subfolder of the image folder. It is helpful here that the equipment images are also created as subfolders (`equipment`)
of the image folder.

```
├── BuildMetaData
│   ├── models
│   └── views
├── env
├── image
│   ├── background
│   ├── equipment
├── image_bg_png
├── image_bg_webp
├── metadata
└── tests
```

# DEVELOPMENT

# GENERAL

The app is using TKinter that is why you have to install the tkinter framework. If you are using Paru as
package installer type: `paru -Sy tk`

## RUN

    # start
    # before each cmd run:
    make env # enables virtual env

    # the app runs
    make run

    # the app tests
    make test

    # the tests coverage
    make cov

    # remove output folders (metadata, image_bg_png/webp)
    make clean

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
