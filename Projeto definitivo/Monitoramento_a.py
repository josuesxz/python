from tkinter import*
import os

a = Tk()
back = os.path.dirname(__file__)

a.title("Monitoring system")
a.geometry("600x600")
a.configure(background = '#CA8E8E')

def mona():
    with open("dados_a.txt", 'r') as mostre3:
        k3 = mostre3.readlines()
        txt["text"] = ''.join(k3)

help = Label(a, text='Click to check the information')
help.pack()

run = Button(a, text="Check", command=mona)
run.pack()

txt = Label(a, text=' ',background = '#CA8E8E')
txt.pack()

a.mainloop()