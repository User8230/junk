import PySimpleGUI as sg
import datetime

from datetime import time, tzinfo, timedelta, timezone

sg.theme('Black')
layout = [  [sg.Text(size=(110,1), 
                     font='courier 96',
                     pad=(5,(130,3)), 
                     justification='c', 
                     key='-UTC-')],
            [sg.Text(size=(150,1), 
                     font='courier 18', 
                     justification='c', 
                     key='-LOCAL-')],
            [sg.Button('Exit', 
                       font='LiberationSans 10',
                       pad=(5,(100,3)))]  ]
layout3 = [  [sg.Text('My Timer', size=(30,1), pad=(5,(3,3)), justification='c')],
            [sg.Text(size=(30,1), justification='c', key='-UTC-')],
            [sg.Button('Exit')]  ]
layout2 = [  [sg.Text('My Timer')],
            [sg.Text(size=(15,1), key='-LOCAL-')],
            [sg.Text(size=(15,1), key='-UTC-')],
            [sg.Button('Exit')]  ]

window = sg.Window('Timer', layout, font='Any 20', 
    no_titlebar=False, grab_anywhere=True, resizable=True, finalize=True)
#window = sg.Window('Timer', layout, finalize=True)
window.Maximize()

while True:             # Event Loop
    event, values = window.read(timeout=100)
    if event in (None, 'Exit'):
        break
    # window['-OUT-'].update(counter)
    # https://strftime.org/
    # pound sign in windows, hyphen in unix eliminates leading zero
    #format="%a %b %-d %-I:%M%p"
    format="%H:%M:%S"
    # "Mon Sep 30 07:06:05 2013"
    t = datetime.datetime.now(timezone.utc).strftime(format)
    window['-UTC-'].update(t)
    #format="%c"
    t = datetime.datetime.now().strftime("%c")
    window['-LOCAL-'].update(t)

window.close()

exit()

