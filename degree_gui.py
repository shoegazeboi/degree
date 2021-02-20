import PySimpleGUI as sg
from degree import degree
import sys

sg.theme('DarkAmber')
layout = [
    [sg.Text('Enter degree'), sg.InputText(default_text=2)],
    [sg.Text('Enter number'), sg.InputText()],
    [sg.Button('Raise'), sg.Button('Cancel')]
          ]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancel':
        sys.exit()

    if event == 'Raise':

        answer = degree(values[1], values[0], console='off')
        if type(answer) is str:
            sg.popup_error(answer)
        else:
            sg.popup('raised\n {}'.format(answer[0]))
