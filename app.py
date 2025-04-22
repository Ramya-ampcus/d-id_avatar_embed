import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="D-ID Avatar Embed", layout="centered")

st.title("🎙️ AI Conversational Avatar")
st.markdown("""
This app features a real-time conversational AI avatar embedded using D-ID.

You can interact with the assistant using voice or text, directly on this page.
""")

# 👇 Embed D-ID agent script
html_code = """
<div id="did-agent-container"></div>
<script
    type="module"
    src="https://agent.d-id.com/v1/index.js"
    data-name="did-agent"
    data-mode="fabio"
    data-client-key="Z29vZ2xlLW9hdXRoMnwxMTE5ODc0MjkyMDAyODgwODc1NDI6MjdPMVp1TWRyeFZsYmt0RHpMWDVJ"
    data-agent-id="agt_pgkMtYJk"
    data-monitor="true">
</script>
"""

components.html(html_code, height=600)
