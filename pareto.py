def score_pareto(markov, arima, context, meta, n_large, n_croisee, n_recent):
    grilles = []

    for i in markov:
        try:
            score = (
                markov[i]["score"]
                + arima[i]["score"]
                + context[i]["score"]
                + meta[i]["score"]
            )
            nums = markov[i]["nums"]
            stars = markov[i]["stars"]
            grilles.append((nums, stars, score))
        except Exception as e:
            print(f"Erreur à l'index {i}: {e}")
            continue

    grilles = sorted(grilles, key=lambda x: x[2], reverse=True)
    return grilles[:n_large + n_croisee + n_recent]
