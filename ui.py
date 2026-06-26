import streamlit as st

def show_sidebar():
    st.markdown("""
    <div class="custom-sidebar">
        <div class="brand-box">
            <div class="brand-icon">🎓</div>
            <div>
                <div class="brand-text-small">Aplikasi</div>
                <div class="brand-text-main">Manajemen Data<br>Mahasiswa</div>
            </div>
        </div>
        <div class="menu-title">MENU</div>
    """, unsafe_allow_html=True)

def close_sidebar():
    st.markdown("</div>", unsafe_allow_html=True)

def menu_button(label, target):
    tipe = "primary" if st.session_state.menu == target else "secondary"
    if st.button(label, use_container_width=True, type=tipe):
        st.session_state.menu = target
        st.rerun()

def page_title(icon, title, desc):
    st.markdown(
        f"""
        <div class="page-title">
            <div class="page-icon">{icon}</div>
            <h1>{title}</h1>
        </div>
        <div class="page-desc">{desc}</div>
        """,
        unsafe_allow_html=True
    )

def section_title(icon, title, desc=""):
    st.markdown(
        f"""
        <div class="section-title"><span>{icon}</span><h2>{title}</h2></div>
        <div class="section-desc">{desc}</div>
        """,
        unsafe_allow_html=True
    )

def footer():
    st.markdown(
        '<div class="footer">© 2026 | Sistem Manajemen Data Mahasiswa | Tugas UAS</div>',
        unsafe_allow_html=True
    )
