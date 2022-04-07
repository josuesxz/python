from tkinter import*
import os
from tkinter import ttk

menu = Tk()
next = os.path.dirname(__file__)

def adiante():
    vr = cb_ruas.get()
    vf = cb_funcao.get()
    if vf == 'Captacao de dados':
        if vr == "Rua A":
            exec(open(next + "\\sensores_a.py").read())
        if vr == "Rua B":
            exec(open(next + "\\sensores_b.py").read())
        show['text'] = "List updated successfully!"
    if vf == "Monitoramento":
        if vr == "Rua B":
            with open("dados_b.txt", 'r') as mostre2:
                k2 = mostre2.readlines()
                show['text'] = ' '.join(k2)
        if vr == "Rua A":
            with open("dados_a.txt", 'r') as mostre:
                k = mostre.readlines()
                show['text'] = ' '.join(k)

menu.title("Select")
menu.geometry("600x600")
menu.configure(background = '#CA8E8E')

instuir = Label(menu, text="Select whether you want to monitor or capture more data",background = '#CA8E8E')
instuir.pack()

ruas = ["Rua A", "Rua B"]
lbruas= Label(menu, text="Road")
lbruas.pack()
cb_ruas = ttk.Combobox(menu, values=ruas)
cb_ruas.pack()

funcao = ["Monitoramento", "Captacao de dados"]
lbfuncao= Label(menu, text="Operation")
lbfuncao.pack()
cb_funcao = ttk.Combobox(menu, values=funcao)
cb_funcao.pack()

check = Button(menu, text="Next", command=adiante)
check.pack()

show = Label(menu, text='',background = '#CA8E8E')
show.pack()

menu.mainloop()