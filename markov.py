import numpy as np
import pandas as pd
from collections import defaultdict

def analyse_markov(bitmap_df, ordre=3):
    """
    Analyse markovienne d'ordre supérieur (par défaut ordre 3) sur l'historique.
    Retourne les probabilités de transition pour chaque combinaison possible.
    """
    transitions = defaultdict(lambda: defaultdict(int))

    lignes = bitmap_df.drop(columns=["date"]).values.tolist()

    for i in range(len(lignes) - ordre):
        contexte = tuple(tuple(lignes[i + j]) for j in range(ordre))
        prochaine = tuple(lignes[i + ordre])
        transitions[contexte][prochaine] += 1

    probabilites = {}

    for contexte, suites in transitions.items():
        total = sum(suites.values())
        proba = {k: v / total for k, v in suites.items()}
        probabilites[contexte] = proba

    return probabilites

def probabilite_grille(grille_binaire, model_markov, ordre=3):
    """
    Calcule la probabilité d'une grille à partir du modèle markovien.
    """
    if len(model_markov) == 0:
        return 0.0

    score_total = 0
    n = len(grille_binaire)

    for i in range(n - ordre):
        contexte = tuple(grille_binaire[j] for j in range(i, i + ordre))
        suivante = tuple(grille_binaire[i + ordre])
        proba = model_markov.get(contexte, {}).get(suivante, 0.0001)
        score_total += np.log(proba)

    return np.exp(score_total / (n - ordre))
