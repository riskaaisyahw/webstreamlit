import streamlit as st

#BEP UNIT
def calculate_bep(fixed_costs, selling_price, variable_costs):
    bep_units = fixed_costs / (selling_price - variable_costs)
    return bep_units

# Tampilan Streamlit
st.title("Kalkulator Break Even Point (BEP)")
st.markdown("BEP adalah kondisi dimana perusahaan tidak mengalami kerugian maupun keuntungan.")

# Input biaya tetap, harga jual, dan biaya variabel
st.header("Perhitungan")
fixed_costs = st.number_input("Masukkan Biaya Tetap (tapa titik):", min_value=0., step=1.0)
selling_price = st.number_input("Masukkan Nilai Jual/Unit (tanpa titik):", min_value=0., step=1.0)
variable_costs = st.number_input("Masukkan Biaya Produksi/Unit (tanpa titik):", min_value=0., step=1.0)

# Tombol untuk menghitung BEP
if st.button("Hitung Nilai BEP  Unit"):
    bep_units = calculate_bep(fixed_costs, selling_price, variable_costs)
    st.header("Break-Even Point:")
    st.write(f"Perusahaan akan berada pada kondisi BEP setelah menjual {bep_units} unit")

#BEP UANG
def calculate_bep_uang(fixed_costs, selling_price, variable_costs):
    bep_uang = fixed_costs / (1 - (variable_costs / selling_price))
    return bep_uang

# Tombol untuk menghitung BEP dalam uang
if st.button("Hitung Nilai BEP Uang"):
    bep_uang = calculate_bep_uang(fixed_costs, selling_price, variable_costs)
    st.header("Break-Even Point:")
    st.write(f"Perusahaan akan berada pada kondisi BEP setelah mendapat Rp {bep_uang} dari hasil penjualan")


