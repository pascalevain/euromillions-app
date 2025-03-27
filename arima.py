import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

def prevision_arima(historique):
    previsions = {}
    for i in range(len(historique)):
        score = 0
        try:
            ligne = historique.iloc[i, 1:6].astype(float)
            moyenne = ligne.mean()
            score = moyenne  # ou une vraie prévision basée sur ARIMA
        except Exception:
            score = 0
        previsions[i] = {"nums": [], "stars": [], "score": score}
    return previsions

def score_arima(arima_result):
    sorted_results = sorted(arima_result.items(), key=lambda x: x[1]['score'], reverse=True)
    return [(res[1]['nums'], res[1]['stars'], res[1]['score']) for res in sorted_results]
