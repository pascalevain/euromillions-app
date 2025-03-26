import pandas as pd
import numpy as np
import streamlit as st
from fpdf import FPDF

# Configuration de la page
st.set_page_config(page_title="Euromillions V4.0 Expert", layout="centered")

# Authentification simple par mot de passe
PASSWORD = "1701"
mot_de_passe = st.sidebar.text_input("Mot de passe", type="password")
if mot_de_passe != PASSWORD:
    st.error("Accès restreint. Veuillez entrer le mot de passe.")
    st.stop()
st.sidebar.success("Accès confirmé. Mode Expert activé.")

# Titre de l'application
st.title("🎯 Optimisation Euromillions V4.0 - Mode Expert")
st.markdown("_Développé par **Pascal EVAIN**_")

# Imports des modules
from markov import analyse_markov
from arima import prevision_arima, score_arima
from context import score_contexte
from pareto import score_pareto
from meta_distributions import analyser_meta_distribution, score_meta_distribution
from diagnostic import tester_toutes_les_fonctions, afficher_rapport_diagnostic
from pdf_export import exporter_pdf

# Interface principale
st.title("📊 Lancement de l'optimisation complète")
st.markdown("Cette version applique **l'intégralité** de la méthodologie V4.0, incluant l'analyse contextuelle, temporelle, markovienne, et les méta-distributions.")

# Chargement automatique depuis GitHub
st.header("1. Importer l'historique des tirages")

@st.cache_data
def charger_historique_depuis_github():
    url = url = "https://raw.githubusercontent.com/pascalevain/euromillions-app/main/euromillions_bitmap_maj_final.csv"

"
    return pd.read_csv(url)

historique = charger_historique_depuis_github()
st.success(f"Historique chargé automatiquement : {len(historique)} tirages.")
st.dataframe(historique.tail(10))

# Paramètres utilisateur
st.header("2. Paramètres de génération")
n_large = st.selectbox("🎯 Nombre de grilles (spectre large)", [5, 10, 20])
n_croisée = st.selectbox("🔁 Nombre de grilles (analyse croisée)", [5, 10, 20])
n_recent = st.selectbox("📉 Grilles basées sur X tirages récents", [2, 4, 6, 8, 10])
instructions = st.text_area("📋 Consignes personnalisées pour guider la génération")

# Lancer l'analyse
if st.button("🚀 Lancer l'analyse et générer les grilles optimisées"):
    markov_result = analyse_markov(historique)
    arima_result = prevision_arima(historique)
    contexte = score_contexte(historique)
    meta_result = analyser_meta_distribution(historique)

    pareto_grilles = score_pareto(markov_result, arima_result, contexte, meta_result,
                                  n_large, n_croisée, n_recent)

    st.success(f"✅ {len(pareto_grilles)} grilles optimisées générées.")
    for i, (nums, stars, score) in enumerate(pareto_grilles):
        st.markdown(f"**Grille {i+1}** 🎱 : {' - '.join(map(str, nums))} ⭐ {' & '.join(map(str, stars))} → Score : {score:.2f}")

    exporter_pdf(pareto_grilles, instructions)
    st.download_button("📄 Télécharger le rapport PDF", "rapport_euromillions_v4.pdf", mime="application/pdf")

# Diagnostic
if st.checkbox("🧪 Activer le mode diagnostic"):
    resultats_test = tester_toutes_les_fonctions(historique)
    afficher_rapport_diagnostic(resultats_test)
