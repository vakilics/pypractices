import functions
'''
pip install PySimpleGUI
sudo apt-get install python3.10-tk
'''
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
#del_button = sg.Button("Delete")
#window = sg.Window('My To-Do App', layout=[[label, input_box]])  # both label and input_txt in save row!
#window = sg.Window('My To-Do App', layout=[[label], [input_box], [add_button], [del_button]]) # In different rows!, here based on list, 4 rows!
window = sg.Window('My To-Do App', layout=[[label, input_box, add_button]]) # In two rows!


window.read()
print("Test!")
window.close()

