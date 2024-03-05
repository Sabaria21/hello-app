import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca file CSV
@st.cache
def load_data():
    df = pd.read_csv("nama_file.csv")
    return df

def main():
    # Menampilkan judul
    st.title("Dashboard Penggunaan Sepeda")

    # Memuat data
    df = load_data()

    # Menampilkan data jika diinginkan
    if st.checkbox("Tampilkan Data"):
        st.write(df)

    # Menghitung rata-rata jumlah pengguna sepeda acak dan terdaftar
    avg_casual = df['casual'].mean()
    avg_registered = df['registered'].mean()

    # Pembuatan plot
    categories = ['Casual', 'Registered']
    avg_counts = [avg_casual, avg_registered]

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(categories, avg_counts, color=['blue', 'green'])
    ax.set_xlabel('Kategori Pengguna Sepeda')
    ax.set_ylabel('Rata-rata Jumlah Pengguna Sepeda')
    ax.set_title('Rata-rata Jumlah Pengguna Sepeda Acak dan Terdaftar')
    ax.grid(axis='y')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
