# Prioritization Framework Publication

This repository contains all the supplement material for the paper _"Best Practices for Machine Learning Systems: 
An Industrial Framework for Analysis and Optimization"_ ([Arxiv](https://arxiv.org/abs/2306.13662), [Researchgate](https://www.researchgate.net/publication/371686085_Best_Practices_for_Machine_Learning_Systems_An_Industrial_Framework_for_Analysis_and_Optimization)).

## How to reproduce the paper's results?

### Install requirements

Install the required libraries by running:

`pip install -r requirements.txt`

### Launch the notebook with the results

Open the notebook `results.ipynb` and run all the cells.

## How to run the prioritization framework?

The algorithms are implemented in `prioritization_framework.py`:

1. `get_n_practices_brute_force`
2. `get_n_practices_greedy`

They do not require any additional packages, only a python 3.7+ environment.