import PySimpleGUI as sg

label1 = sg.Text("Enter feet:")
input1 = sg.Input()

label2 = sg.Text("Enter inches:")
input2 = sg.Input()

Convert_button = sg.Button("Converter")
exit_button = sg.Button("Exit")
window = sg.Window("Convert",
                   layout=[[label1, input1],
                           [label2, input2],
                           [Convert_button],
                           [exit_button]])
while True:
    event, values = window.read()
    #if event == "Exit":
    #    break
    #OR following:
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.read()
print("Test!")
window.close()

