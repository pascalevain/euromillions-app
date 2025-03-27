from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "Rapport Euromillions V4.0 - Grilles Optimisées", ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, 'C')

def exporter_pdf(grilles, instructions=""):
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    if instructions:
        pdf.multi_cell(0, 10, f"📋 Consignes : {instructions}")

    pdf.ln(5)
    for i, (nums, stars, score) in enumerate(grilles):
        texte = f"Grille {i+1} : {' - '.join(map(str, nums))} + {' & '.join(map(str, stars))} → Score : {score:.2f}"
        pdf.cell(0, 10, txt=texte.encode('latin-1', 'replace').decode('latin-1'), ln=True)

    # Génère le fichier PDF dans le dossier courant
    pdf.output("rapport_euromillions_v4.pdf")
