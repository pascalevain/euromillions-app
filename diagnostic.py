import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
from collections import Counter
import time
import streamlit as st

def prevision_arima(bitmap_df, colonne=0, ordre=(2, 1, 0), horizon=1):
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
    scores = []
    for boule in grille:
        prevision = prevision_arima(bitmap_df, colonne=boule - 1, horizon=horizon)[-1]
        scores.append(prevision)
    return float(np.mean(scores)) if scores else 0.0

def contexte_freq(bitmap_df, taille_fenetre=5):
    recent = bitmap_df.tail(taille_fenetre)
    frequences = recent.sum().sort_values(ascending=False)
    return list(frequences.index[:10])

def score_contexte(bitmap_df, grille, taille_fenetre=5):
    boules_frequentes = contexte_freq(bitmap_df, taille_fenetre)
    score = sum(1 for boule in grille if boule - 1 in boules_frequentes)
    return score / len(grille) if grille else 0.0

def diagnostic_execution(fonction, *args, **kwargs):
    debut = time.time()
    resultat = fonction(*args, **kwargs)
    fin = time.time()
    duree = fin - debut
    return resultat, duree

def tester_toutes_les_fonctions(bitmap_df, grille):
    rapport = {}

    resultat, duree = diagnostic_execution(score_arima, bitmap_df, grille)
    rapport["score_arima"] = {"valeur": resultat, "temps": duree}

    resultat, duree = diagnostic_execution(score_contexte, bitmap_df, grille)
    rapport["score_contexte"] = {"valeur": resultat, "temps": duree}

    return rapport

def afficher_rapport_diagnostic(rapport):
    st.subheader("\U0001F4CB Rapport de diagnostic : modules exécutés")
    for nom, details in rapport.items():
        st.write(f"**{nom}** → Score : {details['valeur']:.4f} | Temps : {details['temps']:.4f} sec")
