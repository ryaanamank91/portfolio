import streamlit as st

st.set_page_config(layout="wide")

# Display the homepage header
st.header("Home", anchor=None)

# create two columns in the webpage

column_left, column_right = st.columns(2)

# First column content
with column_left:
    image = st.image('images/photo.jpg')

# Second Column content
with column_right:
    st.title("Ryaan Amank Semwal")
    content = """
    Hi, I am Ryaan Amank Semwal! I am a Technical Project Lead @EXCELTIC, a global leader in providing consulting 
    solutions in the automotive sector, with my current focus on sensor fusion and upcoming microcontrollers 
    for automotive.. 
    With over 9 years of experience in the automotive industry, 
    I have successfully led and managed teams and projects in product development, system engineering, and 
    requirement analysis for ADAS and infotainment systems. """

    description = st.info(content)