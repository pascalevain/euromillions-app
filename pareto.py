def score_pareto(markov, arima, contexte, meta, n1, n2, n3):
    grilles = []
    for i in markov:
        try:
            score = markov[i]["score"] + arima[i]["score"] + contexte[i]["score"] + meta[i]["score"]
            grilles.append((markov[i]["nums"], markov[i]["stars"], score))
        except KeyError:
            continue
    grilles.sort(key=lambda x: x[2], reverse=True)
    return grilles[:n1 + n2 + n3]
