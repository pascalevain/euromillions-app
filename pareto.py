
def score_pareto(markov, arima, context, meta, n_large, n_croisee, n_recent):
    grilles = []
    for i in range(len(markov)):
        if i in arima and i in context and i in meta:
            score = markov[i]['score'] + arima[i]['score'] + context[i]['score'] + meta[i]['score']
            nums = markov[i]['nums']
            stars = markov[i]['stars']
            grilles.append((nums, stars, score))
    grilles.sort(key=lambda x: x[2], reverse=True)
    return grilles[:n_large + n_croisee + n_recent]
