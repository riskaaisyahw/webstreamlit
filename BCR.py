import streamlit as st

def calculate_bcr(benefits, costs):
    bcr = benefits / costs
    return bcr

# Tampilan Streamlit
st.title("Kalkulator Benefit Cost Ratio (BCR)")
st.markdown ('BCR merupakan metode perhitungan dari perbandingan antara biaya produksi dengan keuntungan yang diterima dari sebuah proyek.')
st.markdown("Jika hasil perhitungan melebihi 1, maka proyek menguntungkan perusahaan. Namun, jika nilai BCR dibawah 1, maka proyek merugikan perusahaan")

# Input manfaat dan biaya
st.header("Perhitungan")
benefits = st.number_input("Masukkan Nilai Keuntungan/Pendapatan (tanpa titik):", min_value=0.0, step=1.0)
costs = st.number_input("Masukkan Nilai Biaya/Modal (tanpa titik):", min_value=0.0, step=1.0)

# Tombol untuk menghitung BCR
if st.button("Hitung Nilai BCR"):
    bcr = calculate_bcr(benefits, costs)
    st.header("Benefit Cost Ratio (BCR):")
    st.write(f"Nilai BCR yaitu sebesar {bcr}")
    if bcr>=1:
        st.write('Keputusan: Investasi/proyek menguntungkan perusahan')
    else:
        st.write('Keputusan: Investasi/proyek merugikan perusahaan')