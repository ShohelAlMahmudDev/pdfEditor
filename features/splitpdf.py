import streamlit as st
from PyPDF2 import PdfReader,PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
import os
import base64

def render():
    st.title("Split PDF")
    st.write("Welcome to Split PDF!")

    uploaded_file=st.file_uploader("Upload a PDF",type="pdf")
    #split PDF
    if uploaded_file: 
        if st.button("Split"):
            reader = PdfReader(uploaded_file)
            for i, page in enumerate(reader.pages):
                writer = PdfWriter()
                writer.add_page(page)
                split_pdf = BytesIO()
                writer.write(split_pdf)
                split_pdf.seek(0)
                st.markdown(
                f'<iframe src="data:application/pdf;base64,{base64.b64encode(split_pdf.getvalue()).decode()}" '
                f'width="700" height="500"></iframe>',
                unsafe_allow_html=True,
                )
                st.download_button(f"Download Page {i + 1}", data=split_pdf, file_name=f"page_{i + 1}.pdf")
