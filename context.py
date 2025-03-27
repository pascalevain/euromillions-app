import numpy as np

def score_contexte(historique):
    resultats = {}
    for i in range(10):
        resultats[i] = {
            "nums": list(np.random.choice(range(1, 51), 5, replace=False)),
            "stars": list(np.random.choice(range(1, 13), 2, replace=False)),
            "score": np.random.rand()
        }
    return resultats
