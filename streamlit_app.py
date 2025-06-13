
import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk
import os
print("Current working directory:", os.getcwd())

# Judul
st.title("Dashboard Determinan Stunting Kecamatan Bogor Selatan")

# Muat data
url = 'https://raw.githubusercontent.com/awanimbus/blank-app/refs/heads/main/Cleaning2.csv'
data = pd.read_csv(url,index_col=0)

# Sidebar: Pilihan variabel
variable = st.sidebar.selectbox(
    "Pilih Faktor Determinan",
    ["Air Bersih", "Riwayat Ibu Hamil", "Imunisasi", "Jamban Sehat", 
     "BPJS/JKN", "Merokok Keluarga", "Penyakit Penyerta", "Kecacingan"]
)

# Tampilkan peta
st.subheader("Peta Tematik Prevalensi Stunting")
midpoint = (data['latitude'].mean(), data['longitude'].mean())
st.map(data[['latitude', 'longitude', 'prevalensi_stunting']])

# Grafik korelasi
st.subheader(f"Korelasi antara {variable} dan Stunting")
chart = alt.Chart(data).mark_circle(size=60).encode(
    x=alt.X(variable), 
    y='prevalensi_stunting',
    tooltip=['kelurahan', variable, 'prevalensi_stunting']
).interactive()
st.altair_chart(chart, use_container_width=True)

# Heatmap korelasi
st.subheader("Heatmap Korelasi Semua Faktor")
corr = data.drop(columns=['kelurahan','latitude','longitude']).corr()
st.write(corr)
