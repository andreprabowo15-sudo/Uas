import pandas as pd

def _nilai(record, kolom):
    try:
        if kolom == "IPK":
            return float(record[kolom])
        if kolom == "Semester":
            return int(record[kolom])
        return str(record[kolom]).lower()
    except Exception:
        return str(record.get(kolom, "")).lower()

def bubble_sort(df, kolom):
    data = df.to_dict("records")
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):
            if _nilai(data[j], kolom) > _nilai(data[j + 1], kolom):
                data[j], data[j + 1] = data[j + 1], data[j]

    return pd.DataFrame(data)

def merge_sort_list(data, kolom):
    if len(data) <= 1:
        return data

    tengah = len(data) // 2
    kiri = merge_sort_list(data[:tengah], kolom)
    kanan = merge_sort_list(data[tengah:], kolom)

    hasil = []
    i = 0
    j = 0

    while i < len(kiri) and j < len(kanan):
        if _nilai(kiri[i], kolom) <= _nilai(kanan[j], kolom):
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1

    hasil.extend(kiri[i:])
    hasil.extend(kanan[j:])
    return hasil

def merge_sort(df, kolom):
    data = df.to_dict("records")
    return pd.DataFrame(merge_sort_list(data, kolom))
