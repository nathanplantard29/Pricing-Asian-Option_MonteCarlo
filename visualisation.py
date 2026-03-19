import matplotlib.pyplot as plt
import numpy as np
from simulation import generate_paths
from pricing import get_asian_price

# on définit les paramètres 
S = 7500            # prix de l'actif
r = 0.03            # rendement sûr
sigma = 0.20        # nervosité du marché
T = 1.0             # temps en années
N = 252             # nombre morceaux dans l'année (cenvention N=252)
n_simu = 10000      # nombre de simulations
K = 7500            # strike
h_delta = 1.0       # l