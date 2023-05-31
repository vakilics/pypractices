import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input()

label2 = sg.Text("Enter inches:")
input2 = sg.Input()

Convert_button = sg.Button("Converter")

window = sg.Window("Convert",
                   layout=[[label1, input1],
                           [label2, input2],
                           [Convert_button]])

window.read()
print("Test!")
window.close()

