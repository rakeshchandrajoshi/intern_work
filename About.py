import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

st.title("ℹ️ About This Tool")
st.markdown("""
This application uses AI and web scraping to extract product pricing information from hydroponic farming websites.

**Key Technologies:**
- 🔍 Firecrawl API for scraping
- 🤖 Groq LLM for product parsing
- 🖥️ Streamlit for UI/UX

Developed as a research tool for smart agriculture and supply chain insights.
""")
