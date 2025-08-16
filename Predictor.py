import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open("C:/Users/royav/Downloads/Disease Prediction using ML/Models/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("C:/Users/royav/Downloads/Disease Prediction using ML/Models/heart_disease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("C:/Users/royav/Downloads/Disease Prediction using ML/Models/parkinsons_model.sav", 'rb'))
breast_cancer_model = pickle.load(open("C:/Users/royav/Downloads/Disease Prediction using ML/Models/breast_cancer_model.sav", 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           icons=[
                                    'activity',      # Diabetes Prediction (activity glyph)
                                    'heart-pulse-fill',         # Heart Disease Prediction (heart glyph)
                                    'person',        # Parkinson's Prediction (person glyph)
                                    'gender-female'   # Breast Cancer Prediction (shield-check glyph)
                                ],
                           default_index = 0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    #page title
    st.title('Diabetes Prediction using ML')

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    #page title
    st.title('Heart Disease Prediction using ML')

# Parkinsons Prediction Page
if selected == 'Parkinsons Prediction':
    #page title
    st.title('Parkinsons Prediction using ML')

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    #page title
    st.title('Breast Cancer Prediction using ML')