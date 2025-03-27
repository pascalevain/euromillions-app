import streamlit as st
st.set_page_config(page_title="Euromillions V4.0 Expert", layout="centered")

import pandas as pd
import numpy as np
from fpdf import FPDF

from markov import analyse_markov
from arima import prevision_arima, score_arima
from context import score_contexte
from pareto import score_pareto
from diagnostic import tester_toutes_les_fonctions, afficher_rapport_diagnostic
from pdf_export import exporter_pdf
from meta_functions import analyser_meta_distribution, score_meta_distribution

# Le reste de l’interface est ici volontairement retiré (car déplacé dans app.py).

