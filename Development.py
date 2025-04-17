import streamlit as st

st.set_page_config(page_title="Development", page_icon="🛠️")

st.title("🛠️ Development Details")
st.markdown("""
### Workflow:
1. **Scraping**: Extract raw HTML/text content from selected websites.
2. **Parsing with AI**: Use LLM to extract structured product name, price, and unit.
3. **Display**: Show extracted results in a user-friendly interface.

### Next Features:
- 🌾 Category filters
- 📈 Price tracking
- 📤 Export to CSV
- 🌍 Support for more sites
""")
