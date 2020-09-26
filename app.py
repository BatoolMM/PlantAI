
from fastai.vision.all import *
from fastai.vision.widgets import *
from IPython.display import Image
from ipywidgets import * 
from PIL import Image
import streamlit as st
from pyngrok import ngrok
import urllib.request
import wget

path = Path()
st.set_option('deprecation.showfileUploaderEncoding', False)
st.title("PlantAI")
st.write('''
  ---
  ## **Which Plant is This**?
   This is simple Web application to classify four type of plants:
   **Schefflera**, 
   **Epipremnum aureum**,
   **Dieffenbachia**,
   **Dracaena**.
'''
)
st.image('https://dl.dropboxusercontent.com/s/2873nwxz55lrozc/plants.jpg?dl=0', use_column_width=True)
st.write('''
  ### Please upload a picture for one of these plants!  
''')
Uploaded = st.file_uploader('', type=['png','jpg','jpeg'])

with st.spinner('Loading your picture into memory'):
  url = wget.download('https://dl.dropboxusercontent.com/s/uahengnua8m3hbu/export.pkl?dl=0')
  model = load_learner(url)
  time.sleep(1)

if Uploaded is not None:
    img = Image.open(Uploaded)
    img_fastai = PILImage.create(Uploaded)
    st.image(img, caption='This is your uploaded picture', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    pred,pred_idx,probs = model.predict(img_fastai)
    st.write("Prediction: ", pred, "; Probability: ", probs[pred_idx]*100,'%  :sunglasses:')

