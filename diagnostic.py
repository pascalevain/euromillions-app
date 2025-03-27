import pandas as pd
import streamlit as st

def tester_toutes_les_fonctions(historique):
    try:
        nb_tirages = len(historique)
        nb_colonnes = historique.shape[1]

        tests = {
            "Tirages chargés": nb_tirages,
            "Colonnes disponibles": nb_colonnes,
            "Valeurs nulles": historique.isnull().sum().sum(),
            "Lignes dupliquées": historique.duplicated().sum(),
        }

        tests["Format OK"] = isinstance(historique, pd.DataFrame)

        return tests

    except Exception as e:
        return {"Erreur": str(e)}


def afficher_rapport_diagnostic(resultats):
    st.subheader("🩺 Rapport de diagnostic")
    for cle, valeur in resultats.items():
        st.markdown(f"**{cle}** : {valeur}")
