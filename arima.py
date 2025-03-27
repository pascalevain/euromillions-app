import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def prevision_arima(bitmap_df):
    scores = []
    for colonne in range(1, bitmap_df.shape[1]):
        try:
            serie = pd.to_numeric(bitmap_df.iloc[:, colonne], errors="coerce").dropna()
            if len(serie) < 10:
                scores.append(0)  # Trop peu de données
                continue

            modele = ARIMA(serie, order=(2, 0, 1))
            resultat = modele.fit()
            prediction = resultat.forecast()[0]
            scores.append(prediction)
        except Exception as e:
            scores.append(0)  # En cas d’erreur ARIMA, on attribue 0
    return scores

def score_arima(scores):
    if not scores:
        return []
    try:
        max_score = max(scores)
        if max_score == 0:
            return [0] * len(scores)
        return [s / max_score for s in scores]
    except Exception:
        return [0] * len(scores)
