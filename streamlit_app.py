import streamlit as st 

# Judul Aplikasi
st.title("Prediksi Potabilitas Air")

# Deskripsi Singkat
st.markdown("Aplikasi ini digunakan untuk memprediksi apakah air layak untuk diminum berdasarkan parameter kualitas air.")

# Input Parameter
st.subheader("Masukkan Parameter Air")
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, max_value=500.0, value=250.0, step=1.0)
conductivity = st.number_input("Conductivity (µS/cm)", min_value=0.0, max_value=1000.0, value=400.0, step=1.0)
organic_carbon = st.number_input("Organic Carbon (mg/L)", min_value=0.0, max_value=50.0, value=10.0, step=0.1)
trihalomethanes = st.number_input("Trihalomethanes (µg/L)", min_value=0.0, max_value=200.0, value=50.0, step=0.1)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, max_value=10.0, value=5.0, step=0.1)

# Tombol Prediksi
if st.button("Prediksi Potabilitas Air"):
    # Logika Prediksi Sederhana (Placeholder)
    # Anda dapat mengganti dengan model machine learning jika ada
    if 6.5 <= ph <= 8.5 and sulfate <= 250 and conductivity <= 500 and organic_carbon <= 20 and trihalomethanes <= 100 and turbidity <= 5:
        hasil = "Air LAYAK untuk diminum"
        warna = "success"
        ikon = "💧"
    else:
        hasil = "Air TIDAK LAYAK untuk diminum"
        warna = "error"
        ikon = "⚠"

    # Menampilkan Hasil Prediksi
    st.subheader("Hasil Prediksi")
    if warna == "success":
        st.success(f"{ikon} {hasil}")
    else:
        st.error(f"{ikon} {hasil}")

