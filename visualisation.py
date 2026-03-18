import matplotlib.pyplot as plt
from simulation import generate_paths

# on définit les paramètres 
S, r, sigma, T, N, n_simu = 7500, 0.03, 0.20, 1.0, 252, 10000

# on utilise la fonction
paths = generate_paths(S, r, sigma, T, N, n_simu)

# affichage 
plt.figure(figsize=(10, 6))
plt.plot(paths[:, :10]) 

plt.title(f"Simulation Monte-Carlo : 10 trajectoires de l'indice (S0={S})")
plt.xlabel("Jours de bourse")
plt.ylabel("Prix de l'indice")
plt.grid(True, alpha=0.3)
plt.axhline