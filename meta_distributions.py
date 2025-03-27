import pandas as pd
import numpy as np
from fpdf import FPDF

from markov import analyse_markov
from arima import prevision_arima, score_arima
from context import score_contexte
from pareto import score_pareto
from diagnostic import tester_toutes_les_fonctions, afficher_rapport_diagnostic
from pdf_export import exporter_pdf
from meta_distributions import analyser_meta_distribution, score_meta_distribution

# Interface principale
st.title("🎯 Optimisation Euromillions V4.0 - Mode Expert")
st.markdown("_Développé par **Pascal EVAIN**_")

st.title("📊 Lancement de l'optimisation complète")
st.markdown("Cette version applique **l'intégralité** de la méthodologie V4.0, incluant l'analyse contextuelle, temporelle, markovienne, et les méta-distributions.")

# Chargement automatique depuis GitHub
st.header("1. Importer l'historique des tirages")

@st.cache_data
def charger_historique_depuis_github():
    url = "https://raw.githubusercontent.com/pascalevain/euromillions-app/main/euromillions_bitmap_maj_final.csv"
    return pd.read_csv(url)

historique = charger_historique_depuis_github()
st.success(f"✅ Historique chargé automatiquement : {len(historique)} tirages.")
st.dataframe(historique.tail(10))

# Paramètres utilisateur
st.header("2. Paramètres de génération")
n_large = st.selectbox("🎯 Nombre de grilles (spectre large)", list(range(0, 21)))
n_croisée = st.selectbox("🔁 Nombre de grilles (analyse croisée)", list(range(0, 21)))
n_recent = st.selectbox("📉 Grilles basées sur X tirages récents", list(range(0, 21)))
instructions = st.text_area("📋 Consignes personnalisées pour guider la génération")

# Lancer l'analyse
if st.button("🚀 Lancer l'analyse et générer les grilles optimisées"):
    markov_result = analyse_markov(historique)
    arima_result = prevision_arima(historique)
    contexte = score_contexte(historique)
    meta_result = analyser_meta_distribution(historique)

    grilles = score_pareto(markov_result, arima_result, contexte, meta_result,
                           n_large, n_croisée, n_recent)

    st.success(f"✅ {len(grilles)} grilles optimisées générées.")
    for i, (nums, stars, score) in enumerate(grilles):
        st.markdown(f"**Grille {i+1}** 🎱 : {' - '.join(map(str, nums))} ⭐ {' & '.join(map(str, stars))} → Score : {score:.2f}")

    exporter_pdf(grilles, instructions)
    st.download_button("📄 Télécharger le rapport PDF", "rapport_euromillions_v4.pdf", mime="application/pdf")

# Mode diagnostic (optionnel)
if st.checkbox("🧪 Activer le mode diagnostic"):
    resultats_test = tester_toutes_les_fonctions(historique)
    afficher_rapport_diagnostic(resultats_test)

