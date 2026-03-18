import numpy as np

# on définit une fonction pour déterminer le prix d'une option asiatique
def get_asian_price(S, r, sigma, T, N, n_simu, K, h, seed):

# on importe la fonction qui génère les chemins depuis un autre fichier
    from simulation import generate_paths

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

    np.random.seed(seed)
    paths_bumped = generate_paths(S+h, r, sigma, T, N, n_simu)
    mean_colomns_b = np.mean(paths_bumped, axis = 0)
    payoff_bumped = np.maximum(0, mean_colomns_b - K)     
    price_bumped = np.mean(payoff_bumped)*np.exp(-r*T)

    delta = (price_bumped - price_ref)/h

    return price_ref, delta