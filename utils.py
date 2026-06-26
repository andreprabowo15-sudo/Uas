import re

def valid_nim(nim):
    return re.match(r"^[0-9]{5,15}$", str(nim))

def valid_nama(nama):
    return re.match(r"^[A-Za-z\s]+$", str(nama))

def valid_email(email):
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", str(email))

def predikat_ipk(ipk):
    try:
        ipk = float(ipk)
        if ipk >= 3.75:
            return "🥇 Cumlaude"
        elif ipk >= 3.50:
            return "🟢 Sangat Memuaskan"
        elif ipk >= 3.00:
            return "🟡 Memuaskan"
        elif ipk >= 2.00:
            return "🟠 Cukup"
        return "🔴 Kurang"
    except Exception:
        return "-"
