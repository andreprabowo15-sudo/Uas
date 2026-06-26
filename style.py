import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: #f8fafc;
    }

    .block-container {
        padding-top: 1.2rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Hilangkan jarak aneh bawaan Streamlit */
    div[data-testid="stVerticalBlock"] {
        gap: 0.65rem;
    }

    /* Sidebar HTML buatan sendiri, stabil di local dan deploy */
    .custom-sidebar {
        background: #0F4C81;
        min-height: 100vh;
        border-radius: 0 18px 18px 0;
        padding: 24px 18px;
        border-right: 5px solid #2F80ED;
        box-shadow: 6px 0 22px rgba(15, 23, 42, 0.18);
        color: white;
    }

    .brand-box {
        display: flex;
        align-items: center;
        gap: 12px;
        padding-bottom: 20px;
        margin-bottom: 18px;
        border-bottom: 1px solid rgba(255,255,255,0.25);
    }

    .brand-icon {
        font-size: 34px;
        line-height: 1;
    }

    .brand-text-small {
        font-size: 13px;
        color: #A7D3FF;
        font-weight: 800;
        line-height: 1.25;
    }

    .brand-text-main {
        font-size: 14px;
        color: white;
        font-weight: 800;
        line-height: 1.35;
    }

    .menu-title {
        color: #A7D3FF;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.7px;
        margin: 4px 0 8px 0;
    }

    /* Tombol menu di area sidebar */
    .custom-sidebar div[data-testid="stButton"] > button {
        width: 100% !important;
        height: 39px !important;
        min-height: 39px !important;
        background: transparent !important;
        color: white !important;
        border: 0 !important;
        border-radius: 10px !important;
        padding: 0 10px !important;
        margin: 0 0 4px 0 !important;

        display: flex !important;
        justify-content: flex-start !important;
        align-items: center !important;
        text-align: left !important;

        font-size: 12.5px !important;
        font-weight: 600 !important;
        transition: 0.2s ease-in-out !important;
    }

    .custom-sidebar div[data-testid="stButton"] > button p {
        width: 100% !important;
        text-align: left !important;
        color: inherit !important;
        margin: 0 !important;
        padding: 0 !important;
        font-size: 12.5px !important;
    }

    .custom-sidebar div[data-testid="stButton"] > button:hover {
        background: #2F80ED !important;
        color: white !important;
    }

    .custom-sidebar div[data-testid="stButton"] > button[kind="primary"] {
        background: #2F80ED !important;
        color: white !important;
        box-shadow: 0 8px 18px rgba(47,128,237,.35) !important;
        font-weight: 800 !important;
    }

    .content-area {
        background: white;
        min-height: 100vh;
        border-radius: 18px;
        padding: 34px 38px;
        box-shadow: 0 3px 18px rgba(15, 23, 42, 0.08);
        border-left: 5px solid #2F80ED;
    }

    .page-title {
        display: flex;
        align-items: center;
        gap: 14px;
        margin-bottom: 6px;
    }

    .page-icon {
        font-size: 38px;
        line-height: 1;
    }

    .page-title h1 {
        margin: 0;
        font-size: 34px;
        font-weight: 800;
        color: #0f172a;
    }

    .page-desc {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 28px;
    }

    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 18px;
        margin-bottom: 32px;
    }

    .card {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 24px 26px;
        display: flex;
        align-items: center;
        gap: 22px;
        box-shadow: 0 2px 8px rgba(15,23,42,.06);
        min-height: 118px;
    }

    .card-icon {
        width: 70px;
        height: 70px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 34px;
    }

    .blue-bg { background: #e8f1ff; color: #2563eb; }
    .green-bg { background: #dcfce7; color: #16a34a; }
    .purple-bg { background: #f3e8ff; color: #7e22ce; }

    .card-label {
        color: #334155;
        font-size: 14px;
        margin-bottom: 8px;
    }

    .card-value {
        color: #2563eb;
        font-size: 31px;
        font-weight: 800;
        line-height: 1;
    }

    .card-small {
        color: #64748b;
        font-size: 13px;
        margin-top: 9px;
    }

    .section-title {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-top: 16px;
        margin-bottom: 4px;
    }

    .section-title span {
        font-size: 28px;
        color: #2563eb;
    }

    .section-title h2 {
        margin: 0;
        font-size: 25px;
        color: #0f172a;
        font-weight: 800;
    }

    .section-desc {
        color: #64748b;
        font-size: 13.5px;
        margin-bottom: 18px;
    }

    div[data-testid="stDataFrame"] {
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid #dbe4f0 !important;
    }

    .footer {
        color: #64748b;
        font-size: 12px;
        margin-top: 40px;
        padding-top: 12px;
        border-top: 1px solid #e2e8f0;
        text-align: center;
    }

    @media (max-width: 900px) {
        .cards { grid-template-columns: 1fr; }
        .content-area { padding: 24px 20px; }
        .page-title h1 { font-size: 27px; }
    }
    </style>
    """, unsafe_allow_html=True)
