# Dibuat oleh :
- Dede Khairunnisa IF22E 2241620101250
- Dhiva Jivianikmah IF22B 22416255201056

# Deteksi penyakit
## Tujuan Analisis
Membangun sebuah sistem prediksi yang dapat membantu dalam mendeteksi risiko penyakit jantung berdasarkan data klinis pasien. Dengan memanfaatkan algoritma machine learning, sistem ini diharapkan mampu mengidentifikasi pola dan faktor-faktor penting yang memengaruhi kemungkinan seseorang mengalami penyakit jantung, seperti tekanan darah, kadar kolesterol, usia, dan detak jantung maksimum. Selain itu, analisis ini bertujuan untuk menghasilkan model klasifikasi yang akurat dan dapat diandalkan, serta dievaluasi melalui metrik performa seperti akurasi, precision, recall, dan F1-score. Hasil dari analisis ini kemudian diterapkan ke dalam aplikasi berbasis web menggunakan Streamlit, sehingga pengguna dapat memanfaatkan prediksi secara interaktif dan mudah diakses. Secara keseluruhan, tujuan akhir dari proyek ini adalah untuk membantu proses deteksi dini penyakit jantung secara lebih efisien, serta memberikan dukungan pengambilan keputusan awal dalam dunia medis.

# Deksripsi Data
Dataset ini terdiri dari:
age: usia

sex: jenis kelamin

cp: tipe nyeri dada

trestbps: tekanan darah saat istirahat
chol: kadar kolesterol
fbs: gula darah puasa
restecg: hasil EKG saat istirahat
thalach: detak jantung maksimum
exang: angina karena olahraga
oldpeak: depresi segmen ST
slope: kemiringan segmen ST
ca: jumlah pembuluh darah utama
thal: kondisi thalassemia
condition: kondisi jantung (sakit/tidak)

# Modeling
Dalam proyek ini, kami memilih Support Vector Machine (SVM) sebagai algoritma utama karena algoritma ini sangat cocok untuk permasalahan klasifikasi biner seperti deteksi penyakit jantung. Variabel target dalam dataset adalah kondisi jantung pasien, yang terdiri dari dua kelas: mengalami penyakit jantung atau tidak mengalami penyakit jantung. SVM bekerja dengan mencari hyperplane terbaik yang memisahkan kedua kelas tersebut secara optimal berdasarkan data medis pasien. Dengan kemampuan SVM untuk menangani data berdimensi tinggi dan memaksimalkan margin antar kelas, algoritma ini diharapkan mampu memberikan hasil prediksi yang akurat dan andal dalam mendeteksi risiko penyakit jantung sejak dini.

