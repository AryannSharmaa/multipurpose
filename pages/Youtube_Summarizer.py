import streamlit as st 

st.write("# Paste link of video")
title=st.text_input("link",placeholder="link")

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)