import streamlit as st
from openai import OpenAI 
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MODEL="gpt-4o-mini"
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found.")

client = OpenAI(api_key=api_key)

def generate_joke(humor_type, content_theme, audience, delivery_style):
    completion = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Your task is to tell me a joke!"}, # <-- This is the system message that provides context to the model
        {"role": "user", "content": f'Generate a {humor_type} {content_theme} joke for a {audience} audience with a {delivery_style} delivery style:'}
        ]
    )

    joke = completion.choices[0].message.content
    return joke

def display_joke():
    st.title("Generate a Joke")

    # User selections
    humor_type = st.selectbox("Select type of humor:", [
        "Puns", "One-Liners", "Riddles", "Knock-Knock Jokes", "Anecdotes", "Observational Humor", "Dark Humor"
    ])
    content_theme = st.selectbox("Select content/theme:", [
        "Animals", "Technology", "Workplace", "Relationships", "Food & Drink", "School & Education", "Sports"
    ])
    audience = st.selectbox("Select audience:", [
        "Family-Friendly", "Adult Humor", "Kids Jokes"
    ])
    delivery_style = st.selectbox("Select delivery style:", [
        "Sarcastic", "Self-Deprecating", "Dry Humor"
    ])

    if st.button("Generate Joke"):
        with st.spinner("Generating joke..."):
            joke = generate_joke(humor_type, content_theme, audience, delivery_style)
        st.write("Here's your joke:")
        st.write(joke)