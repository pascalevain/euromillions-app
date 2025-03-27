from fpdf import FPDF
import streamlit as st
from io import BytesIO

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
        texte = texte.encode('latin-1', 'replace').decode('latin-1')  # Pour éviter les erreurs Unicode
        pdf.cell(0, 10, txt=texte, ln=True)

    # Écriture dans un buffer mémoire (et non fichier disque)
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    # Bouton de téléchargement dans Streamlit
    st.download_button(
        label="📄 Télécharger le rapport PDF",
        data=buffer,
        file_name="rapport_euromillions_v4.pdf",
        mime="application/pdf"
    )
