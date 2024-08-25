import streamlit as st

# to set the layout of the webpage
st.set_page_config(layout='wide')

st.header("Contact Me")

# to implement a form
with st.form(key='email_form'):
    user_email = st.text_input("Your email address:")
    message = st.text_area("Your message here:")
    button = st.form_submit_button("Submit")

    if button:
        message = message + user_email
