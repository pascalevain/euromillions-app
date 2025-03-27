
import numpy as np

def analyse_markov(historique):
    resultats = {}
    for i in range(len(historique)):
        nums = list(range(1, 6))
        stars = list(range(1, 3))
        score = np.random.uniform(0, 1)
        resultats[i] = {"nums": nums, "stars": stars, "score": score}
    return resultats
