
from fpdf import FPDF

def exporter_pdf(grilles, instructions=""):
    if not grilles:
        print("⚠️ Aucune grille à exporter.")
        return

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Rapport Euromillions V4.0 Expert", ln=True, align="C")

    if instructions:
        pdf.multi_cell(0, 10, txt=f"Consignes personnalisées :\n{instructions}\n", align="L")

    for i, (nums, stars, score) in enumerate(grilles):
        pdf.cell(0, 10, txt=f"Grille {i+1} : {nums} ⭐ {stars} → Score : {score:.2f}", ln=True)

    pdf.output("rapport_euromillions_v4.pdf")
