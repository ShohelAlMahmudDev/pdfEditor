import streamlit as st
from streamlit_option_menu import option_menu
from features import mergepdf, splitpdf, modifypdf, convertdoctopdf, settings

def main():
    """
    Main function to run the Streamlit app.
    """
    # Create a navigation menu
    with st.sidebar:
        selected = option_menu(
            menu_title="Main Menu",  # Title of the menu
            options=["Home", "Merge PDF", "Split PDF", "Modify PDF", "Docx to Pdf", "Settings"],  # Menu options
            icons=["house", "file-earmark-plus", "file-earmark-minus", "pencil", "file-pdf", "gear"],  # Corresponding icons
            menu_icon="list",  # Icon for the menu
            default_index=0  # Default selected option
        )

    # Render pages based on selection
    if selected == "Home":
        render_home()
    elif selected == "Merge PDF":
        mergepdf.render()
    elif selected == "Split PDF":
        splitpdf.render()
    elif selected == "Modify PDF":
        modifypdf.render_modify_pdf()
    elif selected == "Docx to Pdf":
        convertdoctopdf.render()
    elif selected == "Settings":
        settings.render()
    else:
        st.error("Invalid selection. Please choose a valid option from the menu.")

def render_home():
    """
    Function to render the Home page.
    """
    st.title("Home")
    st.markdown(
        """
        ## Welcome to the PDF Toolkit
        This application provides powerful tools for managing PDF files, including merging, splitting, and modifying PDFs.
        Use the menu on the left to navigate through the features.
        """
    )

if __name__ == "__main__":
    main()
