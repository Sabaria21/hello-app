import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca dataset
@st.cache
def load_data():
    df = pd.read_csv("nama_file.csv")
    return df

# Mendefinisikan fungsi untuk membuat plot
def plot_data(df):
    # Menghitung rata-rata jumlah pengguna sepeda per bulan
    monthly_avg = df.groupby('mnth')['cnt'].mean()
    
    # Plotting
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker='o')
    plt.xlabel('Bulan')
    plt.ylabel('Rata-rata Pengguna Sepeda')
    plt.title('Rata-rata Pengguna Sepeda per Bulan')
    st.pyplot()

def main():
    # Judul dashboard
    st.title("Dashboard Penggunaan Sepeda")
    
    # Load data
    df = load_data()
    
    # Tampilkan data jika diinginkan
    if st.checkbox("Tampilkan Data"):
        st.write(df)
    
    # Tampilkan plot jika diinginkan
    if st.checkbox("Tampilkan Plot"):
        plot_data(df)

if __name__ == "__main__":
    main()
