def score_contexte(historique):
    results = {}
    for i in range(len(historique)):
        score = sum(historique.iloc[i, 1:6]) % 10
        results[i] = {"nums": [], "stars": [], "score": score}
    return results
