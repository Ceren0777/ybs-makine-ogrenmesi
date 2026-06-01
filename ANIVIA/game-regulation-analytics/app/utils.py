import streamlit as st
from pathlib import Path
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def lokal_css_yukle():
    # Path(__file__).parent ile her zaman 'app' klasörünün yolunu bulur
    # Böylece pages içinden çağrılsa bile dosya yolunu şaşırmaz
    css_yolu = Path(__file__).parent / "assets" / "style.css"
    
    if css_yolu.exists():
        with open(css_yolu, "r", encoding="utf-8") as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def logo_koy(genislik=200):
    logo_yolu = Path(__file__).parent / "assets" / "logo.jpg"
    if logo_yolu.exists():
        st.sidebar.image(str(logo_yolu), width=genislik)
    else:
        # Logo dosyası henüz yoksa veya farklı bir isimdeyse alternatif
        pass
