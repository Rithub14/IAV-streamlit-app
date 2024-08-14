import streamlit as st
from home import home
from cv import display_cv
from jokes import display_joke

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Choose a page", [
        "Home",
        "Curriculum Vitae",
        "Joke Generator"
    ])

    if page == "Home":
        home()
    elif page == "Curriculum Vitae":
        display_cv()
    elif page == "Joke Generator":
        display_joke()

if __name__ == "__main__":
    main()