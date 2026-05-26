# Game Regulation Analytics

Bu proje oyun analitiği ve risk değerlendirmesi üzerine odaklanmaktadır.

## Proje Klasör Yapısı

```text
game-regulation-analytics/
│
├── data/
│   ├── raw/                    # Web scraping ve anketlerden gelen ilk dokunulmamış veriler
│   ├── interim/                # NaN değerleri uçurulmuş, okunabilir temiz veriler (Sweetviz için)
│   └── processed/              # Sadece algoritmalar için matematiksel matrisler (ML için)
│
├── notebooks/                  
│   ├── 01_steam_tabular_cleaning.ipynb  # Fiyat, tür, yaş sınırı gibi sayısal/kategorik verilerin temizliği
│   ├── 02_survey_preprocessing.ipynb    # Anket eksik veri ve ordinal ölçek analizleri
│   ├── 03_eda_sweetviz.ipynb            # A/B çarpıştırması
│   └── 04_ml_models.ipynb               # Sınıflandırma ve regresyon modellerinin eğitilmesi (Scikit-learn)
│
├── src/                        # Arka Plan Modülleri (Sadece Tabular İşlemler)
│   ├── __init__.py
│   ├── scraping_utils.py       # Web scraping fonksiyonları 
│   ├── feature_engineering.py  # Yeni sütunlar oluşturma, kategorik değişkenleri (OHE) dönüştürme
│   └── model_utils.py          # Model performansı ölçme (Accuracy, MSE, RMSE) fonksiyonları
│
├── models/                     
│   ├── game_risk_classifier.pkl  # Sayısal/kategorik özelliklere dayalı risk sınıflandırma modeli
│   └── player_clusters.pkl       # K-Means kümeleme modeli
│
├── app/                        
│   ├── app.py                  
│   └── pages/
│       ├── 1_Oyun_Risk_Radari.py     
│       ├── 2_Oyuncu_Personalari.py   
│       └── 3_Veli_Algisi.py         
│
├── requirements.txt            # NLP kütüphaneleri yok (Sadece pandas, scikit-learn, streamlit vb.)
└── README.md 
```
