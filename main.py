import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
import openai
import os 
import PyPDF2 as pdf

from dotenv import load_dotenv

load_dotenv()

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text


prompt = PromptTemplate(
    template ="""Hey Act like a skilled or very experienced ATS (Application Tracking System) 
    with a deep understanding of tech field, software engineering, data science, data analyst and big data engineer.
    Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide best assistance for improving the resumes.
    Assign the percentage Matching based on Jd and the missing keywords with high accuracy
    resume: {text}
    description: {jd}


    I want the response in one single string having the structure {{ "JD Match":"%", "MissingKeywords":[],"Profile Summary":"" }}
    """,
  input_variables=['text','jd']   
)

parser =StrOutputParser()

llm = ChatOpenAI(model = "gpt-4o-mini",temperature = 0.2)

chain = prompt | llm | parser


st.title("SMART ATS")
st.text("Improve your Resume ATS")
jd=st.text_area("Paste the job description")
uploaded_file=st.file_uploader("Upload your resume ",type="pdf",help= "please upload the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        result = chain.invoke({"text": text, "jd": jd})

        st.subheader(result)

