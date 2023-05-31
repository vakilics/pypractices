import functions
'''
pip install PySimpleGUI
sudo apt-get install python3.10-tk
'''
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
#del_button = sg.Button("Delete")
#window = sg.Window('My To-Do App', layout=[[label, input_box]])  # both label and input_txt in save row!
#window = sg.Window('My To-Do App', layout=[[label], [input_box], [add_button], [del_button]]) # In different rows!, here based on list, 4 rows!
window = sg.Window('My To-Do App',           # In two rows!
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 14))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:   # if we click on close icon, then will no more error happens!
            break


print("Test!")
window.close()

