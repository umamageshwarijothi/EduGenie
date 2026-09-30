import streamlit as st
st.set_page_config(page_title="EduGenie", page_icon="📚")
st.title("📚 EduGenie - Personalized Learning")
st.write("AI-powered study assistant")

topic = st.text_input("Enna topic padikkanum?")
if st.button("Learn"):
    st.success(f"{topic} patri padikkalam!")
    st.write(f"AI Summary for {topic} will come here...")

question = st.text_area("Unga doubt ketka:")
if st.button("Get Answer"):
    st.info("AI answer inge varum")
