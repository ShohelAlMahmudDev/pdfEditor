import streamlit as st
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO

def convert_docx_to_pdf(docx_file, pdf_file):
    """
    Convert a .docx file to a .pdf file using reportlab and python-docx.
    """
    # Load the Word document
    doc = Document(docx_file)

    # Create a PDF canvas
    pdf = canvas.Canvas(pdf_file, pagesize=letter)

    # Starting position for text
    y_position = 750

    # Iterate through the paragraphs and write to the PDF
    for paragraph in doc.paragraphs:
        if y_position < 50:  # Start a new page if the current page is full
            pdf.showPage()
            y_position = 750

        pdf.drawString(50, y_position, paragraph.text)
        y_position -= 20  # Adjust line spacing

    # Save the PDF
    pdf.save()

# Streamlit App
def render():
    # Add a title with a pencil icon
    st.title("📝 DOCX to PDF Converter")
    st.write("Upload a DOCX file to convert it into a PDF.")

    # File uploader for DOCX file
    uploaded_file = st.file_uploader("Upload a DOCX file", type="docx")

    if uploaded_file:
        st.success("File uploaded successfully!")

        # Convert the uploaded DOCX file to PDF
        output_pdf = BytesIO()
        convert_docx_to_pdf(uploaded_file, output_pdf)

        # Prepare PDF file for download
        output_pdf.seek(0)

        # Add a pencil icon to the download button
        st.download_button(
            label="🖋️ Download PDF",
            data=output_pdf,
            file_name=uploaded_file.name + "_converted.pdf",
            mime="application/pdf"
        )
