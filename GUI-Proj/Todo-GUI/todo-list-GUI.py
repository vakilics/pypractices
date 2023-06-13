import functions
'''
pip install PySimpleGUI
sudo apt-get install python3.10-tk
'''
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 20])
edit_button = sg.Button("Edit")

#del_button = sg.Button("Delete")
#window = sg.Window('My To-Do App', layout=[[label], [input_box], [add_button], [del_button]]) # In different rows!, here based on list, 4 rows!
window = sg.Window('My To-Do App',           # In two rows, ...!
                   layout=[[label, input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 16))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)  #to show the todolist after Add in the window

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':    #to show the text we select to edit, in Input box!
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:   # if we click on close icon, then will no more error happens!
            #exit()
            break



print("Test!")
window.close()

