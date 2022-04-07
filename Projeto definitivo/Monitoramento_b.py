from tkinter import*
import os

b = Tk()
back = os.path.dirname(__file__)

b.title("Monitoring system")
b.geometry("600x600")
b.configure(background = '#CA8E8E')

def mona():
    with open("dados_b.txt", 'r') as mostre2:
        k2 = mostre2.readlines()
        txt ['text'] = ' '.join(k2)

help = Label(b, text='Click to check the information')
help.pack()

run = Button(b, text="Check", command=mona)
run.pack()

txt = Label(b, text="",background = '#CA8E8E')
txt.pack()

b.mainloop()