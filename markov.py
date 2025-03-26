import numpy as np
from collections import defaultdict

def build_transition_matrix(data, order=3):
    """
    Construit une matrice de transition markovienne d'ordre supérieur.
    """
    transitions = defaultdict(lambda: defaultdict(int))

    for i in range(len(data) - order):
        prev_state = tuple(data[i:i + order])
        next_state = data[i + order]
        transitions[prev_state][next_state] += 1

    matrix = {}
    for state, next_states in transitions.items():
        total = sum(next_states.values())
        matrix[state] = {k: v / total for k, v in next_states.items()}

    return matrix

def predict_next_numbers(matrix, recent_sequence, top_n=5):
    """
    Prédit les prochaines valeurs probables à partir de la matrice.
    """
    state = tuple(recent_sequence)
    if state in matrix:
        sorted_probs = sorted(matrix[state].items(), key=lambda x: x[1], reverse=True)
        return [num for num, _ in sorted_probs[:top_n]]
    return []

def analyse_markov(bitmap, order=3):
    """
    Applique l'analyse markovienne à l'historique bitmap.
    """
    historical_data = []

    # Convertir le bitmap en une séquence plate d’indices tirés (1 à 50)
    for _, row in bitmap.iterrows():
        nums = [i for i, v in enumerate(row[:-12], start=1) if v == 1]
        historical_data.extend(nums)

    # Générer la matrice de transition
    matrix = build_transition_matrix(historical_data, order=order)

    # Extraire les dernières valeurs observées pour la prédiction
    recent = historical_data[-order:]
    prediction = predict_next_numbers(matrix, recent, top_n=5)

    return prediction
