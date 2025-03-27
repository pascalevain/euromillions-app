import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def prevision_arima(historique):
    resultat = {}
    for i in range(len(historique)):
        ligne = historique.iloc[i, 1:6].values  # Nombres principaux
        etoiles = historique.iloc[i, 6:].values  # Étoiles
        score = 0
        try:
            for col in range(1, historique.shape[1]):
                serie = pd.to_numeric(historique.iloc[:, col], errors="coerce").dropna()
                if len(serie) < 10:
                    continue
                modele = ARIMA(serie, order=(2, 0, 1))
                fit = modele.fit()
                prediction = fit.forecast()[0]
                score += prediction
        except:
            score = 0
        resultat[i] = {
            "nums": list(ligne),
            "stars": list(etoiles),
            "score": score
        }
    return resultat
