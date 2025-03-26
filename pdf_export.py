import pandas as pd
import numpy as np
import streamlit as st
from fpdf import FPDF

def score_pareto(bitmap_df, grille):
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

def exporter_pdf(grilles, consignes=""):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.set_text_color(40, 40, 40)
    pdf.cell(200, 10, txt="Rapport Expert Euromillions - V4.0", ln=True, align="C")
    pdf.ln(5)

    if consignes:
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 8, f"Consignes personnalisées :\n{consignes}")
        pdf.ln(3)

    for i, (nums, stars, score) in enumerate(grilles):
        grille_txt = f"Grille {i+1}: Nums = {sorted(nums)}, Étoiles = {sorted(stars)}, Score = {score:.2f}"
        pdf.cell(0, 8, grille_txt, ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", style="I", size=8)
    pdf.set_text_color(100)
    pdf.cell(0, 10, txt="Document généré automatiquement par Euromillions V4.0 Expert.", ln=True)

    return pdf.output(dest="S").encode("latin-1")
