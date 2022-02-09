import streamlit as st 
import pytesseract 
from PIL import Image #to read an image and display it

pytesseract.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'    #configuration settings 
st.title('OPTICAL CHARACTER RECOGNITION (OCR)')
st.text("Upload the image:")

uploaded_file = st.sidebar.file_uploader("Choose an image :", type=["jpg","png","jpeg"]) #upload these file types
if uploaded_file is not None:    #if there is some file in this variable(uploaded_file) only then execute the below commands
  img = Image.open(uploaded_file) #read the image 
  
  st.image(img, caption = 'Uploaded image', use_column_width =True) #display the image 

  st.write("") #prints blank line and empty space
  
  if st.button('PREDICT'):
    output = pytesseract.image_to_string(img)
    st.text(output)
