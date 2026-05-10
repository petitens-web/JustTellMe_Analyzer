import streamlit as st
import streamlit.components.v1 as components
import os

# 1. Page Setup
st.set_page_config(
    page_title="JusTelMi PVT Analyzer",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. UI Reset (Hiding Streamlit elements for a custom look)
st.markdown("""
    <style>
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding: 0px; margin: 0px; max-width: 100%; }
        iframe { display: block; width: 100vw; height: 100vh; border: none; }
        [data-testid="stSidebarNav"] { display: none; }
    </style>
""", unsafe_allow_html=True)

# 3. State Management
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

# 4. Content Loader
def render_page(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            html_content = f.read()
            components.html(html_content, height=2500, scrolling=True)
    else:
        st.error(f"Required file '{file_name}' was not found in the repository.")

# 5. Routing Logic
if not st.session_state.authenticated:
    # Shows the landing/login page
    render_page("index.html")
    
    # Navigation Bridge (Since iframe-to-parent communication is restricted)
    if st.button("Enter Dashboard"):
        st.session_state.authenticated = True
        st.rerun()
else:
    # Shows the main analyzer
    render_page("app_4.html")
    
    # Sidebar logout option
    if st.sidebar.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()
