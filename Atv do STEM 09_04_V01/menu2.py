from cProfile import label
from cgitb import text
from glob import escape
from tkinter import*
from tkinter import ttk

menu = Tk()

def cadastro():
    cadastro = Tk()

    def limpe():
        name.delete(0, END)
        age.delete(0, END)


    def creat_account():
        vNome = name.get()
        vIdade = age.get()
        if vNome == " " or vIdade == " ":
            a = "Nome ou idade incorreto!"
            msg["text"] = a
            limpe()
        else:
            with open("cadastro.txt", 'a' ) as escreva:
                escreva.write("Nome: " + vNome + ', idade ' + vIdade + ' anos '+'\n')
                b = "Cadastro concluido!"
                msg["text"] = b
            print("deu certo amigo!")

    def volta():
        cadastro.destroy()

    cadastro.title("Insert")
    cadastro.geometry("300x300")
    cadastro.configure(background= '#CA8E8E')

    textoInstrutivo = Label(cadastro, text="Insert")
    textoInstrutivo.pack()

    nome = StringVar()
    idade = StringVar()

    name = Entry(cadastro, textvariable=nome)
    name.pack()
    age = Entry(cadastro, textvariable=idade)
    age.pack()

    buttonOk = Button(cadastro, text="Confirm", command=creat_account, background="#8B4513")
    buttonOk.pack()
    space = Label(cadastro, text=" ", background = '#CA8E8E')
    space.pack()

    limpe = Button(cadastro, text="Clear all", command=limpe, background="#8B4513")
    limpe.pack()

    sair = Button(cadastro, text="Exit", command=volta)
    sair.pack()

    msg =Label(cadastro, text="  ",background = '#CA8E8E')
    msg.pack()

    cadastro.mainloop()
    
    
def consult():
    print("Demostrando a listagem de usuarios: ")
    amostra.pack()
    with open("cadastro.txt", 'r') as leitura:
        usuario = leitura.readlines()
        k = ''.join(usuario)
        amostra["text"] = ''.join(k)
        print(usuario)
    
    def back():
        exit1.pack_forget()
        amostra.pack_forget()
    
    esoaco = Label(menu, text=" ", background= '#CA8E8E')
    esoaco.pack()
    exit1 = Button(menu, text="Back", command=back)
    exit1.pack()


#--------------------------------------------------------------------------------------------
menu.title("Menu")
menu.geometry("300x300")
menu.configure(background= '#CA8E8E')

instruir = Label(menu, text = "Do you have account?")
instruir.pack()
space = Label(menu, text=" ", background= '#CA8E8E')
space.pack()
#---------------------------------------------------------------------------------------------
buttonYes = Button(menu, text="Yes", command=consult, background="#8B4513")
buttonYes.pack()
space1 = Label(menu, text=" ", background= '#CA8E8E')
space1.pack()
#-------------------------------------------------------------------------------------------------------------
buttonNo = Button(menu, text="No", command=cadastro, background="#8B4513")
buttonNo.pack()
space2 = Label(menu, text=" ", background= '#CA8E8E')
space2.pack()

secao = Label(menu, text="Usuarios cadastrados: ", background= '#CA8E8E')
secao.pack()
amostra = Label(menu, text="                                  ")
amostra.pack()

menu.mainloop()