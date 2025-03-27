
def score_pareto(markov, arima, context, meta, n_large, n_croisee, n_recent):
    grilles = []
    for i in markov:
        try:
            score = (
                markov[i]["score"] +
                arima[i]["score"] +
                context[i]["score"] +
                meta[i]["score"]
            )
            grilles.append((
                markov[i]["nums"],
                markov[i]["stars"],
                score
            ))
        except KeyError as e:
            print(f"Clé manquante pour l'index {i} : {e}")
            continue

    grilles.sort(key=lambda x: x[2], reverse=True)
    return grilles[:max(n_large, n_croisee, n_recent)]
