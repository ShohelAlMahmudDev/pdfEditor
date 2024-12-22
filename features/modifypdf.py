import streamlit as st
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import pdfplumber
from io import BytesIO
import base64


def render_modify_pdf():
    """
    Function to render the Modify PDF page with text search and replace capability using pdfplumber.
    """
    st.title("Modify PDF")
    st.write("Upload a PDF file to search and replace text in real-time.")

    # File uploader
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

    if uploaded_file:
        # PDF Preview
        st.subheader("PDF Preview")
        st.markdown(
            f'<iframe src="data:application/pdf;base64,{base64.b64encode(uploaded_file.getvalue()).decode()}" '
            f'width="700" height="500"></iframe>',
            unsafe_allow_html=True,
        )

        # Search and Replace
        st.subheader("Search and Replace Text")
        search_text = st.text_input("Text to Search")
        replace_text = st.text_input("Text to Replace")

        # Replace Button
        if st.button("Replace Text"):
            try:
                modified_pdf = BytesIO()
                writer = PdfWriter()

                with pdfplumber.open(uploaded_file) as pdf:
                    for page in pdf.pages:
                        # Extract text from the page
                        page_content = page.extract_text()
                        if page_content and search_text in page_content:
                            # Replace text
                            updated_content = page_content.replace(search_text, replace_text)

                            # Generate a new PDF page with the updated text
                            packet = BytesIO()
                            c = canvas.Canvas(packet, pagesize=letter)
                            text_object = c.beginText(50, 750)  # Starting position
                            text_object.setFont("Helvetica", 12)

                            for line in updated_content.splitlines():
                                text_object.textLine(line)

                            c.drawText(text_object)
                            c.save()

                            # Add the new page to the writer
                            packet.seek(0)
                            new_pdf_reader = PdfReader(packet)
                            writer.add_page(new_pdf_reader.pages[0])
                        else:
                            # Add the original page back if unchanged
                            packet = BytesIO(page.to_pdf())
                            writer.add_page(PdfReader(packet).pages[0])

                # Save the modified PDF
                writer.write(modified_pdf)
                modified_pdf.seek(0)

                st.success("Text replaced successfully!")
                st.download_button(
                    "Download Modified PDF", data=modified_pdf, file_name="modified.pdf"
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")


# Entry point for the Streamlit app
if __name__ == "__main__":
    render_modify_pdf()
