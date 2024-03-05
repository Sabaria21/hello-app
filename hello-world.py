import streamlit as st

# Judul dashboard
st.title('Dashboard Sederhana')

# Teks
st.header('Header Dashboard')
st.write('Ini adalah dashboard sederhana menggunakan Streamlit.')

# Sidebar
st.sidebar.header('Sidebar')
st.sidebar.write('Ini adalah sidebar untuk memilih opsi.')

# Tombol
if st.button('Klik di sini'):
    st.write('Anda telah mengklik tombol.')

# Pilihan dari pengguna
option = st.selectbox('Pilih opsi:', ['A', 'B', 'C'])
st.write('Anda memilih:', option)

# Masukan dari pengguna
user_input = st.text_input('Masukkan teks:', 'Tulis sesuatu...')
st.write('Anda memasukkan:', user_input)
