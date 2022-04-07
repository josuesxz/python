import PySimpleGUI as tela

def already_account():
    print("Demostrando a listagem de usuarios: ")
    with open("cadastro.txt", 'r') as leitura:
            usuario = leitura.readlines()
            k = ''.join(usuario)
            print(usuario)
    
    tela.theme("DarkBrown2")
    layoutShow = [
        [tela.Text("Here there all users:")],
        [tela.Text(" ")],
        [tela.Text(k)],
        [tela.Text(" ")],
        [tela.Button("ok")]
    ]
    window = tela.Window("Informações", layout=layoutShow, finalize=True, element_justification='center')
    eventos = tela.read_all_windows()

    if eventos == "ok":
        window.close()
    return 0
