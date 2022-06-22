import PySimpleGUI as sg
from numpy import save
import os
import time

class View:

    def config(self):
        sg.theme('Dark')
        sg.theme_button_color(('black', 'white'))

    def __init__(self):
        self.pagInicial()
        
    def pagInicial(self):
        self.config()

        appname = "PHPSimple IDE"
        version = " v1.0"
        menu = [
            ['&File', ['&New', '&Save', '&Run']],
        ]

        layout = [
            [sg.Menu(menu, tearoff=False, key='menu', background_color="white", text_color="black", font=("Verdana",10), size=(10,10))],
            #[sg.Multiline('<?php\necho "Hello World"\n?>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <meta http-equiv="X-UA-Compatible" content="IE=edge">\n   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n   <title>Document</title>\n</head>\n<body>\n\n</body>\n</html>', key='dev', size=(200,25))],
            [sg.Multiline('<?php\n\necho "Hello World";\n', key='dev', size=(200,25))],
            [sg.Text('')],
            [sg.Button('Teste', size=(10,1))]
        ]

        janela = sg.Window(appname, layout, size=(1000,600))

        while True:
            event, val = janela.read()
            dev = val['dev']

            if event == sg.WIN_CLOSED:
                exit()
            if event == 'Save':
                self.save(dev)
            if event == 'Teste':
                print(dev)

    def save(self, dev):
        self.config()
        layout = [
            [sg.Text('Save')],
            [sg.Text('')],
            [sg.Text('Project Name:')],
            [sg.Input('index', key='inpNome')],
            #[sg.Text('Folder Name:')],
            #[sg.Input('MyProject', key='inpFolder')],
            [sg.Text('')],
            [sg.Button('Save', key='btnSalvar')],

        ]

        janela = sg.Window('Save', layout, size=(400,300), finalize=True)
        while True:
            event, val = janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'btnSalvar':
                pasta = val['inpFolder']
                proj = val['inpNome']
                
                with open('build/scripts/'+proj+'.php', 'w') as arquivo:
                    arquivo.write(dev)
                    sg.popup("Saved!")

                    
                


View()