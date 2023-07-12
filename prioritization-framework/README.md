# Prioritization Framework Publication

The framework enables the prioritization of ML best practices using the optimization described in our paper 
_"Best Practices for Machine Learning Systems: 
An Industrial Framework for Analysis and Optimization"_ ([Arxiv](https://arxiv.org/abs/2306.13662)). The notebook
`results.ipynb` reproduces the paper's results.

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

The influence scores of practices - sub characteristics can be found in the `data` folder. If you want to prioritize
new practices, you have to score them and add them as input to the framework.