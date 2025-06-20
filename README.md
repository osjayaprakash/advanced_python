# Setup

[![Build Stats](https://github.com/osjayaprakash/notes/workflows/deploy-book/badge.svg)](https://github.com/osjayaprakash/notes/actions)


## Build Locally

To build the book locally you need to install [Jupyter Book](https://jupyterbook.org/en/stable/intro.html):

Setup the github repo:
```zsh
gh auth login 
gh repo clone osjayaprakash/notes
```

Install sublime text editor:
```zsh
brew install --cask sublime-text sublime-merge
pip3 install notebook
```

```zsh
cd $HOME && python3 -m venv cs230 && cd - 
source ~/cs230/bin/activate
python3 -m pip install -U jupyter-book
```

With [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) installed you can build the book locally as follows:

```bash
# From the root directory of the repository
jupyter-book build .
```

The HTML of the book are located in the `_build/html` directory. Open the `index.html` file to land on the home page of the book.

## Developing

This repo uses pre-commit, so after cloning run `pip install -r requirements.txt` and `pre-commit install` prior to committing.
If you have already committed, but your PR is failing because of a pre-commit error, run `pre-commit run --all`
