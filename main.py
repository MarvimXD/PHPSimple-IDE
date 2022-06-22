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
            ['&Apache', ['&Iniciar', 'Instalar']],
            ['&File', ['&New', '&Save', '&Run']],
        ]

        layout = [
            [sg.Menu(menu, tearoff=False, key='menu', background_color="white", text_color="black", font=("Verdana",10), size=(10,10))],
            #[sg.Multiline('<?php\necho "Hello World"\n?>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <meta http-equiv="X-UA-Compatible" content="IE=edge">\n   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n   <title>Document</title>\n</head>\n<body>\n\n</body>\n</html>', key='dev', size=(200,25))],
            [sg.Multiline('<?php\n\necho "Hello World";\n', key='dev', size=(200,25), disabled=True)],
            [sg.Text('')],
            [sg.Text('Start a new project!'), sg.Button('Click here', key='btnNewProject', size=(10,1))],
        ]

        janela = sg.Window(appname, layout, size=(1000,500))

        while True:
            event, val = janela.read()
            dev = val['dev']

            if event == sg.WIN_CLOSED:
                exit()
            if event == 'Save':
                self.save(dev)
            if event == 'Run':
                self.run(dev)
            if event == 'Iniciar':
                sg.popup("O Apache será iniciado!")
                os.system("start res/batsrc/apacheinit.lnk")
            if event == 'Instalar':
                sg.popup("O Apache será instalado!")
                os.system("start res/batsrc/apacheinstall.lnk")

            if event == 'New' or event == 'btnNewProject':
                self.newProject()
    
    def pagProjeto(self, nome):
        self.config()

        appname = "PHPSimple IDE"
        version = " v1.0"
        menu = [
            ['&Apache', ['&Iniciar', 'Instalar']],
            ['&File', ['&New', '&Save', '&Run']],
        ]

        layout = [
            [sg.Menu(menu, tearoff=False, key='menu', background_color="white", text_color="black", font=("Verdana",10), size=(10,10))],
            #[sg.Multiline('<?php\necho "Hello World"\n?>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <meta http-equiv="X-UA-Compatible" content="IE=edge">\n   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n   <title>Document</title>\n</head>\n<body>\n\n</body>\n</html>', key='dev', size=(200,25))],
            [sg.Multiline('<?php\n\necho "Hello World";\n', key='dev', size=(200,25))],
            [sg.Text('')],
            [sg.Button('IfElseIf', size=(10,1))],
            [sg.Button('IfElse', size=(10,1))],
            
        ]

        janela = sg.Window(appname + ' ' + nome, layout, size=(1000,600))

        while True:
            event, val = janela.read()
            dev = val['dev']

            if event == sg.WIN_CLOSED:
                exit()
            if event == 'Save':
                self.save(dev, nome)
            if event == 'Run':
                self.run(dev)
            if event == 'Iniciar':
                sg.popup("O Apache será iniciado!")
                os.system("start res/batsrc/apacheinit.lnk")
            if event == 'Instalar':
                sg.popup("O Apache será instalado!")
                os.system("start res/batsrc/apacheinstall.lnk")
            if event == 'IfElseIf':
                text = janela['dev']
                text.update(text.get()+"\n\nif($condition) {\n    //Write your code here\n\n\n} else if ($condition2) { \n    //Write your code here\n\n\n} else {\n    //Write your code here")
            if event == 'IfElse':
                text = janela['dev']
                text.update(text.get()+"\n\nif($condition) {\n    //Write your code here\n\n\n} else {\n    //Write your code here")



    def newProject(self):
        self.config()
        layout = [
            [sg.Text('Project Name:')],
            [sg.Input('index', key='inpNome')],
            [sg.Text('')],
            [sg.Button('Create', key='btnCmd')],

        ]

        janela = sg.Window('Save', layout, size=(200,120), finalize=True)
        while True:
            event, val = janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'btnCmd':
                proj = val['inpNome']
                self.pagProjeto(proj)
                

    def run(self, dev):
        with open('php/temp.php', 'w') as arquivo:
            arquivo.write(dev)
            os.system("start http://localhost/temp.php/")


    def save(self, dev, nome=None):
        self.config()
        if nome == None:
            layout = [
                [sg.Text('Project Name:')],
                [sg.Input('index', key='inpNome')],
                #[sg.Text('Folder Name:')],
                #[sg.Input('MyProject', key='inpFolder')],
                [sg.Text('')],
                [sg.Button('Save', key='btnSalvar')],

            ]
        else:
            layout = [
                [sg.Text('Project Name:')],
                [sg.Input(nome, key='inpNome')],
                #[sg.Text('Folder Name:')],
                #[sg.Input('MyProject', key='inpFolder')],
                [sg.Text('')],
                [sg.Button('Save', key='btnSalvar')],

            ]

        janela = sg.Window('Save', layout, size=(200,120), finalize=True)
        while True:
            event, val = janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'btnSalvar':
                proj = val['inpNome']
                
                with open('php/'+proj+'.php', 'w') as arquivo:
                    arquivo.write(dev)
                    sg.popup("Saved in 'php' folder!")
                    os.system("start http://localhost/"+proj+".php/")

                    
                


View()