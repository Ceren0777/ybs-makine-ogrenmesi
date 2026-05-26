import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

def get_survey_data(sheet_url):
    try:
        # secrets.toml dosyasını okuyup Cloud'a bağlanan satır
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        df = conn.read(spreadsheet=sheet_url, ttl=600)
        df = df.dropna(how="all")
        return df
    except Exception as e:
        st.error(f"Bağlantı hatası: {e}")
        return pd.DataFrame()