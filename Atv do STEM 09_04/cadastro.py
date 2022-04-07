from os import read
import PySimpleGUI as tela2

def register(evento):
     with open("cadastro.txt", 'a' ) as escreva:
            escreva.write({'nome'} + '\t')
            escreva.write(str({'idade'}) + '\n')
            print("deu certo amigo!")

def creat_account():
    tela2.theme("Reddit")
    layoutSign = [
        [tela2.Text("É necessário criar uma conta para acesso")],
        [tela2.Text("Nome"), tela2.Input(key='nome')],
        [tela2.Text("Idade"), tela2.Input(key='idade')],
        [tela2.Button("OK")]
    ]
    eventos = tela2.read_all_windows()
    if eventos == "Ok":
        register()

    return tela2.Window("Cadastro", layout=layoutSign, finalize=True, element_justification='center')