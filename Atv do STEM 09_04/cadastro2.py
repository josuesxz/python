from tkinter import*
import os
from tkinter import ttk
import modulo_cadstro

cadastro = Tk()
next2 = os.path.dirname(__file__)

def new_user():
    modulo_cadstro.creat_account()


cadastro.title("Create account")
cadastro.geometry("300x200")
cadastro.configure(background = '#796363')

textoInstrutivo = Label(cadastro, text="Insert your name and you age")
textoInstrutivo.pack()

nome = StringVar()
idade = StringVar()

name = Entry(cadastro, textvariable=nome)
name.pack()
age = Entry(cadastro, textvariable=idade)
age.pack()

buttonOk = Button(cadastro, text="Confirm", command=new_user)

cadastro.mainloop()