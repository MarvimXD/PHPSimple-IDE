import PySimpleGUI as sg
from numpy import amax, save
import os
import time
import texts
import config

class View:

    def config(self):
        sg.theme('Dark')
        sg.theme_button_color(('black', 'white'))

    def __init__(self):
        self.pagInicial()
        
    def pagInicial(self):
        self.config()
        appname = config.appname()
        version = config.version()
        menu = [
            ['&Apache', ['&Start', 'Install']],
            ['&File', ['&New']],
            ['&Help', ['&How to Use']],
        ]

        layout = [
            [sg.Menu(menu, tearoff=False, key='menu', background_color="white", text_color="black", font=("Verdana",10), size=(10,10))],
            #[sg.Multiline('<?php\necho "Hello World"\n?>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <meta http-equiv="X-UA-Compatible" content="IE=edge">\n   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n   <title>Document</title>\n</head>\n<body>\n\n</body>\n</html>', key='dev', size=(200,25))],
            [sg.Multiline(''+appname+version+'\n\n'+texts.initWelcome(), key='dev', size=(200,7), font='Verdana', disabled=True)],
            [sg.Multiline('History\n\n'+texts.initHistory(), key='dev', size=(200,8), font='Verdana', disabled=True)],
            [sg.Multiline('Newest\n\n'+texts.initNewest(), key='dev', size=(200,5), font='Verdana', disabled=True)],
            [sg.Text('')],
            [sg.Text('Start a new project!'), sg.Button('Click here', key='btnNewProject', size=(10,1))],
        ]

        janela = sg.Window(appname, layout, icon=config.pathico(), size=(1000,500), finalize=True)

        while True:
            event, val = janela.read()
            dev = val['dev']

            if event == sg.WIN_CLOSED:
                exit()
            if event == 'Save':
                self.save(dev)
            if event == 'Run':
                self.run(dev)
            if event == 'Start':
                sg.popup("Apache is going to start!")
                os.system("start res/batsrc/apacheinit.lnk")
            if event == 'Install':
                sg.popup("Apache will be installed!")
                os.system("start res/batsrc/apacheinstall.lnk")

            if event == 'New' or event == 'btnNewProject':
                self.newProject(janela)
            if event == 'How to Use':
                self.howTo()
    
    def pagProjeto(self, nome):
        self.config()

        appname = config.appname()
        version = config.version()

        menu = [
            ['&Apache', ['&Start', 'Install']],
            ['&File', ['&New', '&Save', '&Run']],
            ['&Help', ['&How to Use']],
        ]

        layout = [
            [sg.Menu(menu, tearoff=False, key='menu', background_color="white", text_color="black", font=("Verdana",10), size=(10,10))],
            #[sg.Multiline('<?php\necho "Hello World"\n?>\n<html lang="en">\n<head>\n   <meta charset="UTF-8">\n   <meta http-equiv="X-UA-Compatible" content="IE=edge">\n   <meta name="viewport" content="width=device-width, initial-scale=1.0">\n   <title>Document</title>\n</head>\n<body>\n\n</body>\n</html>', key='dev', size=(200,25))],
            [sg.Multiline('<?php\n\necho "Hello World";\n', key='dev', size=(200,25))],
            [sg.Text('')],
            [sg.Text('Common'), sg.Text('Examples', pad=(36,0))],
            [sg.Button('If Else If', key='btnElif', size=(10,1)), sg.Button('Counter', key='btnCounter', size=(10,1))],
            [sg.Button('If Else', key='btnIf', size=(10,1)), sg.Button('Variable', key='btnVari', size=(10,1))],
            [sg.Button('While', key='btnWhile', size=(10,1)), sg.Button('Print/Show', key='btnPrint', size=(10,1))],
            [sg.Button('For', key='btnFor', size=(10,1)), sg.Button('Defined Var', key='btnDef', size=(10,1))],
            
        ]

        janela = sg.Window(appname + ' ' + nome, layout, icon=config.pathico(), size=(1000,630))

        while True:
            event, val = janela.read()
            dev = val['dev']

            if event == sg.WIN_CLOSED:
                exit()
            if event == 'How to Use':
                self.howTo()
            if event == 'New':
                self.newProject(janela)
            if event == 'Save':
                self.save(dev, nome)
            if event == 'Run':
                self.run(dev, nome)
            if event == 'Start':
                sg.popup("Apache is going to start!")
                os.system("start res/batsrc/apacheinit.lnk")
            if event == 'Install':
                sg.popup("Apacha will be installed!")
                os.system("start res/batsrc/apacheinstall.lnk")
            if event == 'btnElif':
                text = janela['dev']
                text.update(text.get()+"\n\nif($condition) {\n    //Write your code here\n\n\n} else if ($condition2) { \n    //Write your code here\n\n\n} else {\n    //Write your code here")
            if event == 'btnIf':
                text = janela['dev']
                text.update(text.get()+"\n\nif($condition) {\n    //Write your code here\n\n\n} else {\n    //Write your code here")
            if event == 'btnWhile':
                text = janela['dev']
                text.update(text.get()+"\n\nwhile($condition) {\n    //Write your code here\n\n\n}")
            if event == 'btnFor':
                text = janela['dev']
                text.update(text.get()+"\n\nfor($i;$i<0;$i++) {\n    //Write your corde\n\n\n}")
            if event == 'btnCounter':
                text = janela['dev']
                text.update(text.get()+"\n\n//An example to count numbers from 0 to 99 using variables in PHP with break line <br>\n\nfor($i=0;$i<100;$i++) {\n    echo $i . '<br>';\n\n\n}")
            if event == 'btnVari':
                text = janela['dev']
                text.update(text.get()+"\n\n//Variable example:\n\n$variable_name = 'Hello World';")
            if event == 'btnPrint':
                text = janela['dev']
                text.update(text.get()+"\n\n//Printing/Showing something like a variable example:\n\n$variable_name = 'Hello World';\necho $variable_name;")
            if event == 'btnDef':
                text = janela['dev']
                text.update(text.get()+"\n\n//By defining a variable it cannot be changed during the execution of the code\n\ndefine('VARIABLE_NAME', 'Hello World');\necho VARIABLE_NAME;")



    def howTo(self):
        self.config()
        layout = [
            [sg.Text('How to Use:')],
            [sg.Text('The first step to use PHPSide is installing and starting the Apache,\nyou can find it on menu upside the main page.')],
            [sg.Text('After the instalation you just have to start it.')],
            [sg.Text('Once with the Apache installed and started you can start a new project in File > New.')],
            [sg.Text('With your project already started you can start learning PHP or training it as your wish.')],
            [sg.Text('')],
            [sg.Text('Run')],
            [sg.Text('You can run your project easily by using the option "Run" in menu File > Run.')],
            [sg.Text('')],
            [sg.Text('Save')],
            [sg.Text('To save your project just click in "Save" option in menu File > Save.')],
            [sg.Text('')],
            [sg.Text('')],
            

        ]

        janela = sg.Window('Save', layout, icon=config.pathico(), finalize=True)
        while True:
            event, val = janela.read()
            if event == sg.WIN_CLOSED or event == 'btnCmd':
                break


    def newProject(self, janelaOld):
        self.config()
        layout = [
            [sg.Text('Project Name:')],
            [sg.Input('index', key='inpNome')],
            [sg.Text('')],
            [sg.Button('Create', key='btnCmd')],

        ]

        janela = sg.Window('Save', layout, icon=config.pathico(), size=(200,120), finalize=True)
        while True:
            event, val = janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'btnCmd':
                proj = val['inpNome']
                janela.close()
                janelaOld.close()
                self.pagProjeto(proj)
                

    def run(self, dev, nome):
        with open('php/'+nome+'.php', 'w') as arquivo:
            arquivo.write(dev)
            os.system("start http://localhost/"+nome+".php/")


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

        janela = sg.Window('Save', layout, icon=config.pathico(), size=(200,120), finalize=True)
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