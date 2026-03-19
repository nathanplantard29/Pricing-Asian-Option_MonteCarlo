import numpy as np

# on importe la fonction qui génère les chemins depuis un autre fichier
from simulation import generate_paths

# on définit une fonction pour déterminer le prix d'une option asiatique
def get_asian_price(S, r, sigma, T, N, n_simu, K, h_delta, h_sigma, h_rho, seed):

# référence
# pour avoir les mêmes simulations de référence et bumpé
    np.random.seed(seed)
# on appelle la fonction
    paths_ref = generate_paths(S, r, sigma, T, N, n_simu)
# c'est une option asiatique donc on calcule la moyenne des variations de toutes les simulations
    mean_colomns_r = np.mean(paths_ref, axis = 0)
# on utilise la formule du Payoff
    payoff_ref = np.maximum(0, mean_colomns_r - K)     
# on calcule la moyenne des gains possibles et on y retire le taux d'intérêt
    price_ref = np.mean(payoff_ref)*np.exp(-r*T)

# delta
    np.random.seed(seed)
    paths_delta = generate_paths(S+h_delta, r, sigma, T, N, n_simu)
    mean_colomns_delta = np.mean(paths_delta, axis = 0)
    payoff_delta = np.maximum(0, mean_colomns_delta - K)     
    price_delta = np.mean(payoff_delta)*np.exp(-r*T)
    delta = (price_delta - price_ref)/h_delta

# sigma
    np.random.seed(seed)
    paths_sigma = generate_paths(S, r, sigma+h_sigma, T, N, n_simu)
    mean_colomns_sigma = np.mean(paths_sigma, axis = 0)
    payoff_sigma = np.maximum(0, mean_colomns_sigma - K)     
    price_sigma = np.mean(payoff_sigma)*np.exp(-r*T)
    vega = (price_sigma - price_ref)/h_sigma * 0.01

# gamma
    np.random.seed(seed)
    paths_gamma = generate_paths(S-h_delta, r, sigma, T, N, n_simu)
    mean_colomns_gamma = np.mean(paths_gamma, axis = 0)
    payoff_gamma = np.maximum(0, mean_colomns_gamma - K)     
    price_gamma = np.mean(payoff_gamma)*np.exp(-r*T)
    gamma = (price_delta + price_gamma - 2*price_ref)/(h_delta**2)


    np.random.seed(seed)
    paths_rho = generate_paths(S, r+h_rho, sigma, T, N, n_simu)
    mean_colomns_rho = np.mean(paths_rho, axis = 0)
    payoff_rho = np.maximum(0, mean_colomns_rho - K)     
    price_rho = np.mean(payoff_rho)*np.exp(-(r+h_rho)*T)
    rho = (price_rho - price_ref)/h_rho * 0.01

    return price_ref, delta, vega, gamma, rho
