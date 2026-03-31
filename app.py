import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ren's Finance", layout="wide")

st.title("💰 Ren's Financial Tracker")

# Bagian Atas: Tombol Input
st.subheader("Tambah Pengeluaran")
link_form = "TEMPEL_LINK_GOOGLE_FORM_KAMU_DI_SINI"

st.markdown(f"""
<a href="{link_form}" target="_blank">
    <button style="
        background-color: #4CAF50;
        color: white;
        padding: 15px 32px;
        text-align: center;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
        border: none;
        width: 100%;">
        ➕ Klik di Sini untuk Catat Belanja
    </button>
</a>
""", unsafe_allow_all=True)

st.divider()

# Bagian Bawah: Tampilan Data dari Sheets
st.subheader("📊 Riwayat Pengeluaran (Real-time)")

# Ambil link Google Sheets yang sudah di-publish ke CSV
sheet_url = st.secrets["gsheets_url"].replace("/edit?usp=sharing", "/export?format=csv")

try:
    df = pd.read_csv(sheet_url)
    # Tampilkan 10 data terakhir
    st.dataframe(df.tail(10), use_container_width=True)
    
    # Total sederhana
    if not df.empty:
        total = df.iloc[:, -1].sum() # Asumsi nominal di kolom terakhir
        st.info(f"Estimasi Total Pengeluaran: **Rp{total:,}**")
except:
    st.warning("Belum bisa narik data. Pastikan link Google Sheets di Secrets sudah benar.")
