import streamlit as st
import pandas as pd

st.set_page_config(page_title="Financial Tracker", layout="wide")

st.title("💰 Kayoubi's Financial Tracker")
st.write("Catat pengeluaran harianmu di sini.")

# Input Form
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        item = st.text_input("Nama Barang")
        kategori = st.selectbox("Kategori", ["Makan", "Transport", "Kebutuhan", "Hiburan"])
    with col2:
        harga = st.number_input("Nominal (Rp)", min_value=0, step=1000)
        tanggal = st.date_input("Tanggal")
    
    submit = st.form_submit_button("Simpan Transaksi")

if submit:
    st.success(f"Berhasil dicatat: {item} - Rp{harga:,}")

st.divider()
st.subheader("Ringkasan")
st.info("Data ini akan masuk ke Google Sheets setelah kita hubungkan nanti.")

