import pandas as pd

def linear_search(df, keyword):
    hasil = []
    keyword = str(keyword).lower()

    for _, row in df.iterrows():
        nama = str(row["Nama"]).lower()
        nim = str(row["NIM"])
        if keyword in nama or keyword in nim:
            hasil.append(row)

    return pd.DataFrame(hasil)

def binary_search(df, nim):
    df_sorted = df.sort_values("NIM").reset_index(drop=True)
    kiri = 0
    kanan = len(df_sorted) - 1
    nim = str(nim)

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        nilai_tengah = str(df_sorted.loc[tengah, "NIM"])

        if nilai_tengah == nim:
            return pd.DataFrame([df_sorted.loc[tengah]])
        elif nilai_tengah < nim:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return pd.DataFrame()
