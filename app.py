import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ren's Finance", layout="wide")

st.title("💰 Ren's Financial Tracker")

# Tab untuk navigasi biar rapi
tab1, tab2 = st.tabs(["➕ Catat Pengeluaran", "📊 Lihat Riwayat"])

with tab1:
    st.subheader("Input Data Baru")
    # Ganti link di bawah dengan Link Google Form Ren
    link_form = "https://docs.google.com/forms/d/e/1FAIpQLSdboIaKAdpS9wGckVb8KeEJctV2_-vDXwrBheQXLD3BBezxJw/viewform?usp=dialog"
    
    # Menampilkan Form di dalam website
    st.components.v1.iframe(link_form, height=600, scrolling=True)

with tab2:
    st.subheader("Data Real-time dari Sheets")
    # Ambil link Sheets dari Secrets
    try:
        sheet_url = st.secrets["gsheets_url"].replace("/edit?usp=sharing", "/export?format=csv")
        df = pd.read_csv(sheet_url)
        st.dataframe(df, use_container_width=True)
        
        # Hitung total kalau kolom terakhirnya angka
        total = df.iloc[:, -1].sum()
        st.success(f"Total Pengeluaran Tercatat: **Rp{total:,}**")
    except:
        st.info("Tabel akan muncul otomatis setelah Ren isi data pertama di Form.")
