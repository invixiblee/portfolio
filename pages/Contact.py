
import streamlit as st

st.title('Contact Me!')

with st.form(key='form'):
    useremail = st.text_input("Your Email Adress:")
    message = st.text_area("Your Message:")
    button = st.form_submit_button('Submit')
    if button:
        message = message + useremail
