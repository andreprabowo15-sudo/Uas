import os
import pandas as pd
import streamlit as st

DATA_FILE = "data_mahasiswa.csv"
KOLOM = ["NIM", "Nama", "Email", "Jurusan", "Semester", "IPK", "Status"]

def load_data():
    try:
        if os.path.exists(DATA_FILE):
            df = pd.read_csv(DATA_FILE, dtype=str)

            if "Nilai" in df.columns and "IPK" not in df.columns:
                df = df.rename(columns={"Nilai": "IPK"})

            for kolom in KOLOM:
                if kolom not in df.columns:
                    df[kolom] = ""

            return df[KOLOM]

        return pd.DataFrame(columns=KOLOM)
    except Exception as e:
        st.error(f"Error membaca file: {e}")
        return pd.DataFrame(columns=KOLOM)

def save_data(df):
    try:
        df.to_csv(DATA_FILE, index=False)
    except Exception as e:
        st.error(f"Error menyimpan file: {e}")
