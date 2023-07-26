#easty to integrate with web apps using "stramlit"
# By refreshing the web page, python code will be executed from top to button!
import streamlit as st
import functions


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["my_new_todo"] + "\n"
    #print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("Welcome Vakili's To-Do Web App!")
st.subheader("This is my todo app!")
st.write("This App helps manage your tasks! ")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add To-DO!", placeholder="something...", on_change=add_todo, key='my_new_todo')

#print("End of App!")
st.session_state