import streamlit as st
from PyPDF2 import PdfReader,PdfWriter
from reportlab.pdfgen import canvas
from io import BytesIO
import os
import base64

def render():
    st.title("Merged PDF")
    st.write("Welcome to Merged PDF!")

    #file merging
    merge_files=st.file_uploader("Select PDFs to Merge",type="pdf",accept_multiple_files=True)
    if merge_files:
        if st.button("Merge"):
            writer = PdfWriter()
            for pdf in merge_files:
                reader =PdfReader(pdf)
                for page in reader.pages:
                    writer.add_page(page)
            merged_pdf = BytesIO()
            writer.write(merged_pdf)
            merged_pdf.seek(0)
            st.subheader("Generated PDF Preview")
            st.markdown(
                f'<iframe src="data:application/pdf;base64,{base64.b64encode(merged_pdf.getvalue()).decode()}" '
                f'width="700" height="500"></iframe>',
                unsafe_allow_html=True,
            )
            st.download_button("Download Merged PDF",data=merged_pdf,file_name="merged.pdf")
