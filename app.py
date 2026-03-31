import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

# Konfigurasi Tampilan
st.set_page_config(page_title="Ren's Finance", layout="wide")

st.title("💰 Ren's Financial Tracker")
st.write(f"Sesi Aktif: {datetime.now().strftime('%d %B %Y')}")

# Inisialisasi Koneksi ke Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Form Input
with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        item = st.text_input("Nama Barang/Kegiatan")
        kategori = st.selectbox("Kategori", ["Makan", "Transport", "Kebutuhan", "Hiburan", "Investasi"])
    with col2:
        harga = st.number_input("Nominal (Rp)", min_value=0, step=1000)
        tanggal = st.date_input("Tanggal Transaksi")
    
    submit = st.form_submit_button("Simpan ke Cloud")

if submit:
    if item and harga > 0:
        # Membuat baris data baru
        new_data = pd.DataFrame([{
            "Tanggal": tanggal.strftime("%Y-%m-%d"),
            "Nama Barang": item,
            "Kategori": kategori,
            "Nominal": harga
        }])
        
        # Ambil data lama & gabungkan
        existing_data = conn.read(spreadsheet=st.secrets["gsheets_url"])
        updated_df = pd.concat([existing_data, new_data], ignore_index=True)
        
        # Simpan kembali ke Google Sheets
        conn.update(spreadsheet=st.secrets["gsheets_url"], data=updated_df)
        st.success(f"Berhasil disimpan, Ren! Data '{item}' sudah masuk ke Sheets.")
    else:
        st.error("Isi nama barang dan nominal dulu ya.")

st.divider()
st.subheader("Riwayat Transaksi Terbaru")
# Menampilkan data dari Sheets secara Real-time
try:
    df = conn.read(spreadsheet=st.secrets["gsheets_url"])
    st.dataframe(df.tail(10), use_container_width=True)
except:
    st.info("Belum ada data yang tersimpan di Google Sheets.")

