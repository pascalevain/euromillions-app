import pandas as pd
import numpy as np
from fpdf import FPDF

from markov import analyse_markov
from arima import prevision_arima, score_arima
from context import score_contexte
from pareto import score_pareto
from diagnostic import tester_toutes_les_fonctions, afficher_rapport_diagnostic
from pdf_export import exporter_pdf

# Fonctions d’analyse des méta-distributions
def analyser_meta_distribution(historique):
    """
    Calcule un score simple basé sur la moyenne des colonnes 1 à 5 du fichier historique.
    Peut être remplacé par une méthode plus complexe ultérieurement.
    """
    scores = historique.iloc[:, 1:6].mean(axis=1)
    return {i: score for i, score in enumerate(scores)}

def score_meta_distribution(meta_result):
    """
    Trie les résultats de méta-distribution par score décroissant.
    """
    return sorted(meta_result.items(), key=lambda x: x[1], reverse=True)


