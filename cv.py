import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

import os
from rag import pinecone_index, gpt_answer
from dotenv import load_dotenv
from openai import OpenAI 

# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
resume_file = current_dir / "files" / "Muhammad_Rizwan_Aslam_Resume.pdf"
profile_image = current_dir / "files" / "pic.png"
github_logo = current_dir / "files" / "github_logo.svg"
linkedin_logo = current_dir / "files" / "linkedin_logo.svg"
gmail_logo = current_dir / "files" / "gmail_logo.svg"

# Social Media Links
gmail_url = "mailto:rizwanaslam.work@gmail.com"
linkedin_url = "https://www.linkedin.com/in/rizwan-aslam-cs/"
github_url = "https://github.com/Rithub14"

# Load environment variables from .env file
load_dotenv()

MODEL="gpt-4o-mini"
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found.")

client = OpenAI(api_key=api_key)

# Function to increase the size of expander label 
st.set_page_config(layout="wide", initial_sidebar_state="expanded")

def ChangeWidgetFontSize(wgt_txt_list, wch_font_size):
    text_conditions = "".join(
        f"if (elements[i].innerText == '{txt}') {{ elements[i].style.fontSize = '{wch_font_size}'; }}" 
        for txt in wgt_txt_list
    )
    
    htmlstr = f"""<script>
                    var elements = window.parent.document.querySelectorAll('*');
                    for (var i = 0; i < elements.length; ++i) {{
                        {text_conditions}
                    }}
                  </script>"""
    
    components.html(htmlstr, height=0, width=0)

def display_cv():
    col1, col2 = st.columns([3, 1])
    with col2:
        st.image(str(profile_image), use_column_width=True)

    with col1:
        st.write("# Muhammad Rizwan Aslam")
        
        col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
        # Wrapper for logos
        st.markdown('<div style="display: flex; flex-direction: column; align-items: flex-start;">', unsafe_allow_html=True)
        with col1:        
            # Gmail logo with bottom margin
            with open(gmail_logo, "r") as svg_file:
                gmail_logo_svg = svg_file.read()
                st.markdown(
                    f'<a href="{gmail_url}" target="_blank"><div style="width:50px;height:50px;margin-bottom:20px;">{gmail_logo_svg}</div></a>', 
                    unsafe_allow_html=True
                )
        with col2:
            # LinkedIn logo with bottom margin
            with open(linkedin_logo, "r") as svg_file:
                linkedin_logo_svg = svg_file.read()
                st.markdown(
                    f'<a href="{linkedin_url}" target="_blank"><div style="width:40px;height:40px;margin-bottom:20px;">{linkedin_logo_svg}</div></a>', 
                    unsafe_allow_html=True
                ) 
        with col3:
            # GitHub logo with no bottom margin
            with open(github_logo, "r") as svg_file:
                github_logo_svg = svg_file.read()
                st.markdown(
                    f'<a href="{github_url}" target="_blank"><div style="width:40px;height:40px;">{github_logo_svg}</div></a>', 
                    unsafe_allow_html=True
                )
        st.markdown('</div>', unsafe_allow_html=True) 

    # Button to download the resume/cv
    with open(resume_file, "rb") as file:
        st.download_button("Download CV", file, "Muhammad_Rizwan_Aslam_Resume.pdf")

    st.write("#### ML engineer with focused experience in generative AI and diverse ML areas, passionate about leveraging AI to solve complex business challenges across industries. #####")

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
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("**Data Science Intern** | Machine Learning 1, Lahore, Pakistan")
        with col2:
            st.write("(May 2023 – July 2023)")
        st.write("• Engineered an automated text extraction system processing 1000+ documents from diverse formats (PDF, Word, images), streamlining data integration for 30 targeted resume templates and reducing manual processing time")
        st.write("• Contributed to the development of robust datasets for computer vision models by performing image annotation for object detection using LabelImg")

        col1, col2 = st.columns([3, 1])
        with col1:
            st.write("**Software Developer Intern** | ABACUS Consulting, Lahore, Pakistan")
        with col2:
            st.write("(May 2021 – July 2021)")
        st.write("• Implemented an algorithm leveraging Spring Boot to generate and read QR codes seamlessly")
        st.write("• Conducted thorough testing and debugging of the QR code algorithm to ensure reliability and accuracy")

    with st.expander("Projects 🏆"):
        st.write("**RAG (Retrieval-Augmented Generation)** | LangChain - OpenAI - Pinecone - Streamlit")
        st.write("• Deployed a Streamlit app that processes documents, stores embeddings in Pinecone, and uses LangChain’s RetrievalQA with GPT-3.5 for AI-powered document querying")

        st.write("**Comic AI** | OpenAI - Stable Diffusion - Streamlit")
        st.write("• Created an AI-powered comic strip generator that transforms user scenarios into 6-panel comics, using OpenAI's API for text and Stable Diffusion for images")

        st.write("**Deep learning approach for mango variety identification using UAV imagery** | PyTorch - Streamlit")
        st.write("• Developed a deep learning model to identify and classify mango varieties from UAV imagery using YOLOv5 and YOLOv7 and created a Streamlit web app to showcase and interact with the model trained on over 12,000 images.")

    with st.expander("Certifications 🥇"):
        st.write("• Machine Learning Specialization - DeepLearning.AI")
        st.write("• Deep Learning Specialization - DeepLearning.AI")
        st.write("• Python for Data Science and Machine Learning Bootcamp- Udemy")

    # RAG
    vector_store = pinecone_index()
    query = st.text_input('Ask GPT anything about me:', placeholder="Educational Background / Work Experience / Projects")
    if query:
        answer = gpt_answer(vector_store, query, k=5)
        st.text_area('LLM Expert:', answer, height=300)

    list_of_wgt_txt = ['Skills 👩‍💻', 'Education 🎓', 'Experience 🚧', 'Projects 🏆', 'Certifications 🥇', 'Ask GPT anything about me:']
    ChangeWidgetFontSize(list_of_wgt_txt, '20px')