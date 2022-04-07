from tkinter import*
import os
from tkinter import Button

menu = Tk()
next = os.path.dirname(__file__)

def sensor_a():
    exec(open(next + "\\sensores_a.py").read())

def sensor_b():
    exec(open(next + "\\sensores_b.py").read())

def monitorA():
    with open("dados_a.txt", 'r') as mostre:
        k = mostre.readlines()
        show['text'] = ' '.join(k)

def monitorB():
    with open("dados_b.txt", 'r') as mostre2:
        k2 = mostre2.readlines()
        show['text'] = ' '.join(k2)

def ruaA():
    monitora = Button(menu, text="Monitoramento", command=monitorA)
    monitora.pack()
    capta = Button(menu, text="Captacao de dados", command=sensor_a)
    capta.pack()

def ruaB():
    monitoraB = Button(menu, text="Monitoramento", command=monitorB)
    monitoraB.pack()
    captaB = Button(menu, text="Captacao de dados", command=sensor_b)
    captaB.pack()

menu.title("Select")
menu.geometry("500x300")
menu.configure(background = '#CA8E8E')

instuir = Label(menu, text="Select whether you want to monitor or capture more data",background = '#CA8E8E')
instuir.pack()

ruaA = Button(menu, text="Rua A", command=ruaA)
ruaA.pack()

ruaB = Button(menu, text="Rua B", command=ruaB)
ruaB.pack()

show = Label(menu, text='',background = '#CA8E8E')
show.pack()

menu.mainloop()