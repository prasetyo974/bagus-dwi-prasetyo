import streamlit as st

st.set_page_config(
    page_title="Prediksi Kelulusan",
    page_icon="🎓",
    layout="wide"
)

st.sidebar.title("📋 MENU")

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Home",
        "Prediksi Nilai",
        "Tentang",
        "Bantuan"
    ]
)

if menu == "Home":
    from pages.home import tampilkan
    tampilkan()

elif menu == "Prediksi Nilai":
    from pages.prediksi import tampilkan
    tampilkan()

elif menu == "Tentang":
    from pages.tentang import tampilkan
    tampilkan()

elif menu == "Bantuan":
    from pages.bantuan import tampilkan
    tampilkan()