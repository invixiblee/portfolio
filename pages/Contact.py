
import streamlit as st
from send_email import semail

st.title('Contact Me!')

with st.form(key='form'):
    useremail = st.text_input("Your Email Adress:")
    rawmessage = st.text_area("Your Message:")
    message = f"""\
Subject: Portfolio Contact - From {useremail}

From: {useremail}
{rawmessage}
"""
    button = st.form_submit_button('Submit')
    if button:
        semail(message)
        st.info("Your email was delivered successfully!")
