import pandas as pd
import numpy as np
import streamlit as st
from fpdf import FPDF
st.set_page_config(page_title="Euromillions V4.0 Expert", layout="centered")

# Authentification simple par mot de passe
PASSWORD = "1701"
mot_de_passe = st.sidebar.text_input("Mot de passe", type="password")
if mot_de_passe != PASSWORD:
    st.error("Accès restreint. Veuillez entrer le mot de passe.")
    st.stop()

st.sidebar.success("Accès confirmé. Mode Expert activé.")

st.title("🎯 Optimisation Euromillions V4.0 - Mode Expert")
st.markdown("_Développé par **Pascal EVAIN**_")

from markov import analyse_markov
from arima import prevision_arima, score_arima
from context import score_contexte
from pareto import score_pareto
from meta_distributions import analyser_meta_distribution, score_meta_distribution
from diagnostic import tester_toutes_les_fonctions, afficher_rapport_diagnostic
from pdf_export import exporter_pdf

# Interface principale
st.set_page_config(page_title="Euromillions V4.0 Expert", layout="centered")
st.title("\U0001F3AF Optimisation Euromillions V4.0 Expert")
st.markdown("Cette version applique **l'intégralité de la méthodologie V4.0**, incluant l'analyse contextuelle, temporelle, markovienne, et les méta-distributions.\n")

# Chargement de l'historique
st.header("1. Importer l'historique complet des tirages")
fichier = st.file_uploader("Chargez ici le fichier bitmap (.csv) mis à jour :", type=["csv"])
if fichier:
    historique = pd.read_csv(fichier)
    st.success("Historique chargé : {} tirages".format(len(historique)))
    st.dataframe(historique.tail(10))

    # Paramètres utilisateur
    st.header("2. Paramètres de génération")
    n_large = st.selectbox("Nombre de grilles (spectre large)", [5, 10, 20])
    n_croisee = st.selectbox("Nombre de grilles (analyse croisée)", [5, 10])
    n_recent = st.selectbox("Grilles basées sur X tirages récents", [2, 4, 6, 8, 10])
    st.markdown("**\U0001F4DD Consignes personnalisées pour guider la génération**")
    instructions = st.text_area("me réaliser un rapport complet sur ce qui a été fait")

    if st.button("\U0001F52C Lancer l'analyse et générer les grilles optimisées"):
        # Modules d'analyse
        markov_result = analyse_markov(historique)
        arima_result = analyse_arima(historique)
        contexte = analyse_contexte(historique)
        meta_result = analyse_meta_distributions(historique)
        pareto_grilles = optimisation_pareto(markov_result, arima_result, contexte, meta_result,
                                             n_large, n_croisee, n_recent)

        st.success(f"\u2705 {len(pareto_grilles)} grilles optimisées générées.")
        for i, (nums, stars, score) in enumerate(pareto_grilles):
            st.markdown(f"**Grille {i+1}** : {sorted(nums)} + [{', '.join(map(str, stars))}]  → Score : `{score:.2f}`")

        # Diagnostic
        afficher_diagnostics()

        # Export PDF
        st.header("\U0001F4C4 Exporter le rapport PDF")
        if st.button("Télécharger le rapport PDF"):
            pdf = exporter_pdf(pareto_grilles, instructions)
            st.download_button("Télécharger le rapport PDF", data=pdf, file_name="rapport_euromillions_v4_expert.pdf")

else:
    st.info("Veuillez importer un fichier .csv pour activer l'analyse.")
