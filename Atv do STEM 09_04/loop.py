import PySimpleGUI as tela1
import cadastro
import acessando_a_conta

def tela1_incial():
    tela1.theme('DarkBrown2')
    layoutHome = [
        [tela1.Text("Welcome!")],
        [tela1.Text(" ")],
        [tela1.Text("Do you have account?")],
        [tela1.Text("")],
        [tela1.Button("Yes"), tela1.Text(" "), tela1.Button("No")],
        [tela1.Text(" ")]
    ]
    return tela1.Window("Menu incial", layout=layoutHome, finalize=True, element_justification='center')

tela11, tela12, tela13 = tela1_incial(), None, None #escolha de iniciar a janela incial ainda

while True:
    janela, evento, valores = tela1.read_all_windows()
    if janela == tela11 and evento == tela1.WIN_CLOSED:
        break
    if janela == tela11 and evento == "Yes":
        tela12 = acessando_a_conta.already_account()
        tela11.hide()
    elif janela == tela11 and evento == "No":
        tela13 = cadastro.creat_account()
        tela11.hide()

'''
MISSÃO:
    1) Desenvolver a função para voltar em ok no acesso da conta
    2) Desenvolver a tela1 de criação de conta
    3) Melhorar a estéstica das tela1s de acesso e criando a conta
    4) Desenvolver a função de back no botão de criando a conta
'''