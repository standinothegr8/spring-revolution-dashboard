"""Spring Revolution Dashboard — Streamlit host.

The dashboard itself is a self-contained HTML/JS page (assets/dashboard.html).
Streamlit serves it full-width inside a component frame, so every interaction
(tabs, cartogram, sliders, calibration game) keeps working unchanged. Per-viewer
state is stored in the visitor's own browser, exactly as on the original page.
"""
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

ROOT = Path(__file__).parent
HTML_PATH = ROOT / "assets" / "dashboard.html"

st.set_page_config(
    page_title="Spring Revolution Dashboard — by Stan",
    page_icon="🌼",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Remove Streamlit's default padding so the page runs edge to edge.
st.markdown(
    """
    <style>
      .block-container {padding: 0 !important; max-width: 100% !important;}
      header[data-testid="stHeader"] {height: 0; background: transparent;}
      footer {display: none;}
      iframe {display: block; border: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = HTML_PATH.read_text(encoding="utf-8")

# Height is fixed by Streamlit's component API; the frame scrolls internally.
# Raise FRAME_HEIGHT if you add sections. Deep links: append ?tab=ground etc.
FRAME_HEIGHT = 2600
tab = st.query_params.get("tab")
if tab and tab.isalpha():
    # Forward ?tab= to the page's own hash router (runs before the page script).
    html = html.replace("<body>", f"<body><script>location.hash='{tab}';</script>", 1)

# st.iframe (Streamlit >= 1.60) replaces components.html and can size the frame
# to its content; older releases fall back to a fixed-height component frame.
if hasattr(st, "iframe"):
    build_dir = ROOT / ".build"
    build_dir.mkdir(exist_ok=True)
    page = build_dir / f"dashboard_{tab or 'pulse'}.html"
    if not page.exists() or page.read_text(encoding="utf-8") != html:
        page.write_text(html, encoding="utf-8")
    st.iframe(page, height="content")
else:
    components.html(html, height=FRAME_HEIGHT, scrolling=True)
