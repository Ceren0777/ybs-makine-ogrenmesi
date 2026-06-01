import streamlit as st
from utils import lokal_css_yukle, logo_koy

st.set_page_config(page_title="ANIVIA Game Insight", layout="wide")

# CSS ve Logo yükle
lokal_css_yukle()
logo_koy()

st.markdown('<h1 class="main-title">ANIVIA GAME INSIGHT</h1>', unsafe_allow_html=True)
st.title("Game Regulation Analytics")
