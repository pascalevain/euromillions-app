import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from collections import Counter

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

def contexte_freq(bitmap_df, taille_fenetre=5):
    """
    Analyse de la fréquence des boules dans une fenêtre glissante pour détecter les boules dominantes récemment.

    :param bitmap_df: Historique bitmap (sans colonne de date).
    :param taille_fenetre: Nombre de lignes (tirages) à prendre en compte.
    :return: Liste des boules les plus fréquentes dans la fenêtre.
    """
    recent = bitmap_df.tail(taille_fenetre)
    frequences = recent.sum().sort_values(ascending=False)
    return list(frequences.index[:10])

def score_contexte(bitmap_df, grille, taille_fenetre=5):
    """
    Calcule un score basé sur la présence des boules de la grille dans le contexte récent.

    :param bitmap_df: Historique bitmap.
    :param grille: Liste des boules de la grille à scorer (nombres de 1 à 50).
    :param taille_fenetre: Taille de la fenêtre pour analyser les fréquences.
    :return: Score basé sur les fréquences récentes.
    """
    boules_frequentes = contexte_freq(bitmap_df, taille_fenetre)
    score = sum(1 for boule in grille if boule - 1 in boules_frequentes)
    return score / len(grille) if grille else 0.0
