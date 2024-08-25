import streamlit as st
from send_email import send_email

# to set the layout of the webpage
st.set_page_config(layout='wide')

st.header("Contact Me")

# to implement a form
with st.form(key='email_form'):
    user_email = st.text_input("Your email address:")
    raw_message = st.text_area("Your message here:")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
