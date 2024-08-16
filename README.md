# IAV App

Welcome to IAV app! This project features a Python-based Streamlit app that includes my curriculum vitae and a joke generator powered by gpt-4o-mini.

## Project Overview

The application consists of the following pages:

1. **Home Page**: Displays a welcoming message and an animation.
2. **Curriculum Vitae**: Showcases my CV with detailed professional information.
3. **Joke Generator**: Uses gpt-4o-mini to generate and display jokes based on user preferences.

## Installation and Setup

To run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rithub14/IAV-streamlit-app.git
    ```
2. **Navigate to the Project Directory**:
    ```bash
    cd portfolio
    ```
3. **Set Up a Virtual Environment (optional but recommended)**:
    ```bash
    # On Windows:
    python -m venv venv
    venv\Scripts\activate
    ```
    ```bash
    # on macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```
4. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5. **Create a .env File**:
    ```bash
    OPENAI_API_KEY=your_openai_api_key
    ```
6. **Run the Application**:
    ```bash
    streamlit run app.py
    ```
## Folder Structure:
```
    IAV-APP/
    │
    ├── .streamlit/
    │   └── config.toml
    │
    ├── __pycache__/
    │
    ├── files/
    │   ├── animation.json
    │   ├── github_logo.svg
    │   ├── gmail_logo.svg
    │   ├── linkedin_logo.svg
    │   ├── Muhammad_Rizwan_Aslam_Resume.pdf
    │   └── pic.png
    │
    ├── .gitignore
    ├── README.md
    ├── app.py
    ├── cv.py
    ├── home.py
    ├── jokes.py
    └── requirements.txt
```