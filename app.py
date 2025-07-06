import streamlit as st
import pickle
import re
import nltk

nltk.download('punkt')
nltk.download('stopwords')


# loading models
clf=pickle.load(open('clf.pkl' , "rb"))
tfidf=pickle.load(open('tfidf.pkl', 'rb'))

# web app
st.title("Resume Screening App")