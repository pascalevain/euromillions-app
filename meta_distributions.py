
import pandas as pd
import numpy as np

# Fonction d’analyse des méta-distributions
def analyser_meta_distribution(historique):
    # Exemple de calcul : moyenne par ligne des valeurs numériques (hors date)
    scores = historique.iloc[:, 1:].mean(axis=1)
    resultats = {
        i: {
            "nums": [],  # Les numéros ne sont pas définis à ce niveau
            "stars": [],  # Les étoiles non plus
            "score": score
        }
        for i, score in enumerate(scores)
    }
    return resultats

# Fonction de tri basée sur les scores
def score_meta_distribution(meta_result):
    sorted_items = sorted(meta_result.items(), key=lambda x: x[1]["score"], reverse=True)
    return [(item[1]["nums"], item[1]["stars"], item[1]["score"]) for item in sorted_items]
