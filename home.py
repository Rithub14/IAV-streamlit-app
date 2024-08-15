import streamlit as st
import json
from streamlit_lottie import st_lottie
from pathlib import Path

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
animation = current_dir / "files" / "animation.json"

def load_lottie_json():
    with open(animation, 'r') as file:
        return json.load(file)
    
def home():
    st.title("Welcome to IAV Application")
    st.write("This is the Home Page. Please select an option from the sidebar to proceed.")

    lottie_json = load_lottie_json()
    
    st_lottie(lottie_json, speed=1, width=800, height=500, key="animation")