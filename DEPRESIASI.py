import streamlit as st

def calculate_depreciation(initial_value, salvage_value, useful_life):
    depreciation = (initial_value - salvage_value) / useful_life
    return depreciation

# Tampilan Streamlit
st.title("Kalkulator Depresiasi")
st.markdown("Depresiasi merupakan penyusutan nilai investasi.")
st.markdown("Tujuan dilakukannya perhitungan depresiasi untuk meminimalisir kerugian perusahaan.")

# Input nilai awal, nilai sisa, dan umur manfaat
st.header("Perhitungan")
initial_value = st.number_input("Masukkan Nilai Investasi Aset (tanpa titik):", min_value=0.0, step=1.0)
salvage_value = st.number_input("Masukkan Nilai Sisa Aset (tanpa titik):", min_value=0.0, step=1.0)
useful_life = st.number_input("Masukkan Masa Pakai Aset (Tahun):", min_value=0, step=1)
umur_buku = st.number_input("Nilai Buku Tahun Ke-:", min_value=0, step=1)

# Tombol untuk menghitung depresiasi
if st.button("Hitung Nilai Depresiasi"):
    depreciation = calculate_depreciation(initial_value, salvage_value, useful_life)
    st.header("Besar Depresiasi/Tahun:")
    st.write(f"Besarnya penyusutan/tahun adalah {depreciation}")

#Nilai Buku
def calculate_nilai_buku(initial_value, salvage_value, useful_life, umur_buku):
    nilai_buku = initial_value-(((initial_value - salvage_value) / useful_life)*umur_buku)
    return nilai_buku

#Tomb0l untuk menghitung nilai buku
if st.button("Hitung Nilai Buku"):
    nilai_buku = calculate_nilai_buku(initial_value, salvage_value, useful_life, umur_buku)
    st.header("Nilai Buku:")
    st.write(f"Nilai buku tahun ke {umur_buku} adalah {nilai_buku}")
