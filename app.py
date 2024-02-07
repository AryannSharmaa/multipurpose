import streamlit as st 
import os
import google.generativeai as genai 
from dotenv import load_dotenv

load_dotenv()

api=os.getenv("api")

genai.configure(api_key=api)

model=genai.GenerativeModel('gemini-pro')

# response=(model.generate_content(""))
st.set_page_config(page_title="Home")

st.write("# Assistant")

