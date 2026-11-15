import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="EtanCheck Pro", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        #MainMenu, header, footer, [data-testid="stToolbar"] {display: none !important;}
        .block-container {padding: 0 !important; margin: 0 !important; max-width: 100% !important;}
        iframe {width: 100vw !important; height: 100vh !important; height: 100dvh !important; border: none !important; display: block !important;}
    </style>
""", unsafe_allow_html=True)

with open("index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=900, scrolling=True)
