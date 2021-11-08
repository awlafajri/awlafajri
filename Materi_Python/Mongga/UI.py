import PySimpleGUI as sg


kolom1=[
    [sg.Text("Baris 1 kolom 1"), sg.Text("ini kolom tambahan")],
    [sg.Text("Baris 2 kolom 1")]
]



kolom2=[
    [sg.Text("Baris 1 kolom 2")],
    [sg.Text("Baris 2 kolom 2")],
    [sg.Button("Tombol",key="-BUT-")],
    [sg.Submit("Submit")],
    [sg.Cancel("Cancel")],
    [sg.Checkbox("Checkbox")],
    [sg.Image(key="-IMA-")],
    [sg.In(size=(40,1),key="-IN-")]

]

layout=[[
    sg.Column(kolom2)
    ]
]

window = sg.Window("Aplikasi latihan",layout)
print(dir(window))

while True:

    event, values = window.read()

    if event == "Exit" or event == sg.WIN_CLOSED:

        break

window.close()