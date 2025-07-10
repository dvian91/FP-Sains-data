import streamlit as st
import numpy as np
import pickle

analisis_model = pickle.load(open('model_prediksi.sav', 'rb'))
scaler = pickle.load(open('scaler_prediksi.sav', 'rb'))

st.set_page_config(page_title="Deteksi Penyakit Jantung", layout="centered")

st.title("💓 Deteksi Penyakit Jantung")
st.markdown("Masukkan data pasien berikut untuk mengetahui apakah memiliki risiko penyakit jantung.")

# Input data pasien
age = st.slider("Usia", 20, 100, 50)
sex = st.selectbox("Jenis Kelamin", ("Pria", "Wanita"))
cp = st.selectbox("Tipe Nyeri Dada", [0, 1, 2, 3])
trestbps = st.slider("Tekanan Darah Istirahat (mm Hg)", 80, 200, 120)
chol = st.slider("Kolesterol (mg/dl)", 100, 400, 200)
fbs = st.selectbox("Gula Darah > 120 mg/dl", ("Ya", "Tidak"))
restecg = st.selectbox("Hasil EKG", [0, 1, 2])
thalach = st.slider("Detak Jantung Maksimum", 60, 250, 150)
exang = st.selectbox("Angina karena Olahraga", ("Ya", "Tidak"))
oldpeak = st.slider("Oldpeak (depresi ST)", 0.0, 6.0, 1.0, step=0.1)
slope = st.selectbox("Slope Segmen ST", [0, 1, 2])
ca = st.selectbox("Jumlah Pembuluh yang Diberi Warna", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [0, 1, 2, 3])

input_data = np.array([[ 
    age,
    1 if sex == "Pria" else 0,
    cp,
    trestbps,
    chol,
    1 if fbs == "Ya" else 0,
    restecg,
    thalach,
    1 if exang == "Ya" else 0,
    oldpeak,
    slope,
    ca,
    thal
]])

scaled_input = scaler.transform(input_data)

if st.button("Prediksi"):
    prediction = analisis_model.predict(scaled_input)[0]
    probability = analisis_model.predict_proba(scaled_input)[0][1] * 100

    if prediction == 1:
        st.error(f"⚠ Pasien berisiko mengalami penyakit jantung.\n\nRisiko sebesar *{probability:.2f}%*.")
    else:
        st.success(f"✅ Pasien kemungkinan tidak mengalami penyakit jantung.\n\nRisiko sebesar *{probability:.2f}%*.")

st.markdown("---")
st.caption("Model ini digunakan untuk tujuan edukasi dan bukan sebagai pengganti diagnosis medis.")
