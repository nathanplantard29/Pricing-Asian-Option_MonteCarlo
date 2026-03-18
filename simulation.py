import numpy as np

# on définit une fonction qui va générer des chemins en donnant tout les paramètres nécessaire
def generate_paths(S, r, sigma, T, N, n_simu):

# on découpe les T années par des N petits morceaux (par convention N=252 jours de bourses en 1 an)
    dt = T/N        

# on créé une matrice de N lignes et n_simu colonnes remplit de variables aléatoire tiré d'une loi normale centrée réduite 
    Z = np.random.standard_normal((N, n_simu))     

# on donne la formule du Mouvement Brownien Géométrique.
    daily_returns = np.exp((r-0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z)

# on mutliplie le prix de départ S par le produit cummulé de chaque jours de bourse (effet boule de neige)
    paths = S * np.cumprod(daily_returns, axis = 0)

# on créé 1 ligne de n_simu colonnes où chaque case contient le prix de départ S
    start_points = np.full((1, n_simu), S)

# on empile verticalement des blocks qui représente les variations de chaque jours de bourses les uns sur les autres
    full_paths = np.vstack([start_points, paths])

    return full_paths