#easty to integrate with web apps using "stramlit"
import streamlit as st
import functions

todos = functions.get_todos()

st.title("Welcome Mr. Abdul Rahman Vakili")
st.subheader("This is my todo app!")
st.write("This App helps manage your tasks! ")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add To-DO!", placeholder="something...")