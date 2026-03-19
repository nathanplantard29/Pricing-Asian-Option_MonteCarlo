import numpy as np

# on importe la fonction qui définit le prix de l'option asiatique
from pricing import get_asian_price

# on définit les paramètres 
S = 7500            # prix de l'actif
r = 0.03            # rendement sûr
sigma = 0.20        # nervosité du marché
T = 1.0             # temps en années
N = 252             # nombre morceaux dans l'année (cenvention N=252)
n_simu = 10000      # nombre de simulations
K = 7500            # strike
h_delta = 1.0       # le pas pour le delta
h_sigma = 0.01      # le pas pour sigma
h_rho = 0.001       # le pas pour rho
seed = 123          # graine

# on utilise la fonction
prix, delta, vega, gamma, rho = get_asian_price(S,r,sigma,T,N,n_simu,K,h_delta,h_sigma,h_rho,seed)

# affichage
print(f"Le prix de l'option asiatique est de : {prix:.2f} $")
print(f"Le Delta de l'option est de : {delta:.3f}")
print(f"Le Vega de l'option est de : {vega*0.01:.3f}")
print(f"Le Gamma de l'option est de : {gamma:.6f}")
print(f"Le Rho de l'option est de : {rho:.6f}")

