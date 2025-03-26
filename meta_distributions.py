import pandas as pd
import numpy as np

def analyser_meta_distribution(bitmap_df):
    """
    Analyse les méta-distributions en repérant les configurations statistiques globales et les cycles.
    Retourne un dictionnaire avec des caractéristiques de régime.
    """
    meta_infos = {}

    # Moyennes par colonne (boules 1-50)
    moyennes = bitmap_df.iloc[:, :50].mean()
    ecarts = bitmap_df.iloc[:, :50].std()

    # Top 10 les plus probables
    top_boules = list(moyennes.sort_values(ascending=False).head(10).index)

    meta_infos["moyennes"] = moyennes.to_dict()
    meta_infos["ecarts_types"] = ecarts.to_dict()
    meta_infos["top_boules"] = top_boules

    # Analyse de changement de régime (variation brutale de moyenne glissante)
    rolling_mean = bitmap_df.iloc[:, :50].rolling(window=10).mean()
    variation = rolling_mean.diff().abs().mean(axis=1)
    points_inflexion = variation[variation > variation.mean() + variation.std()].index.tolist()

    meta_infos["points_inflexion"] = points_inflexion

    return meta_infos

def score_meta_distribution(grille, meta_infos):
    """
    Score une grille selon sa conformité avec les top boules dominantes du régime actuel.
    """
    top_boules = meta_infos.get("top_boules", [])
    score = sum(1 for b in grille if b - 1 in top_boules)
    return score / len(grille) if grille else 0.0
