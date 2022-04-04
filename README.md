# Coin game
This is an analysis of a coin game.

## Rules the of game:
```
●
●●
●●●
●●●●
```
We have four rows with coins. The first row contains 1 coin, the second 2, the third 3 and
the fourth contains 4 coins. The players take turns. In each turn a player can remove an
arbitrary number (>=1) of coins from one row. He must take at least one coin. The player
who takes the last coin has lost the game.


## Setup
prerequisite: [miniconda or anaconda](https://docs.conda.io/en/latest/miniconda.html)

```sh
conda env create environment.yml
conda env update environment.yml
python setup.py develop
```


## Test
```sh
python tests/test_utils.py
```

## Demo Notebook
```sh
jupyter notebook
# navigate to noteboos/How_to_analyze_game.ipynb
```