import pandas as pd

def tester_toutes_les_fonctions(historique):
    if not isinstance(historique, pd.DataFrame):
        return {"erreur": "Format de l'historique invalide"}
    tests = {
        "lignes": len(historique),
        "colonnes": historique.shape[1],
        "colonnes_vides": historique.isnull().sum().to_dict()
    }
    return tests

def afficher_rapport_diagnostic(resultats):
    import streamlit as st
    st.subheader("🧪 Rapport de Diagnostic")
    for cle, valeur in resultats.items():
        st.write(f"**{cle}** : {valeur}")
