import streamlit as st
import pandas as pd
from datetime import datetime

from style import load_css
from models import Mahasiswa, MahasiswaBeasiswa
from database import load_data, save_data
from utils import valid_nim, valid_nama, valid_email, predikat_ipk
from searching import linear_search, binary_search
from sorting import bubble_sort, merge_sort
from ui import show_sidebar, close_sidebar, menu_button, page_title, section_title, footer

st.set_page_config(
    page_title="Manajemen Data Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

load_css()

if "menu" not in st.session_state:
    st.session_state.menu = "Dashboard"

df = load_data()

col_menu, col_isi = st.columns([1.05, 4.25], gap="large")

with col_menu:
    show_sidebar()
    menu_button("🏠 Dashboard", "Dashboard")
    menu_button("➕ Tambah Data", "Tambah Data")
    menu_button("▣ Data Mahasiswa", "Tampilkan Data")
    menu_button("✎ Edit Data", "Edit Data")
    menu_button("🗑 Hapus Data", "Hapus Data")
    menu_button("🔍 Pencarian", "Pencarian")
    menu_button("↕ Pengurutan", "Pengurutan")
    menu_button("ⓘ Tentang Aplikasi", "Tentang Program")
    close_sidebar()

with col_isi:
    st.markdown('<div class="content-area">', unsafe_allow_html=True)

    menu = st.session_state.menu

    if menu == "Dashboard":
        page_title("📊", "Dashboard", "Ringkasan data mahasiswa secara keseluruhan")

        rata_ipk = round(pd.to_numeric(df["IPK"], errors="coerce").mean(), 2) if not df.empty else 0
        total_jurusan = df["Jurusan"].nunique() if not df.empty else 0

        st.markdown(
            f"""
            <div class="cards">
                <div class="card">
                    <div class="card-icon blue-bg">👥</div>
                    <div>
                        <div class="card-label">Total Mahasiswa</div>
                        <div class="card-value">{len(df)}</div>
                        <div class="card-small">Mahasiswa terdaftar</div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-icon green-bg">🏢</div>
                    <div>
                        <div class="card-label">Jumlah Jurusan</div>
                        <div class="card-value" style="color:#16a34a;">{total_jurusan}</div>
                        <div class="card-small">Jurusan tersedia</div>
                    </div>
                </div>
                <div class="card">
                    <div class="card-icon purple-bg">☆</div>
                    <div>
                        <div class="card-label">Rata-rata IPK</div>
                        <div class="card-value" style="color:#7e22ce;">{rata_ipk}</div>
                        <div class="card-small">Rata-rata IPK keseluruhan</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(f"📅 {datetime.now().strftime('%d-%m-%Y')} | 🕒 {datetime.now().strftime('%H:%M:%S')}")

        section_title("▤", "Data Terbaru", "Data mahasiswa yang tersimpan")

        if not df.empty:
            df_tampil = df.copy().reset_index(drop=True)
            df_tampil.index = df_tampil.index + 1
            df_tampil["Predikat IPK"] = df_tampil["IPK"].apply(predikat_ipk)
            st.dataframe(df_tampil, use_container_width=True, height=280)

            section_title("▦", "Grafik Jumlah Mahasiswa per Jurusan", "Visualisasi jumlah mahasiswa berdasarkan jurusan")
            st.bar_chart(df["Jurusan"].value_counts())
        else:
            st.info("Belum ada data mahasiswa.")

    elif menu == "Tambah Data":
        page_title("➕", "Tambah Data Mahasiswa", "Masukkan data mahasiswa baru dengan validasi otomatis")

        with st.form("form_tambah"):
            nim = st.text_input("NIM")
            nama = st.text_input("Nama")
            email = st.text_input("Email")
            jurusan = st.selectbox("Jurusan", ["Teknik Informatika", "Sistem Informasi", "Manajemen Informatika"])
            semester = st.selectbox("Semester", ["1", "2", "3", "4", "5", "6", "7", "8"])
            ipk = st.number_input("IPK", min_value=0.00, max_value=4.00, step=0.01, format="%.2f")
            tipe = st.radio("Status", ["Mahasiswa Aktif", "Mahasiswa Beasiswa"])
            submit = st.form_submit_button("Simpan Data")

        if submit:
            try:
                if not valid_nim(nim):
                    st.error("NIM harus angka minimal 5 digit.")
                elif not valid_nama(nama):
                    st.error("Nama hanya boleh huruf dan spasi.")
                elif not valid_email(email):
                    st.error("Format email tidak valid.")
                elif nim in df["NIM"].values:
                    st.error("NIM sudah terdaftar.")
                else:
                    mhs = MahasiswaBeasiswa(nim, nama, email, jurusan, semester, ipk) if tipe == "Mahasiswa Beasiswa" else Mahasiswa(nim, nama, email, jurusan, semester, ipk)
                    data_baru = mhs.to_dict()
                    data_baru["Status"] = mhs.status()
                    df_baru = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
                    save_data(df_baru)
                    st.success("Data mahasiswa berhasil ditambahkan.")
                    st.info(f"Predikat IPK: {predikat_ipk(ipk)}")
                    st.balloons()
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")

    elif menu == "Tampilkan Data":
        page_title("▣", "Data Mahasiswa", "Daftar lengkap data mahasiswa yang tersimpan")

        if df.empty:
            st.warning("Data masih kosong.")
        else:
            df_tampil = df.copy().reset_index(drop=True)
            df_tampil.index = df_tampil.index + 1
            df_tampil["Predikat IPK"] = df_tampil["IPK"].apply(predikat_ipk)
            st.dataframe(df_tampil, use_container_width=True)

            csv = df_tampil.to_csv(index=False).encode("utf-8")
            st.download_button("📥 Download Data CSV", csv, "data_mahasiswa.csv", "text/csv")

    elif menu == "Edit Data":
        page_title("✎", "Edit Data Mahasiswa", "Perbarui data mahasiswa berdasarkan NIM")

        if df.empty:
            st.warning("Data masih kosong.")
        else:
            pilih_nim = st.selectbox("Pilih NIM", df["NIM"].tolist())
            data_lama = df[df["NIM"] == pilih_nim].iloc[0]

            jurusan_list = ["Teknik Informatika", "Sistem Informasi", "Manajemen Informatika"]
            semester_list = ["1", "2", "3", "4", "5", "6", "7", "8"]

            with st.form("form_edit"):
                nama = st.text_input("Nama", data_lama["Nama"])
                email = st.text_input("Email", data_lama["Email"])
                jurusan = st.selectbox(
                    "Jurusan",
                    jurusan_list,
                    index=jurusan_list.index(data_lama["Jurusan"]) if data_lama["Jurusan"] in jurusan_list else 0
                )
                semester = st.selectbox(
                    "Semester",
                    semester_list,
                    index=semester_list.index(str(data_lama["Semester"])) if str(data_lama["Semester"]) in semester_list else 0
                )

                try:
                    ipk_lama = float(data_lama["IPK"])
                except Exception:
                    ipk_lama = 0.00

                ipk = st.number_input("IPK", min_value=0.00, max_value=4.00, value=ipk_lama, step=0.01, format="%.2f")
                submit = st.form_submit_button("Update Data")

            if submit:
                if not valid_nama(nama):
                    st.error("Nama tidak valid.")
                elif not valid_email(email):
                    st.error("Email tidak valid.")
                else:
                    df.loc[df["NIM"] == pilih_nim, ["Nama", "Email", "Jurusan", "Semester", "IPK"]] = [nama, email, jurusan, semester, ipk]
                    save_data(df)
                    st.success("Data berhasil diperbarui.")
                    st.info(f"Predikat IPK terbaru: {predikat_ipk(ipk)}")

    elif menu == "Hapus Data":
        page_title("🗑", "Hapus Data Mahasiswa", "Hapus data mahasiswa yang sudah tidak diperlukan")

        if df.empty:
            st.warning("Data masih kosong.")
        else:
            pilih_nim = st.selectbox("Pilih NIM yang akan dihapus", df["NIM"].tolist())

            if st.button("Hapus Data", type="primary"):
                df_baru = df[df["NIM"] != pilih_nim]
                save_data(df_baru)
                st.success("Data berhasil dihapus.")

    elif menu == "Pencarian":
        page_title("🔍", "Pencarian Data", "Cari mahasiswa menggunakan Linear Search atau Binary Search")

        metode = st.selectbox("Pilih Metode", ["Linear Search", "Binary Search"])
        keyword = st.text_input("Masukkan Nama atau NIM")

        if st.button("Cari", type="primary"):
            if keyword.strip() == "":
                st.warning("Masukkan keyword terlebih dahulu.")
            else:
                hasil = linear_search(df, keyword) if metode == "Linear Search" else binary_search(df, keyword)
                st.info("Time Complexity: O(n)" if metode == "Linear Search" else "Time Complexity: O(log n)")

                if hasil.empty:
                    st.warning("Data tidak ditemukan.")
                else:
                    hasil = hasil.copy()
                    hasil["Predikat IPK"] = hasil["IPK"].apply(predikat_ipk)
                    st.dataframe(hasil, use_container_width=True)

    elif menu == "Pengurutan":
        page_title("↕", "Pengurutan Data", "Urutkan data mahasiswa menggunakan algoritma sorting")

        kolom = st.selectbox("Urutkan berdasarkan", ["NIM", "Nama", "Jurusan", "Semester", "IPK"])
        metode = st.selectbox("Pilih Metode Sorting", ["Bubble Sort", "Merge Sort"])

        if st.button("Urutkan Data", type="primary"):
            if df.empty:
                st.warning("Data masih kosong.")
            else:
                hasil = bubble_sort(df, kolom) if metode == "Bubble Sort" else merge_sort(df, kolom)
                st.info("Time Complexity: O(n²)" if metode == "Bubble Sort" else "Time Complexity: O(n log n)")
                hasil["Predikat IPK"] = hasil["IPK"].apply(predikat_ipk)
                st.dataframe(hasil, use_container_width=True)

    elif menu == "Tentang Program":
        page_title("ⓘ", "Tentang Aplikasi", "Informasi fitur dan konsep pemrograman yang digunakan")

        st.write("""
        Aplikasi ini dibuat untuk memenuhi tugas UAS Manajemen Data Mahasiswa berbasis web.

        Fitur yang digunakan:
        - Input, edit, hapus, dan tampilkan data mahasiswa
        - Penyimpanan data menggunakan File I/O CSV
        - OOP: class, object, encapsulation, inheritance, polymorphism
        - Searching: Linear Search dan Binary Search
        - Sorting: Bubble Sort dan Merge Sort
        - Regex validation
        - Error handling menggunakan try-except
        - Time Complexity
        - IPK menggunakan skala 0.00 sampai 4.00 seperti dunia perkuliahan
        """)

        st.subheader("Predikat IPK")
        st.table({
            "Rentang IPK": ["3.75 - 4.00", "3.50 - 3.74", "3.00 - 3.49", "2.00 - 2.99", "0.00 - 1.99"],
            "Predikat": ["Cumlaude", "Sangat Memuaskan", "Memuaskan", "Cukup", "Kurang"]
        })

        st.subheader("Estimasi Time Complexity")
        st.table({
            "Fitur": ["Linear Search", "Binary Search", "Bubble Sort", "Merge Sort"],
            "Complexity": ["O(n)", "O(log n)", "O(n²)", "O(n log n)"]
        })

    footer()
    st.markdown("</div>", unsafe_allow_html=True)
