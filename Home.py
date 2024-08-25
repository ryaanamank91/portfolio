import streamlit as st
# from PIL import Image
import pandas

st.set_page_config(layout="wide")

# Display the homepage header
st.header("Home", anchor=None)

# create two columns for row1 in the webpage
column_left_row1, column_right_row1 = st.columns([0.5, 2])

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
    requirement analysis for ADAS and infotainment systems. 
    My core competencies include Embedded SW development (Python, C and C++)
    Automotive SPICE (ASPICE), Agile Project Management, Product Operations, and System Architecture Framework. 
    I hold an MBA in International Business and two MSc degrees in Automotive Engineering for Sustainable Mobility from 
    prestigious institutions. My mission is to deliver high-quality, innovative, and customer-centric products that 
    enhance the user experience and sustainability of mobility.
    """

    description = st.info(content1)

# Add second row
content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
brief = st.write(content2)

# create two more columns for row3 in the webpage
column_left_row3, empty_column, column_right_row3 = st.columns([1.5, 0.5, 1.5])

# to read data from .csv file and store it as a dataframe
df = pandas.read_csv('data.csv', sep=';')

with column_left_row3:
    for index, row in df[:10].iterrows():  # divide the content of csv into 2 columns
        st.header(row['title'])  # to write the titles from .csv file for first column
        st.write(row['description'])  # to write the description from .csv file for the second column
        st.image("images/" + row["image"])  # to generate images
        st.write(f"[Source Code]({row['url']})")  # to insert the links

with column_right_row3:
    for index, row in df[10:].iterrows():  # divide the content of csv into 2 columns
        st.header(row['title'])  # to write the titles from .csv file for the second column
        st.write(row['description'])  # to write the description from .csv file for the second column
        st.image("images/" + row["image"])  # to generate images
        st.write(f"[Source Code]({row['url']})")  # to insert the links
