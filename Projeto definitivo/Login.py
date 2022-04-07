from tkinter import*
import os
login = Tk()
pastaApp=os.path.dirname(__file__)

def loginTest():
    p =  vsenha.get()
    u = vuser.get()
    print("Senha digitada:"+ p)
    if p != 'senha' and u != "Josue" :
        a = "Incorrect password or username!"
        msg["text"] = a
    if p == 'senha' and u == 'Josue' :
        exec(open(pastaApp+"\\Menu.py").read())


login.title("Login")
login.geometry("300x200")
login.configure(background = '#796363')

vsenha = StringVar()
vuser = StringVar()

textodeBoasvindas1 = Label(login,text="User", background = '#796363')
textodeBoasvindas1.pack()
user = Entry(login, textvariable=vuser)
user.pack()

textodeBoasvindas2 = Label(login,text="Password",background = '#796363')
textodeBoasvindas2.pack()
password = Entry(login, textvariable=vsenha, show="*")
password.pack()

check = Button(login, text="Enter", command=loginTest)
check.pack()

msg =Label(login, text="  ",background = '#796363')
msg.pack()

login.mainloop()