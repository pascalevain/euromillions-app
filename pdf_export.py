from fpdf import FPDF

def exporter_pdf(grilles, instructions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Grilles optimisées Euromillions V4.0", ln=True, align="C")
    pdf.ln(10)
    if instructions:
        pdf.multi_cell(0, 10, txt=f"Consignes :\n{instructions}")
        pdf.ln(5)
    for i, (nums, stars, score) in enumerate(grilles):
        grille_str = f"Grille {i+1} : {', '.join(map(str, nums))} ⭐ {', '.join(map(str, stars))} (Score : {score:.2f})"
        pdf.cell(200, 10, txt=grille_str, ln=True)
    pdf.output("rapport_euromillions_v4.pdf")
