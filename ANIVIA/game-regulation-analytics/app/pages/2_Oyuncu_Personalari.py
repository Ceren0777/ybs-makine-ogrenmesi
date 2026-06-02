import streamlit as st
import pandas as pd
import joblib
from utils import lokal_css_yukle, logo_koy
from pathlib import Path

st.set_page_config(page_title="Oyuncu Personaları", layout="wide")

# CSS ve Logo yükle
lokal_css_yukle()
logo_koy()

# CSS renkleri tanımla (CSS'ten uyumlu)
COLOR_LIGHT_BLUE = "#E0F2FE"      # Çok Açık Bebe Mavisi
COLOR_DARK_BLUE = "#1E3A8A"       # Koyu Mavi
COLOR_GOLD = "#D4AF37"             # Altın
COLOR_DARK_GOLD = "#B8860B"        # Koyu Altın
COLOR_VERY_LIGHT_BLUE = "#EBF3FA"  # Çok Açık Mavi
COLOR_TEXT_DARK = "#0a0f2c"        # Çok Koyu Mavi

# 1. Modeli ve Beklenen Sütunları Yükle
scaler = None
model_persona = None
beklenen_sutunlar = []

models_dir = Path(__file__).parent.parent.parent / "models"
model_path = models_dir / "anivia_persona_classification.pkl"
features_path = models_dir / "anivia_persona_features.pkl"

try:
    if model_path.exists():
        model_persona = joblib.load(model_path)
    if features_path.exists():
        beklenen_sutunlar = joblib.load(features_path)
except Exception as e:
    st.error(f"❌ Model veya özellik listesi yüklenemedi: {e}")

# Başlık - HTML ile stillendir
st.markdown(f"""
<div style="background-color: {COLOR_LIGHT_BLUE}; padding: 30px; border: 5px solid {COLOR_GOLD}; border-radius: 8px; box-shadow: 0 0 20px rgba(212, 175, 55, 0.5); margin-bottom: 25px; text-align: center;">
    <h1 style="color: {COLOR_DARK_BLUE}; font-size: 2.5em; margin: 0; text-shadow: 2px 2px 4px rgba(0,0,0,0.1);">👥 OYUNCU PERSONALARI 👥</h1>
    <p style="color: {COLOR_DARK_BLUE}; margin-top: 15px; font-size: 16px; font-weight: 600;">Makine Öğrenmesi Tabanlı Oyuncu Segmentasyonu ve Profilleri</p>
    <hr style="border: none; border-top: 2px solid {COLOR_GOLD}; margin: 20px 0;">
    <p style="color: {COLOR_DARK_BLUE}; font-size: 14px; line-height: 1.8; margin: 0;">
    📌 <strong>Bu dashboard</strong>, yapay zeka algoritmaları kullanarak oyuncu davranışlarını analiz eder; 
    oyuncu tercihlerini, yaş gruplarını ve oyun türü afiniteleri temel alarak farklı oyuncu personas oluşturur.
    </p>
</div>
""", unsafe_allow_html=True)

# Veriyi yükle
data_path = Path(__file__).parent.parent.parent / "data" / "processed" / "oyuncular_temiz.csv"

try:
    df_oyuncular = pd.read_csv(data_path)
except Exception as e:
    st.error(f"❌ Veri yükleme hatası: {e}")
    df_oyuncular = pd.DataFrame()

# Ana metrikler satırı
if not df_oyuncular.empty:
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        toplam_oyuncu = len(df_oyuncular)
        st.markdown(f"""
        <div style="background-color: {COLOR_LIGHT_BLUE}; padding: 30px 15px; border: 3px solid {COLOR_GOLD}; border-radius: 8px; text-align: center; box-shadow: 0 4px 8px rgba(212, 175, 55, 0.3); min-height: 180px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <h3 style="color: {COLOR_GOLD}; margin: 0 0 15px 0; font-size: 11px; font-weight: 900; letter-spacing: 1px;">TOPLAM OYUNCU</h3>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 40px; font-weight: bold; margin: 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">👤</p>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 32px; font-weight: bold; margin: 8px 0 0 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">{toplam_oyuncu}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        yaş_grupları = len(df_oyuncular['oyuncu_yas'].unique())
        st.markdown(f"""
        <div style="background-color: {COLOR_LIGHT_BLUE}; padding: 30px 15px; border: 3px solid {COLOR_GOLD}; border-radius: 8px; text-align: center; box-shadow: 0 4px 8px rgba(212, 175, 55, 0.3); min-height: 180px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <h3 style="color: {COLOR_GOLD}; margin: 0 0 15px 0; font-size: 11px; font-weight: 900; letter-spacing: 1px;">YAŞ GRUPLARI</h3>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 40px; font-weight: bold; margin: 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">🎂</p>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 32px; font-weight: bold; margin: 8px 0 0 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">{yaş_grupları}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        en_cok_oyun_count = df_oyuncular['oyuncu_oyun_turu'].value_counts().values[0] if 'oyuncu_oyun_turu' in df_oyuncular.columns else 0
        st.markdown(f"""
        <div style="background-color: {COLOR_LIGHT_BLUE}; padding: 30px 15px; border: 3px solid {COLOR_GOLD}; border-radius: 8px; text-align: center; box-shadow: 0 4px 8px rgba(212, 175, 55, 0.3); min-height: 180px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <h3 style="color: {COLOR_GOLD}; margin: 0 0 15px 0; font-size: 11px; font-weight: 900; letter-spacing: 1px;">EN ÇOK OYUN</h3>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 40px; font-weight: bold; margin: 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">🎮</p>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 32px; font-weight: bold; margin: 8px 0 0 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">{en_cok_oyun_count}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        mobil_count = len(df_oyuncular[df_oyuncular['oyuncu_cihaz'].str.contains('Mobil', na=False)]) if 'oyuncu_cihaz' in df_oyuncular.columns else 0
        st.markdown(f"""
        <div style="background-color: {COLOR_LIGHT_BLUE}; padding: 30px 15px; border: 3px solid {COLOR_GOLD}; border-radius: 8px; text-align: center; box-shadow: 0 4px 8px rgba(212, 175, 55, 0.3); min-height: 180px; display: flex; flex-direction: column; justify-content: center; align-items: center;">
            <h3 style="color: {COLOR_GOLD}; margin: 0 0 15px 0; font-size: 11px; font-weight: 900; letter-spacing: 1px;">FAVORİ CİHAZ</h3>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 40px; font-weight: bold; margin: 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">💻</p>
            <p style="color: {COLOR_DARK_BLUE}; font-size: 32px; font-weight: bold; margin: 8px 0 0 0; text-shadow: 1px 1px 2px rgba(0,0,0,0.1);">{mobil_count}</p>
        </div>
        """, unsafe_allow_html=True)

# =====================================================================
# YENİ EKLENEN BÖLÜM: PERSONA KİMLİK KARTLARI
# =====================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"""
<h3 style='text-align: center; color: {COLOR_DARK_BLUE}; border-bottom: 2px solid {COLOR_GOLD}; padding-bottom: 10px; margin-bottom: 20px;'>
    📑 ANIVIA PERSONA KATALOĞU
</h3>
""", unsafe_allow_html=True)

card_col1, card_col2, card_col3, card_col4 = st.columns(4)

kart_stili = f"""
    background-color: white; 
    border-top: 5px solid {COLOR_DARK_BLUE}; 
    border-radius: 8px; 
    padding: 20px; 
    box-shadow: 0 4px 8px rgba(0,0,0,0.1); 
    height: 380px;
"""

with card_col1:
    st.markdown(f"""
    <div style="{kart_stili}">
        <div style="text-align: center; font-size: 40px; margin-bottom: 10px;">👑</div>
        <h4 style="color: {COLOR_DARK_BLUE}; text-align: center; font-size: 16px; margin-bottom: 15px;">Koleksiyoner / Premium</h4>
        <p style="font-size: 13px; color: #555; text-align: justify;">Oyunu hırs için oynamayan ama cüzdanı açık olan kitledir. Başarıyı emekle değil, satın aldığı estetik/premium içeriklerle gösterirler.</p>
        <hr style="margin: 10px 0; opacity: 0.2;">
        <p style="font-size: 12px; color: #155724; background-color: #d4edda; padding: 8px; border-radius: 5px;"><b>Risk:</b> Düşük<br><b>Öneri:</b> Hesap çalınmasına karşı 2FA (İki Adımlı Doğrulama).</p>
    </div>
    """, unsafe_allow_html=True)

with card_col2:
    st.markdown(f"""
    <div style="{kart_stili}">
        <div style="text-align: center; font-size: 40px; margin-bottom: 10px;">🛡️</div>
        <h4 style="color: {COLOR_DARK_BLUE}; text-align: center; font-size: 16px; margin-bottom: 15px;">Odaklı / F2P Oyuncu</h4>
        <p style="font-size: 13px; color: #555; text-align: justify;">Oyuna ciddi zaman ve emek harcayan ancak para harcamayı sevmeyen gruptur. Parayla gelişmek yerine oyun içi emekle (grind) ilerlerler.</p>
        <hr style="margin: 10px 0; opacity: 0.2;">
        <p style="font-size: 12px; color: #004085; background-color: #cce5ff; padding: 8px; border-radius: 5px;"><b>Risk:</b> Yok<br><b>Öneri:</b> En dengeli profildir. Müdahale edilmeden bırakılabilir.</p>
    </div>
    """, unsafe_allow_html=True)

with card_col3:
    st.markdown(f"""
    <div style="{kart_stili}">
        <div style="text-align: center; font-size: 40px; margin-bottom: 10px;">💸</div>
        <h4 style="color: {COLOR_DARK_BLUE}; text-align: center; font-size: 16px; margin-bottom: 15px;">Dürtüsel / Pay-to-Win</h4>
        <p style="font-size: 13px; color: #555; text-align: justify;">Oynamaya veya emek vermeye niyeti olmayan, "parayı basıp kazanmak" isteyen kitle. Loot box (şans kutusu) mekaniklerine zaafları vardır.</p>
        <hr style="margin: 10px 0; opacity: 0.2;">
        <p style="font-size: 12px; color: #856404; background-color: #fff3cd; padding: 8px; border-radius: 5px;"><b>Risk:</b> Yüksek (Finansal)<br><b>Öneri:</b> Ebeveyn denetimi ve kesin harcama limiti şarttır.</p>
    </div>
    """, unsafe_allow_html=True)

with card_col4:
    st.markdown(f"""
    <div style="{kart_stili}">
        <div style="text-align: center; font-size: 40px; margin-bottom: 10px;">⚔️</div>
        <h4 style="color: {COLOR_DARK_BLUE}; text-align: center; font-size: 16px; margin-bottom: 15px;">Toksik / Rekabetçi</h4>
        <p style="font-size: 13px; color: #555; text-align: justify;">Kazanmaya, lig atlamaya ve rakiplerini ezmeye odaklıdırlar. Para harcamazlar ama kazanma hırsları agresif davranışlara yol açar.</p>
        <hr style="margin: 10px 0; opacity: 0.2;">
        <p style="font-size: 12px; color: #721c24; background-color: #f8d7da; padding: 8px; border-radius: 5px;"><b>Risk:</b> Kritik (Psikolojik)<br><b>Öneri:</b> Sohbet filtreleri ve katı süre kısıtlamaları uygulanmalıdır.</p>
    </div>
    """, unsafe_allow_html=True)


# =====================================================================
# OYUNCU PERSONA TAHMİN FORMU
# =====================================================================
st.markdown("""
<div style="background-color: #E0F2FE; padding: 20px; border: 3px solid #D4AF37; border-radius: 8px; margin: 30px 0; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.4);">
    <h2 style="color: #1E3A8A; margin: 0; font-size: 24px; text-align: center; font-weight: 700;">🎯 OYUNCU PERSONA TAHMİN SİSTEMİ</h2>
    <p style="color: #1E3A8A; font-size: 13px; margin: 10px 0 0 0; text-align: center; font-weight: 600;">ÖZELLİKLERİNİ GİRİN VE AI TARAFINDAN OLUŞTURULACAK PERSONA PROFİLİ GÖREBİLİRSİNİZ</p>
</div>
""", unsafe_allow_html=True)

# Seçeneklerin Listeleri
yas_ops = ['18-22', '23-28', '29-35', '36-45', '46-55', '55+']
haftalik_ops = ['Hiçbir zaman', 'Nadiren (Ayda 1-2 kez)', 'Bazen (Haftada 1-2 kez)', 'Sıklıkla (Haftada 3-4 kez)', 'Neredeyse her gün / Her gün']
sure_ops = ['1 saatten az', '1-3 saat', '3-5 saat', '5 saatten fazla']
butce_ops = ['Hiç harcama yapmam', "250 TL'den az", '250 - 1000 TL arası', '1000 TL ve üzeri']
maglubiyet_ops = [
    'Sakince oyunu kapatır veya başka bir işe geçerim.', 
    'Biraz moralim bozulur ama oyuna ara veririm.', 
    'Sadece kaybımı telafi etmek için bir maç daha atar, sonra çıkarım.', 
    'Hırslanırım ve mutlaka kazanana kadar peş peşe yeni maçlara girmeye devam ederim.',
    'Sinirimden saatlerce bilgisayarın/telefonun başından kalkamam.'
]
uyku_ops = ['Hiçbir zaman', 'Nadiren (Ayda 1-2 kez)', 'Bazen (Ayda birkaç kez)', 'Sıklıkla (Haftada birkaç kez)', 'Neredeyse her gün']
ruh_hali_ops = [
    'Hiç etkilemez, anında unuturum.', 'Sadece anlık olarak canım sıkılır.', 
    'O günkü genel moralimi düşürür.', 'Çevreme karşı gergin ve tahammülsüz olurum.', 
    'Günlük hayatta öfke patlamaları yaşamama sebep olur.'
]
pegi_ops = ['Evet, her zaman', 'Bazen', 'Hayır, dikkat etmiyorum', 'PEGI nedir bilmiyorum']
platform_gorus_ops = ['Kesinlikle desteklemiyorum', 'Desteklemiyorum', 'Kararsızım', 'Destekliyorum', 'Kesinlikle destekliyorum']
ebeveyn_onay_ops = ['Kesinlikle desteklemiyorum', 'Desteklemiyorum', 'Kararsızım', 'Destekliyorum', 'Kesinlikle destekliyorum']

cinsiyet_ops = ['Erkek', 'Kadın']
oyun_turu_ops = [
    'Basit Eğlence / Bulmaca (Candy Crush, Kelime Oyunları, Subway Surfers vb.)',
    'Hayatta Kalma, İnşa Etme & Sandbox (Minecraft, The FOREST, Rust, Subnautica vb.)',
    'Hikaye Odaklı & Rol Yapma - RPG (The Witcher, Cyberpunk, Genshin Impact, Elden Ring, Red Dead Redemption 2 vb.)',
    'Rekabetçi Nişancı & Battle Royale (Valorant, CS2, PUBG Mobile, Apex Legends vb.)',
    'Spor & Yarış (FIFA/FC, NBA 2K, F1, Rocket League vb.)',
    'Strateji & MOBA (League of Legends - LoL, Clash of Clans, Wild Rift vb.)'
]
cihaz_ops = [
    'Kişisel Bilgisayar (Masaüstü, Laptop - Steam, Epic Games vb.)',
    'Mobil Cihaz (Akıllı Telefon, Tablet)',
    'Oyun Konsolu (PlayStation, Xbox, Nintendo vb.)'
]
harcama_amaci_ops = [
    'Oyun içi harcama yapmam.',
    'Oyunda daha hızlı ilerlemek veya diğer oyunculardan güçlü olmak için.',
    'İçeriği belli olan, doğrudan istediğim bir eşyayı/kostümü satın almak için.',
    'İçinden ne çıkacağı belli olmayan, şansa dayalı sürpriz kutular/paketler veya kasalar açmak için (Örn: CS Kasası, FIFA Paketi, PUBG Sandığı).'
]
harcama_etkisi_ops = [
    'Hiç harcamam veya sınırlarımı asla aşmam.',
    'Bazen limitimi aşarım ama bütçemi sarsmaz.',
    'Bütçemi zorlar, diğer ihtiyaçlarımdan kısmam gerekir.',
    'Sonradan pişman olurum veya harcamalarımı çevremden gizlerim.'
]
motivasyon_ops = [
    'Sadece eğlenmek ve vakit geçirmek',
    'Sosyalleşmek ve arkadaşlarımla olmak',
    'Rekabet etmek ve başarmak hissiyatı',
    'Gerçek hayatın stresinden, sorunlarından uzaklaşmak (Kaçış)'
]
stres_etkisi_ops = [
    'Tamamen rahatlatır, stresimi alır.',
    'Oynadığım sürece rahatlarım, kafam dağıtır.',
    'Nötr (Oynamak veya oynamamak genel ruh halimi pek değiştirmez).',
    'Zorlu maçlarda veya rekabet gerektiren anlarda zaman zaman stres yaşadığım olur.',
    'Oynayamadığım zamanlarda çabuk canım sıkılır veya huzursuz/gergin hissederim, .'
]

# 2. st.form ile anketi tasarlıyoruz
with st.form("persona_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Bölüm 1: Genel Demografi")
        f_yas = st.selectbox("Yaş Grubunuz", yas_ops)
        f_cinsiyet = st.selectbox("Cinsiyetiniz", cinsiyet_ops)
        f_cihaz = st.selectbox("En Çok Oynadığınız Cihaz", cihaz_ops)
        f_oyun_turu = st.selectbox("Favori Oyun Türünüz", oyun_turu_ops)
        
        st.subheader("Bölüm 2: Oyun Alışkanlıkları")
        f_haftalik = st.selectbox("Haftalık Oyun Sıklığınız", haftalik_ops)
        f_sure = st.selectbox("Günlük Ortalama Oyun Süreniz", sure_ops)
        f_uyku = st.selectbox("Oyun İçin Uykunuzdan Feragat Eder misiniz?", uyku_ops)
        f_motivasyon = st.selectbox("Oyundaki Temel Motivasyonunuz", motivasyon_ops)
        f_pegi = st.selectbox("Oyun Seçerken Yaş Sınırlarına (PEGI) Dikkat Eder misiniz?", pegi_ops)

    with col2:
        st.subheader("Bölüm 3: Harcama ve Etkileri")
        f_butce = st.selectbox("Aylık Ortalama Oyun İçi Harcamanız", butce_ops)
        f_harcama_amaci = st.selectbox("Harcama Yapmaktaki Temel Amacınız", harcama_amaci_ops)
        f_harcama_etkisi = st.selectbox("Yaptığınız Harcamaların Bütçenize Etkisi", harcama_etkisi_ops)
        
        st.subheader("Bölüm 4: Psikolojik Deneyim")
        f_maglubiyet = st.selectbox("Üst Üste Mağlubiyet Aldığınızda Tepkiniz", maglubiyet_ops)
        f_stres = st.selectbox("Oyunun Stres Seviyenize Etkisi", stres_etkisi_ops)
        f_ruh_hali = st.selectbox("Oyun İçi Olayların Gerçek Hayattaki Ruh Halinize Etkisi", ruh_hali_ops)
        
        st.subheader("Bölüm 5: Yönetim / Katılım")
        f_platform = st.selectbox("Devlet Tarafından Zararlı Görülen Oyunların Yasaklanması", platform_gorus_ops)
        f_ebeveyn = st.selectbox("Aile Onay Sistemi (E-Devlet Entegrasyonu vs.) Hakkındaki Görüşünüz", ebeveyn_onay_ops)
        
    st.markdown("<br>", unsafe_allow_html=True)
    tahmin_buton = st.form_submit_button("🔮 PERSONA PROFİLİ OLUŞTUR", use_container_width=True)
if tahmin_buton:
    # ===================================================================
    # 1. ORDİNAL (SAYISAL) DEĞİŞKENLER İÇİN HARİTA
    # ===================================================================
    sozluk_haritasi = {
        'oyuncu_yas': {'18-22': 0, '23-28': 1, '29-35': 2, '36-45': 3, '46-55': 4, '55+': 5},
        'oyuncu_haftalik_oyun_gunu': {'Hiçbir zaman': 0, 'Nadiren (Ayda 1-2 kez)': 1, 'Bazen (Haftada 1-2 kez)': 2, 'Sıklıkla (Haftada 3-4 kez)': 3, 'Neredeyse her gün / Her gün': 4},
        'oyuncu_gunluk_sure': {'1 saatten az': 0, '1-3 saat': 1, '3-5 saat': 2, '5 saatten fazla': 3},
        'oyuncu_harcama_butcesi': {'Hiç harcama yapmam': 0, "250 TL'den az": 1, '250 - 1000 TL arası': 2, '1000 TL ve üzeri': 3},
        'oyuncu_maglubiyet_tepkisi': {'Sakince oyunu kapatır veya başka bir işe geçerim.': 0, 'Biraz moralim bozulur ama oyuna ara veririm.': 1, 'Sadece kaybımı telafi etmek için bir maç daha atar, sonra çıkarım.': 2, 'Hırslanırım ve mutlaka kazanana kadar peş peşe yeni maçlara girmeye devam ederim.': 3, 'Sinirimden saatlerce bilgisayarın/telefonun başından kalkamam.': 4},
        'oyuncu_uyku_feragati': {'Hiçbir zaman': 0, 'Nadiren (Ayda 1-2 kez)': 1, 'Bazen (Ayda birkaç kez)': 2, 'Sıklıkla (Haftada birkaç kez)': 3, 'Neredeyse her gün': 4},
        'oyuncu_ruh_hali': {'Hiç etkilemez, anında unuturum.': 0, 'Sadece anlık olarak canım sıkılır.': 1, 'O günkü genel moralimi düşürür.': 2, 'Çevreme karşı gergin ve tahammülsüz olurum.': 3, 'Günlük hayatta öfke patlamaları yaşamama sebep olur.': 4},
        'oyuncu_pegi_dikkat': {'Evet, her zaman': 0, 'Bazen': 1, 'Hayır, dikkat etmiyorum': 2, 'PEGI nedir bilmiyorum': 3},
        'oyuncu_platform_kisitlama_gorus': {'Kesinlikle desteklemiyorum': 4, 'Desteklemiyorum': 3, 'Kararsızım': 2, 'Destekliyorum': 1, 'Kesinlikle destekliyorum': 0},
        'oyuncu_ebeveyn_onay_gorus': {'Kesinlikle desteklemiyorum': 4, 'Desteklemiyorum': 3, 'Kararsızım': 2, 'Destekliyorum': 1, 'Kesinlikle destekliyorum': 0}
    }

    # ===================================================================
    # 2. KATEGORİK DEĞİŞKENLER İÇİN İSİM HARİTASI (Jupyter Eğitimiyle Aynı)
    # ===================================================================
    yeni_isim_haritasi = {
        'oyuncu_harcama_etkisi_Bazen limitimi aşarım ama bütçemi sarsmaz.': 'oyuncu_harcama_etkisi_limit_asar_sarsmaz',
        'oyuncu_harcama_etkisi_Bütçemi zorlar, diğer ihtiyaçlarımdan kısmam gerekir.': 'oyuncu_harcama_etkisi_butce_zorlar',
        'oyuncu_harcama_etkisi_Hiç harcamam veya sınırlarımı asla aşmam.': 'oyuncu_harcama_etkisi_hic_harcamaz',
        'oyuncu_harcama_etkisi_Sonradan pişman olurum veya harcamalarımı çevremden gizlerim.': 'oyuncu_harcama_etkisi_pisman_gizler',
        'oyuncu_stres_etkisi_Nötr (Oynamak veya oynamamak genel ruh halimi pek değiştirmez).': 'oyuncu_stres_etkisi_notr',
        'oyuncu_stres_etkisi_Oynadığım sürece rahatlarım, kafam dağıtır.': 'oyuncu_stres_etkisi_rahatlatir',
        'oyuncu_stres_etkisi_Oynayamadığım zamanlarda çabuk canım sıkılır veya huzursuz/gergin hissederim, .': 'oyuncu_stres_etkisi_oynamazsa_gergin',
        'oyuncu_stres_etkisi_Tamamen rahatlatır, stresimi alır.': 'oyuncu_stres_etkisi_tam_rahatlatir',
        'oyuncu_stres_etkisi_Zorlu maçlarda veya rekabet gerektiren anlarda zaman zaman stres yaşadığım olur.': 'oyuncu_stres_etkisi_rekabet_stresi',
        'oyuncu_harcama_amaci_Oyun içi harcama yapmam.': 'oyuncu_harcama_amaci_yapmaz',
        'oyuncu_harcama_amaci_Oyunda daha hızlı ilerlemek veya diğer oyunculardan güçlü olmak için.': 'oyuncu_harcama_amaci_hizli_ilerleme_guc',
        'oyuncu_harcama_amaci_İçeriği belli olan, doğrudan istediğim bir eşyayı/kostümü satın almak için.': 'oyuncu_harcama_amaci_dogrudan_esya',
        'oyuncu_harcama_amaci_İçinden ne çıkacağı belli olmayan, şansa dayalı sürpriz kutular/paketler veya kasalar açmak için (Örn: CS Kasası, FIFA Paketi, PUBG Sandığı).': 'oyuncu_harcama_amaci_sansa_dayali_kutu',
        'oyuncu_motivasyon_Gerçek hayatın stresinden, sorunlarından uzaklaşmak (Kaçış)': 'oyuncu_motivasyon_kacis',
        'oyuncu_motivasyon_Rekabet etmek ve başarmak hissiyatı': 'oyuncu_motivasyon_rekabet',
        'oyuncu_motivasyon_Sadece eğlenmek ve vakit geçirmek': 'oyuncu_motivasyon_eglence',
        'oyuncu_motivasyon_Sosyalleşmek ve arkadaşlarımla olmak': 'oyuncu_motivasyon_sosyallesme',
        'oyuncu_oyun_turu_Basit Eğlence / Bulmaca (Candy Crush, Kelime Oyunları, Subway Surfers vb.)': 'oyuncu_oyun_turu_basit_eglence',
        'oyuncu_oyun_turu_Hayatta Kalma, İnşa Etme & Sandbox (Minecraft, The FOREST, Rust, Subnautica vb.)': 'oyuncu_oyun_turu_hayatta_kalma',
        'oyuncu_oyun_turu_Hikaye Odaklı & Rol Yapma - RPG (The Witcher, Cyberpunk, Genshin Impact, Elden Ring, Red Dead Redemption 2 vb.)': 'oyuncu_oyun_turu_hikaye_rpg',
        'oyuncu_oyun_turu_Rekabetçi Nişancı & Battle Royale (Valorant, CS2, PUBG Mobile, Apex Legends vb.)': 'oyuncu_oyun_turu_rekabetci_nisanci',
        'oyuncu_oyun_turu_Spor & Yarış (FIFA/FC, NBA 2K, F1, Rocket League vb.)': 'oyuncu_oyun_turu_spor_yaris',
        'oyuncu_oyun_turu_Strateji & MOBA (League of Legends - LoL, Clash of Clans, Wild Rift vb.)': 'oyuncu_oyun_turu_strateji_moba',
        'oyuncu_cihaz_Kişisel Bilgisayar (Masaüstü, Laptop - Steam, Epic Games vb.)': 'oyuncu_cihaz_pc',
        'oyuncu_cihaz_Mobil Cihaz (Akıllı Telefon, Tablet)': 'oyuncu_cihaz_mobil',
        'oyuncu_cihaz_Oyun Konsolu (PlayStation, Xbox, Nintendo vb.)': 'oyuncu_cihaz_konsol'
    }

    # ===================================================================
    # 3. KUSURSUZ EŞLEŞTİRME MOTORU
    # ===================================================================
    input_dict = {
        'oyuncu_yas': sozluk_haritasi['oyuncu_yas'].get(f_yas, 0),
        'oyuncu_cinsiyet': f_cinsiyet,
        'oyuncu_haftalik_oyun_gunu': sozluk_haritasi['oyuncu_haftalik_oyun_gunu'].get(f_haftalik, 0),
        'oyuncu_gunluk_sure': sozluk_haritasi['oyuncu_gunluk_sure'].get(f_sure, 0),
        'oyuncu_oyun_turu': f_oyun_turu,
        'oyuncu_cihaz': f_cihaz,
        'oyuncu_harcama_butcesi': sozluk_haritasi['oyuncu_harcama_butcesi'].get(f_butce, 0),
        'oyuncu_harcama_amaci': f_harcama_amaci,
        'oyuncu_harcama_etkisi': f_harcama_etkisi,
        'oyuncu_motivasyon': f_motivasyon,
        'oyuncu_maglubiyet_tepkisi': sozluk_haritasi['oyuncu_maglubiyet_tepkisi'].get(f_maglubiyet, 0),
        'oyuncu_stres_etkisi': f_stres,
        'oyuncu_uyku_feragati': sozluk_haritasi['oyuncu_uyku_feragati'].get(f_uyku, 0),
        'oyuncu_ruh_hali': sozluk_haritasi['oyuncu_ruh_hali'].get(f_ruh_hali, 0),
        'oyuncu_pegi_dikkat': sozluk_haritasi['oyuncu_pegi_dikkat'].get(f_pegi, 0),
        'oyuncu_platform_kisitlama_gorus': sozluk_haritasi['oyuncu_platform_kisitlama_gorus'].get(f_platform, 0),
        'oyuncu_ebeveyn_onay_gorus': sozluk_haritasi['oyuncu_ebeveyn_onay_gorus'].get(f_ebeveyn, 0)
    }

    if len(beklenen_sutunlar) == 0:
        st.error("❌ Model sütun listesi bulunamadı! Lütfen özellikleri 'pkl' olarak kaydedin.")
    else:
        # Tüm sütunları 0 olan temiz şablon oluştur
        df_final = pd.DataFrame(0, index=[0], columns=beklenen_sutunlar)

        # Aktifleştirme (1 Basma veya Sayı Ekleme)
        for anket_sorusu, verilen_cevap in input_dict.items():
            if isinstance(verilen_cevap, str):
                # Metin cevap ise (örn: Cinsiyet_Erkek), One-Hot kolon ismini bul
                ham_sutun_adi = f"{anket_sorusu}_{verilen_cevap}"
                dogru_sutun_adi = yeni_isim_haritasi.get(ham_sutun_adi, ham_sutun_adi)
                
                # Eğer kolon drop_first ile silinmediyse ve modelde varsa 1 yap
                if dogru_sutun_adi in df_final.columns:
                    df_final.at[0, dogru_sutun_adi] = 1
            else:
                # Sayısal cevap ise direkt ilgili kolona yaz (örn: oyuncu_yas = 2)
                if anket_sorusu in df_final.columns:
                    df_final.at[0, anket_sorusu] = verilen_cevap

        try:
            if model_persona is not None:
                tahmin = model_persona.predict(df_final)[0]
                
                sonuc_sozluk = {
                    1: {'isim': 'Koleksiyoner / Premium Oyuncu', 'oneri': 'Çözüm Önerisi: 2FA kullanın, risk düşük', 'renk': '#D4EDDA', 'metin_renk': '#155724'},
                    2: {'isim': 'Odaklı / F2P Oyuncu', 'oneri': 'Çözüm Önerisi: En dengeli profil, müdahale gerektirmez', 'renk': '#CCE5FF', 'metin_renk': '#004085'},
                    3: {'isim': 'Dürtüsel / Pay-to-Win Oyuncu', 'oneri': 'Çözüm Önerisi: Finansal risk yüksek, harcama limiti şart', 'renk': '#FFF3CD', 'metin_renk': '#856404'},
                    4: {'isim': 'Toksik / Rekabetçi Oyuncu', 'oneri': 'Çözüm Önerisi: Psikolojik risk yüksek, sohbet filtresi ve süre kısıtlaması şart', 'renk': '#F8D7DA', 'metin_renk': '#721C24'}
                }
                
                profil = sonuc_sozluk.get(tahmin, {'isim': 'Bilinmeyen Profil', 'oneri': 'Analiz yapılamadı.', 'renk': '#E2E3E5', 'metin_renk': '#383D41'})
                
                st.markdown(f"""
                <div style="background-color: {profil['renk']}; padding: 30px; border-radius: 10px; margin-top: 30px; text-align: center; border: 2px solid {profil['metin_renk']};">
                    <h2 style="color: {profil['metin_renk']}; margin-top: 0; font-size: 28px;">🎯 {profil['isim']}</h2>
                    <hr style="border-top: 1px solid {profil['metin_renk']}; opacity: 0.3; margin: 15px 0;">
                    <p style="color: {profil['metin_renk']}; font-size: 18px; font-weight: bold; margin-bottom: 0;">
                        🛡️ {profil['oneri']}
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
            else:
                st.error("Model yüklü değil.")
        except Exception as e:
            st.error(f"Tahmin işlemi sırasında hata oluştu: {e}")