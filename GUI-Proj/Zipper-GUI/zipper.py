import PySimpleGUI as sg
label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select Destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button]])

while True:
    event, values = window.read()
    print(event,values)
    filepath = values["Choose"].split(";")
    folder = values["folder"]


window.read()
window.close()
print("Test!")