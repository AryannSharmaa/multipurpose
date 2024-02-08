import streamlit as st 
import os
import google.generativeai as genai 
from dotenv import load_dotenv
import PIL.Image 


load_dotenv()
api=os.getenv("api")
genai.configure(api_key=api)

def picture(pic,text="Give detailed info about this"):
    if pic:
        if text:
            with st.spinner("processing"):
                pic=PIL.Image.open(pic)
                model=genai.GenerativeModel('gemini-pro-vision')
                response = model.generate_content([text, pic], stream=True)
                response.resolve()
                st.write(response.text) 
                
def text_assist(text):
    if text:
            with st.spinner("processing"):
                model=genai.GenerativeModel('gemini-pro')
                response=model.generate_content(text)
                st.write(response.text)
                
                



st.set_page_config(page_title="Home")
st.write("# Assistant")
st.subheader("Ask me anything")
pic=st.file_uploader("Upload Image")
text=st.text_input(label='text')
if pic:
    picture(pic,text)
else:
    text_assist(text)


