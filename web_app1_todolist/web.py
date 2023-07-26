'''
- Easty to integrate with web apps using "stramlit"
- Run the web-app: streamlit run web.py
- By refreshing the web page, python code will be executed from top to button!
NOTE: to publish the web_app:
 1. Collect the running requirements existing in machine where this app is running:
    * pip freeze > requirements.txt  # this includes all python-modules required for server which runs the web app!

'''

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

for index, todo in enumerate(todos):
    #st.checkbox(todo, key=todo) #will show each checkbox status
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:   #means: if checkbox is checked/ticked
        #print(checkbox)
        todos.pop(index)
        functions.write_todos(todos) #again write the updated todos without the removed todo.
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Add To-DO!", placeholder="something...", on_change=add_todo, key='my_new_todo')

#print("End of App!")
st.session_state