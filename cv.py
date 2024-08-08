import streamlit as st
from pathlib import Path

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "files" / "Muhammad_Rizwan_Aslam_Resume.pdf"

def display_cv():
    # Button to download the resume/cv
    # st.subheader("Download CV")
    with open(resume_file, "rb") as file:
        st.download_button("Download CV", file, "Muhammad_Rizwan_Aslam_Resume.pdf")

    st.header("Curriculum Vitae")
    st.write("### Muhammad Rizwan Aslam")
    st.write("**Email:** rizwanaslam.work@gmail.com")
    st.write("**LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/rizwan-aslam-cs/)")
    st.write("**GitHub:** [GitHub Profile](https://github.com/Rithub14)")
    
    st.subheader("Education 🎓")
    st.write("**MSc Artificial Intelligence** - Brandenburg University of Technology (BTU Cottbus), Germany (2023 - 2025)")
    st.write("**BSc Computer Science** - COMSATS University Islamabad, Pakistan (2019 - 2023)")

    st.subheader("Skills 👩‍💻")
    st.write("**Programming Languages:** Python, SQL, Java")
    st.write("**Libraries/Frameworks:** Numpy, Pandas, Matplotlib, Scikit-learn, OpenCV, PyTorch, HuggingFace, LangChain, Streamlit, Spring Boot")
    st.write("**Tools:** Git, Docker, VS Code, Jupyter Notebook, Google Colab")
    st.write("**Cloud Platforms:** AWS (SageMaker, Bedrock)")
    st.write("**Soft Skills:** Time management, Problem-solving, Critical thinking, Collaboration")
    
    st.subheader("Experience 🚧")
    st.write("**Data Science Intern** - Machine Learning 1, Lahore, Pakistan (May 2023 – July 2023)")
    st.write("• Engineered an automated text extraction system processing 1000+ documents from diverse formats.")
    
    st.write("**Software Developer Intern** - ABACUS Consulting, Lahore, Pakistan (May 2021 – July 2021)")
    st.write("• Implemented an algorithm leveraging Spring Boot to generate and read QR codes seamlessly.")

    st.subheader("Projects 🏆")
    st.write("**RAG (Retrieval-Augmented Generation)** - Deployed a Streamlit web application for document processing.")
    st.write("**Comic AI** - Created an AI-powered comic strip generator using OpenAI and Stable Diffusion.")
    
    st.subheader("Certifications 🥇")
    st.write("• Machine Learning Specialization - DeepLearning.AI")
    st.write("• Deep Learning Specialization - DeepLearning.AI")