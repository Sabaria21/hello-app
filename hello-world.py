import streamlit as st
import matplotlib.pyplot as plt

# Judul dashboard
st.title('Dashboard')

# Teks
st.header('Bike')

# Sidebar
st.sidebar.header('Sidebar')

# Menginisiasi data
categories = ['Casual', 'Registered']
avg_counts = [avg_casual, avg_registered]

# Pembuatan plot
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(categories, avg_counts, color=['blue', 'green'])
ax.set_xlabel('Kategori Pengguna Sepeda')
ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
ax.set_title('Rata-rata Jumlah Pengguna Sepeda Acak dan Terdaftar')
ax.grid(axis='y')

# Menampilkan plot di Streamlit
st.pyplot(fig)

