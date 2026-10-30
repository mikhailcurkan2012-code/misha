import streamlit as st

st.set_page_config(page_title="My mega app", page_icon=":)", layout="wide")

st.title("Welcome :D")

tab1, tab2, tab3 = st.tabs(["🏠 Головна", "📊 Статистика", "🔗 Корисні посилання"])

with tab3:
    st.subheader("📌 Мої улюблені навчальні сайти та ресурси")
    
    # Створюємо дві колонки
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📚 Навчання")
        st.markdown("- 🌐 [Python Official Documentation](https://www.python.org) — офіційний сайт Python")
        st.markdown("- 🤖 [ChatGPT](https://chatgpt.com) — штучний інтелект для навчання")
        
    with col2:
        st.markdown("### 🎮 Корисні ігри та практики")
        st.markdown("- 🐍 [CheckiO](https://checkio.org) — вивчення Python через гру")
        st.markdown("- 🧩 [LeetCode](https://leetcode.com) — розв'язання задач та тренування логіки")
