import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Prediksi Nilai Kelulusan",
    page_icon="🎓",
    layout="centered"
)

# Sidebar
st.sidebar.title("🎓 MENU")
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "🏠 Home",
        "📝 Prediksi Nilai",
        "ℹ Tentang",
        "❓ Bantuan"
    ]
)

# ================= HOME =================
if menu == "🏠 Home":

    st.title("🎓 Aplikasi Prediksi Nilai Kelulusan")

    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=180
    )

    st.markdown("---")

    st.subheader("Selamat Datang")

    st.write("""
    Aplikasi ini digunakan untuk menghitung nilai akhir mahasiswa
    berdasarkan nilai Tugas, UTS, dan UAS, kemudian menentukan
    grade serta status kelulusannya.
    """)

    st.info("Silakan pilih menu **Prediksi Nilai** pada sidebar.")

# ================= PREDIKSI =================
elif menu == "📝 Prediksi Nilai":

    st.title("📝 Prediksi Nilai Kelulusan")

    nama = st.text_input("Nama Mahasiswa")
    nim = st.text_input("NIM")

    tugas = st.number_input(
        "Nilai Tugas",
        min_value=0,
        max_value=100,
        value=0
    )

    uts = st.number_input(
        "Nilai UTS",
        min_value=0,
        max_value=100,
        value=0
    )

    uas = st.number_input(
        "Nilai UAS",
        min_value=0,
        max_value=100,
        value=0
    )

    if st.button("Hitung Nilai"):

        nilai_akhir = (
            (tugas * 0.30) +
            (uts * 0.30) +
            (uas * 0.40)
        )

        # Menentukan grade
        if nilai_akhir >= 85:
            grade = "A"
        elif nilai_akhir >= 75:
            grade = "B"
        elif nilai_akhir >= 65:
            grade = "C"
        elif nilai_akhir >= 50:
            grade = "D"
        else:
            grade = "E"

        # Status kelulusan
        if nilai_akhir >= 70:
            status = "LULUS"
        else:
            status = "TIDAK LULUS"

        st.markdown("---")
        st.subheader("📋 Hasil Prediksi")

        st.write("**Nama** :", nama)
        st.write("**NIM** :", nim)
        st.write("**Nilai Akhir** :", round(nilai_akhir, 2))
        st.write("**Grade** :", grade)

        if status == "LULUS":
            st.success("🎉 Status : LULUS")
            st.balloons()
        else:
            st.error("❌ Status : TIDAK LULUS")

# ================= TENTANG =================
elif menu == "ℹ Tentang":

    st.title("ℹ Tentang Aplikasi")

    st.write("""
    **Nama Aplikasi :**
    Prediksi Nilai Kelulusan Mahasiswa

    **Bahasa Pemrograman :**
    Python

    **Framework :**
    Streamlit

    **Fungsi Aplikasi :**
    - Menghitung nilai akhir
    - Menentukan grade
    - Menentukan status kelulusan mahasiswa
    """)

# ================= BANTUAN =================
elif menu == "❓ Bantuan":

    st.title("❓ Bantuan")

    st.write("""
    ### Cara Menggunakan

    1. Pilih menu **Prediksi Nilai**.
    2. Masukkan Nama dan NIM.
    3. Masukkan nilai Tugas, UTS, dan UAS.
    4. Klik tombol **Hitung Nilai**.
    5. Hasil akan menampilkan:
       - Nilai Akhir
       - Grade
       - Status Kelulusan
    """)

    st.success("Selamat mencoba!")