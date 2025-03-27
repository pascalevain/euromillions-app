from fpdf import FPDF

# Création d'un PDF simple avec encodage compatible
def exporter_pdf(grilles, instructions=""):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.set_auto_page_break(auto=True, margin=15)

    titre = "Rapport de Grilles Optimisées"
    pdf.cell(200, 10, txt=titre.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    if instructions:
        texte = f"Consignes : {instructions}"
        texte = texte.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, txt=texte)

    for i, (nums, stars, score) in enumerate(grilles):
        texte = f"Grille {i+1} : {nums} + {stars} → Score : {score:.2f}"
        texte = texte.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(200, 10, txt=texte, ln=True)

    pdf.output("rapport_euromillions_v4.pdf")
