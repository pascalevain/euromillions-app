import pandas as pd
import numpy as np
import streamlit as st
from fpdf import FPDF

from markov import analyse_markov
from arima import prevision_arima, score_arima
from context import score_contexte
from pareto import score_pareto
from diagnostic import tester_toutes_les_fonctions, afficher_rapport_diagnostic
from pdf_export import exporter_pdf

from meta_functions import analyser_meta_distribution, score_meta_distribution  # <- import corrigé

# Interface principale
st.set_page_config(page_title="Euromillions V4.0 Expert", layout="centered")
st.title("🎯 Optimisation Euromillions V4.0 - Mode Expert")
st.markdown("_Développé par **Pascal EVAIN**_")

st.title("📊 Lancement de l'optimisation complète")
st.markdown("Cette version applique **l'intégralité** de la méthodologie V4.0, incluant l'analyse contextuelle, temporelle, markovienne, et les méta-distributions.")

# Chargement automatique depuis GitHub ou fichier local
st.header("1. Importer l'historique des tirages")

@st.cache_data
def charger_historique():
    try:
        url = "https://raw.githubusercontent.com/pascalevain/euromillions-app/main/euromillions_bitmap_maj_final.csv"
        df = pd.read_csv(url)
        st.success(f"✅ Historique chargé depuis GitHub : {len(df)} tirages.")
        return df
    except Exception as e:
        st.warning("⚠️ Impossible de charger le fichier depuis GitHub. Veuillez importer un fichier local (.csv)")
        return None

historique = charger_historique()

if historique is None:
    fichier = st.file_uploader("📂 Importer un fichier CSV local", type=["csv"])
    if fichier:
        historique = pd.read_csv(fichier)
        st.success(f"✅ Fichier local chargé : {len(historique)} tirages.")

if historique is not None:
    st.dataframe(historique.tail(10))

# Paramètres utilisateur
st.header("2. Paramètres de génération")
n_large = st.selectbox("🎯 Nombre de grilles (spectre large)", list(range(0, 21)))
n_croisée = st.selectbox("🔁 Nombre de grilles (analyse croisée)", list(range(0,_

