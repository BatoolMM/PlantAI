
from fastai.vision.all import *
from fastai.vision.widgets import *
from IPython.display import Image
from ipywidgets import * 
from PIL import Image
import streamlit as st
from pyngrok import ngrok


path = Path()
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("PlantAI")
st.write('''
  ---
  ## **Which Plant is This**?
   This is simple Web application to classify the type of the plants I have in my home and provide instruction of taking care of it.
  ### Please ask me anything!  
''')
Uploaded = st.file_uploader('', type=['png','jpg','jpeg'])

with st.spinner('Loading your picture into memory'):
  model = load_learner('/content/export.pkl')
  time.sleep(1)

if Uploaded is not None:
    img = Image.open(Uploaded)
    img_fastai = PILImage.create(Uploaded)
    st.image(img, caption='This is your uploaded picture', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    pred,pred_idx,probs = model.predict(img_fastai)
    st.write("Prediction: ", pred, "; Probability: ", probs[pred_idx]*100,'%')
