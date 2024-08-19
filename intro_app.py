import streamlit as st

#Title
st.title("IRIS EDA App")
st.write("Build with Streamlit"+"❤️")

#Header and Subheader
st.header("EDA App")
st.subheader("Iris Dataset")


#checkbox
if st.checkbox("Show Dataset"):
    st.text("Showing Dataset")

#Radio Button
gender=st.radio("What is your gender?",["Male","Female"])

if gender =='Male':
    st.text("Hello Guy")
else:
    st.text("Hello Miss")
#Selection
Occupation= st.selectbox("Occupation",("Programmer","Data Scientist","Doctor"))

#Slider
age=st.slider("Your Age",1,99)

#Buttons
if st.button("About Us"):
   st.text("Hello Us")

#write
st.write("Hello world")

#image
from PIL import Image
import os,datetime
st.image(Image.open(os.path.join('iris_setosa.jpg')))

#Dates
st.date_input("Today date",datetime.datetime.now())

# #Audio
# st.audio()

# #Video
# st.video()