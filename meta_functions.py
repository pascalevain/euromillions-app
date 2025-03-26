import numpy as np
import pandas as pd
from collections import Counter

def analyser_meta_distribution(df):
    """
    Analyse simple : fréquence des boules (1 à 50) et étoiles (1 à 12)
    """
    freq_numeros = Counter()
    freq_etoiles = Counter()

    for _, row in df.iterrows():
        nums = [i for i, v in enumerate(row[:-2], 1) if v == 1]
        etoiles = [i for i, v in enumerate(row[-2:], 1) if v == 1]
        freq_numeros.update(nums)
        freq_etoiles.update(etoiles)

    return {
        "numeros": freq_numeros,
        "etoiles": freq_etoiles
    }

def score_meta_distribution(grille, meta_result):
    """
    Donne un score à une grille en fonction des fréquences observées.
    """
    nums, etoiles = grille
    score_nums = sum(meta_result["numeros"].get(n, 0) for n in nums)
    score_etoiles = sum(meta_result["etoiles"].get(e, 0) for e in etoiles)
    return score_nums + score_etoiles

