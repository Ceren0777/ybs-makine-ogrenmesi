import streamlit as st
from utils import lokal_css_yukle, logo_koy

st.set_page_config(page_title="Veli Algısı", layout="wide")

# CSS ve Logo yükle
lokal_css_yukle()
logo_koy()

st.header("Veli Algısı")
