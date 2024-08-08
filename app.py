# imports
import streamlit as st
from home import home
from cv import display_cv
from jokes import generate_joke

# main
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", [
        "Home",
        "Curriculum Vitae",
        "Jokes by AI"
    ])

    if page == "Home":
        home()
    elif page == "Curriculum Vitae":
        display_cv()
    elif page == "Jokes by AI":
        generate_joke()

if __name__ == "__main__":
    main()