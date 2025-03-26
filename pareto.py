import pandas as pd
import numpy as np
import streamlit as st


def score_pareto(bitmap_df, grille):
    """
    Calcule un score basé sur le principe de Pareto 80/20.
    Les 20 % des boules les plus fréquentes représentent 80 % des présences.
    """
    frequences = bitmap_df.iloc[:, :50].sum().sort_values(ascending=False)
    top_20_percent = int(0.2 * len(frequences))
    top_boules = set(frequences.head(top_20_percent).index)
    score = sum(1 for boule in grille if boule - 1 in top_boules)
    return score / len(grille) if grille else 0.0


def diagnostic_execution(fonction, *args, **kwargs):
    import time
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

    resultat, duree = diagnostic_execution(score_pareto, bitmap_df, grille)
    rapport["score_pareto"] = {"valeur": resultat, "temps": duree}

    return rapport


def afficher_rapport_diagnostic(rapport):
    st.subheader("\U0001F4CB Rapport de diagnostic : modules exécutés")
    for nom, details in rapport.items():
        st.write(f"**{nom}** → Score : {details['valeur']:.4f} | Temps : {details['temps']:.4f} sec")
