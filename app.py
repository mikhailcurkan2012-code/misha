import streamlit as st

st.set_page_config(page_title="My mega app", page_icon=":)", layout="wide")

st.title("Welcome :D")

tab1, tab2 = st.tabs(["'Bout myself", "My instr."])

with tab1:
    st.header("Znayomstvo th avtorom")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://bestanimations.com/media/halloween/1186756171haloween-dancing-skeletons-2-2.gif", width=200)
    with col2:
        st.subheader("i am misha")
        st.write("i am a guy")
