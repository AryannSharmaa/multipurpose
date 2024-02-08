import streamlit as st 
import os
import google.generativeai as genai 
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi as ytapi 


load_dotenv()
api=os.getenv("api")
genai.configure(api_key=api)
st.set_page_config(page_title="Summarize")

def yt_transcript(link):
    transcript=''
    text=ytapi.get_transcript(link,languages=['hi', 'en'])
    for i in range(len(text)):
        transcript+=(text[i]["text"])+" "
    return transcript

def summarize(transcript):
    
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(transcript+" summarize this in points")
    return response

st.write("# Paste link of video")

link=st.text_input("Link",placeholder="Paste link of video")

if link:
    link=link.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{link}/0.jpg")
    with st.spinner("Processing"):
        transcript=yt_transcript(link)
    
        response=summarize(transcript)

        st.write(response.text)