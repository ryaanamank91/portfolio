import streamlit as st
from PIL import Image
import pandas

st.set_page_config(layout="wide")

# Display the homepage header
st.header("Home", anchor=None)

# create two columns for row1 in the webpage
column_left_row1, column_right_row1 = st.columns(2)

# First column and row1 content
with column_left_row1:
    image = st.image('images/photo.jpg')
    # alternative method to open the image
    # Load image
    # img = Image.open('images/photo.jpg')

    # Resize the image
    # img_resized = img.resize((500, 600))  # width: 300px and height: 200px

    # Display the resized image
    # st.image(img_resized)

# Second Column and row1 content
with column_right_row1:
    st.title("Ryaan Amank Semwal")
    content1 = """
    Hi, I am Ryaan Amank Semwal! I am a Technical Project Lead @EXCELTIC, a global leader in providing consulting 
    solutions in the automotive sector, with my current focus on sensor fusion and upcoming microcontrollers 
    for automotive.. 
    With over 9 years of experience in the automotive industry, 
    I have successfully led and managed teams and projects in product development, system engineering, and 
    requirement analysis for ADAS and infotainment systems. """

    description = st.info(content1)

# Add second row
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
brief = st.write(content2)

# create two more columns for row3 in the webpage
column_left_row3, column_right_row3 = st.columns(2)

df = pandas.read_csv('data.csv', sep=';')

with column_left_row3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])

with column_right_row3:
    for index, row in df[10:].iterrows():
        st.header(row['title'])