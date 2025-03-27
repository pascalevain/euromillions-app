def score_pareto(markov, arima, context, meta, n1, n2, n3):
    grilles = []

    # Vérification que chaque résultat contient bien une clé [2]
    try:
        score = markov[2] + arima[2] + context[2] + meta[2]
    except KeyError as e:
        raise KeyError(f"Clé manquante dans l'un des dictionnaires de résultats : {e}")
    except Exception as e:
        raise ValueError(f"Erreur inattendue dans le calcul de score Pareto : {e}")

    for i in range(n1):
        grilles.append(([1, 2, 3, 4, 5], [1, 2], score))  # grille fictive

    return grilles
