import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA


def prevision_arima(bitmap_df, colonne=0, ordre=(2, 1, 0), horizon=1):
    """
    Applique un modèle ARIMA à une colonne spécifique du bitmap pour prédire la tendance future.
    Par défaut, prédit l'évolution de la première boule (colonne=0).

    :param bitmap_df: DataFrame bitmap avec colonnes 0 à 50 (valeurs 0 ou 1).
    :param colonne: Index de la colonne (boule) à analyser.
    :param ordre: Tuple ARIMA (p, d, q).
    :param horizon: Nombre de pas à prévoir.
    :return: Liste des prévisions sur 'horizon' pas.
    """
    serie = bitmap_df.iloc[:, colonne].astype(float)

    try:
        modele = ARIMA(serie, order=ordre)
        fit = modele.fit()
        forecast = fit.forecast(steps=horizon)
        return forecast.tolist()
    except Exception as e:
        print(f"Erreur ARIMA pour la colonne {colonne}: {e}")
        return [0.0] * horizon


def score_arima(bitmap_df, grille, horizon=1):
    """
    Calcule un score basé sur la tendance ARIMA pour chaque boule présente dans la grille.
    Plus le score est élevé, plus les boules correspondent aux tendances prédites.

    :param bitmap_df: Historique bitmap.
    :param grille: Liste des boules de la grille à scorer (nombres de 1 à 50).
    :param horizon: Nombre de pas à prévoir.
    :return: Score moyen de correspondance à la tendance.
    """
    scores = []
    for boule in grille:
        prevision = prevision_arima(bitmap_df, colonne=boule - 1, horizon=horizon)[-1]
        scores.append(prevision)

    return float(np.mean(scores)) if scores else 0.0
