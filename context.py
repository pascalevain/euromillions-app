import numpy as np

def score_contexte(df):
    try:
        # Normalisation simple des colonnes numériques
        data = df.select_dtypes(include=[np.number])
        if data.empty:
            raise ValueError("Aucune donnée numérique trouvée dans le fichier d'historique.")

        normalisé = (data - data.min()) / (data.max() - data.min())
        score = normalisé.mean(axis=1)

        # Exemple : retour de 5 grilles fictives (à adapter)
        grilles = []
        for i in range(5):
            nums = sorted(np.random.choice(range(1, 51), 5, replace=False))
            stars = sorted(np.random.choice(range(1, 13), 2, replace=False))
            grilles.append((nums, stars, score.iloc[-1]))

        return grilles
    except Exception as e:
        raise ValueError(f"Erreur dans score_contexte : {e}")
