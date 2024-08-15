import streamlit as st
from pathlib import Path

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "files" / "Muhammad_Rizwan_Aslam_Resume.pdf"
profile_image = current_dir / "files" / "pic.png"

# Styling of the expander headers
st.markdown("""
  <style>
    .st-emotion-cache-13bfgw8 p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 20px;
            }
  </style>
""", unsafe_allow_html=True)

def display_cv():

    col1, col2 = st.columns([3, 1])

    with col1:
        # st.header("Curriculum Vitae")
        st.write("### Muhammad Rizwan Aslam")
        st.write("**Email:** rizwanaslam.work@gmail.com")
        st.write("**LinkedIn:** [LinkedIn Profile](https://www.linkedin.com/in/rizwan-aslam-cs/)")
        st.write("**GitHub:** [GitHub Profile](https://github.com/Rithub14)")

    with col2:
        st.image(str(profile_image))

    st.write("##### Hi! I am Rizwan, a ML engineer with focused experience in generative AI and diverse ML areas, passionate about leveraging AI to solve complex business challenges across industries. #####")

    with st.expander("Education 🎓"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("**MSc Artificial Intelligence** - Brandenburg University of Technology")
            st.write("**BSc Computer Science** - COMSATS University Islamabad, Pakistan")
        
        with col2:
            st.write("Germany (2023 - 2025)")
            st.write("Pakistan (2019 - 2023)")


    with st.expander("Skills 👩‍💻"):
        st.write("**Programming Languages:** Python, SQL, Java")
        st.write("**Libraries/Frameworks:** Numpy, Pandas, Matplotlib, Scikit-learn, OpenCV, PyTorch, HuggingFace, LangChain, Streamlit, Spring Boot")
        st.write("**Tools:** Git, Docker, VS Code, Jupyter Notebook, Google Colab")
        st.write("**Cloud Platforms:** AWS (SageMaker, Bedrock)")
        st.write("**Soft Skills:** Time management, Problem-solving, Critical thinking, Collaboration")
    
    with st.expander("Experience 🚧"):
        st.write("**Data Science Intern** - Machine Learning 1, Lahore, Pakistan (May 2023 – July 2023)")
        st.write("• Engineered an automated text extraction system processing 1000+ documents from diverse formats.")
    
        st.write("**Software Developer Intern** - ABACUS Consulting, Lahore, Pakistan (May 2021 – July 2021)")
        st.write("• Implemented an algorithm leveraging Spring Boot to generate and read QR codes seamlessly.")

    with st.expander("Projects 🏆"):
        st.write("**RAG (Retrieval-Augmented Generation)** | LangChain - OpenAI - Pinecone - Streamlit")
        st.write("• Deployed a Streamlit web application for document processing")

        st.write("**Comic AI** | OpenAI - Stable Diffusion - Streamlit")
        st.write("• Created an AI-powered comic strip generator using OpenAI and Stable Diffusion.")
    
    with st.expander("Certifications 🥇"):
        st.write("• Machine Learning Specialization - DeepLearning.AI")
        st.write("• Deep Learning Specialization - DeepLearning.AI")

    # Button to download the resume/cv
    with open(resume_file, "rb") as file:
        st.download_button("Download CV", file, "Muhammad_Rizwan_Aslam_Resume.pdf")