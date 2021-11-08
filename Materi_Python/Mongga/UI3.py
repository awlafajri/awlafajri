import PySimpleGUI as sg
import os.path

kolom1=[
    [
        sg.Text("Image Folder "),
        sg.In(size=(20,1),key="-INPUT-"),
        sg.FolderBrowse(key="-FOLDER-")
    ],
    [
        sg.Listbox(
            values=[], size=(40,20), key="-LIST-"
        )
    ]
]

kolom2=[
    [
        sg.Text("Choose an Image from list from left")
    ],

    [
        sg.Text(size=(20,1),key="-TEXT2-")
    ],

    [
        sg.Image(key="-IMG-")
    ]
]


layout=[
    [
        sg.Column(kolom1),
        sg.VSeparator(),
        sg.Column(kolom2),
    ]
]

window = sg.Window("UI MAINAN",layout)

while True:
    event, values = window.read()
    if event == "Exit" or event==sg.WIN_CLOSED:
        break

    if event == "-FOLDER-":
        folder = values["-FOLDER-"]

        try:
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames= []
        for f in file_list:
            filetotal=os.path.join(folder,f)
            if os.path.isfile(filetotal) and f.lower().endswith((".jpg",".png")):
                fnames.append(f)

        window["-LIST-"].update(fnames)

    if event == "-LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-LIST-"][0]
            )
            window["-TEXT2-"].update(filename)
            window["-IMG-"].update(filename=filename)
        except:
            pass

window.close()