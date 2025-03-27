import pandas as pd

# Fonction de scoring Pareto multi-critères

def score_pareto(markov, arima, contexte, meta, n_large=5, n_croisee=5, n_recent=5):
    grilles = {}
    # Fusionner toutes les grilles par index commun
    for i in markov:
        try:
            score = (
                markov[i]["score"] +
                arima[i]["score"] +
                contexte[i]["score"] +
                meta[i]["score"]
            )
            grilles[i] = {
                "nums": markov[i]["nums"],
                "stars": markov[i]["stars"],
                "score": score
            }
        except Exception as e:
            continue

    # Trier par score décroissant
    grilles_tries = sorted(grilles.items(), key=lambda x: x[1]["score"], reverse=True)

    # Découper les résultats selon les paramètres
    resultats = []
    count = 0
    for i, (idx, val) in enumerate(grilles_tries):
        if count >= (n_large + n_croisee + n_recent):
            break
        resultats.append((val["nums"], val["stars"], val["score"]))
        count += 1

    return resultats
