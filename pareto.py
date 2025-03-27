
def score_pareto(markov_result, arima_result, contexte, meta_result, n_large, n_croisee, n_recent):
    all_scores = []

    for markov in markov_result:
        for arima in arima_result:
            for context in contexte:
                for meta in meta_result:
                    nums = markov[0]
                    stars = markov[1]
                    score = markov[2] + arima[2] + context[2] + meta[2]
                    all_scores.append((nums, stars, score))

    all_scores.sort(key=lambda x: x[2], reverse=True)

    top_n = n_large + n_croisee + n_recent
    return all_scores[:top_n]
