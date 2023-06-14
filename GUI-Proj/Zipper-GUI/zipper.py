import PySimpleGUI as sg
from zipcreator import make_archive

label1 = sg.Text("Select file")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="files")

label2 = sg.Text("Select Destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, output_label]])

#text = sg.Text("Welcome")
#button = sg.Button("DELETEokok", key="delete")
#window = sg.Window('My App', layout=[[text], [button]])

while True:
    event, values = window.read()
    print(event,values)
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths, folder)
    window["output"].update(background_color="yellow",  value="Compresseion Completed!")  #will print this text next to the "Compress" cutton in out GUI app!


window.read()
window.close()
print("Test!")