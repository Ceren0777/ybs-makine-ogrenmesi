import streamlit as st
import sys
import os

# src klasörünü yola ekle (Ayrı klasörde olduğu için)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from data_fetchers import get_survey_data

st.title("👨‍👩‍👧 Veli Algısı ve Risk Analizi")

# SİBER GÜVENLİK KASASI TESTİ
if "gsheets" in st.secrets.get("connections", {}):
    st.success("✅ SİSTEM RAPORU: Şifre Kasası (secrets.toml) başarıyla bulundu ve okunuyor!")
else:
    st.error("❌ SİSTEM RAPORU: Streamlit şifreleri GÖREMİYOR! (404 hatasının sebebi bu)")

# Sadece ID'yi değil, o temiz URL'nin tamamını veriyoruz:
VELI_SHEET_URL = "https://docs.google.com/spreadsheets/d/1vpm49xSGrP5Hbj8m8NWInhLFQ-JZA0OATmE7MTTaYd4"
# Veriyi çek (İlk seferde 1-2 saniye sürer, sonrakilerde 0.01 saniyede gelir)
df_veliler = get_survey_data(VELI_SHEET_URL)

if not df_veliler.empty:
    st.success(f"{len(df_veliler)} veli verisi canlı olarak başarıyla çekildi!")
    st.dataframe(df_veliler.head()) # Verinin ilk 5 satırını ekrana bas
else:
    st.warning("Henüz veri yok veya bağlantı kurulamadı.")
