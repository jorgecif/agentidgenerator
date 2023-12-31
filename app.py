import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
#import cv2
import numpy as np
#from tempfile import NamedTemporaryFile
from PIL import Image,ImageEnhance
import os
from RoboArt import roboart
ra = roboart()


imagenProfile="images\saa.png"

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img


st.set_page_config(layout="centered", page_icon="🎓", page_title="ID  Generator")
st.title("🎓 Generador de ID del Agente")

st.write(
    "Generador de ID Agente Evoke"
)

left, right = st.columns(2)

right.write("Here's the template we'll be using:")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")



left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Student name")
uploaded_file = st.file_uploader("Upload your file here...")

if uploaded_file is not None:
    file_details = {"Filename":uploaded_file.name,"FileType":uploaded_file.type,"FileSize":uploaded_file.size}
    st.write(file_details)
    imagenSubida = Image.open(uploaded_file)
    st.text("Original Image")
    st.image(uploaded_file,use_column_width=True)


image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
if image_file is not None:
    file_details = {"FileName":image_file.name,"FileType":image_file.type}
    st.write(file_details)
    img = load_image(image_file)
    st.image(img,caption=None,width=250)
    with open(os.path.join("tempDir",image_file.name),"wb") as f: 
      f.write(image_file.getbuffer())         
    st.success("Saved File")



course = form.selectbox(
    "Choose course",
    ["Report Generation in Streamlit", "Advanced Cryptography"],
    index=0,
)
grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        imagen=imagenSubida,
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False, css='style.css')
    st.balloons()

    right.success("🎉 Your diploma was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )


generarAvatar = form.form_submit_button("Generar Avatar")

if generarAvatar:
    # You can use any random string hash, it doesnt matter
    Robot = ra.robo("Robot") # It generates a robot avatar
    Monster = ra.monster("Monster") # It generates a monster avatar
    RoboHead = ra.robohead("Head") # It generates a robot head avatar
    Kittens = ra.kitten('cats') # It generates a cat avatar

    print(Robot) # prints robo

