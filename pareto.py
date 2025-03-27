def score_pareto(markov, arima, context, meta, n1, n2, n3):
    # Vérification que tous les résultats sont valides
    if not all([markov, arima, context, meta]):
        raise ValueError("Erreur : au moins un des résultats d’analyse est vide ou invalide.")

    grilles = []

    # Exemple très simplifié : score basé sur une combinaison pondérée des résultats
    for i in range(n1):
        score = markov[2] + arima[2] + context[2] + meta[2]
        grilles.append(([1, 2, 3, 4, 5], [1, 2], score))  # grille fictive

    return grilles
