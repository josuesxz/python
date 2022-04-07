import cadastro

def inicial():
    q = str(input("É cadastrado? S/N ")).upper()
    print(q)

    if q == "S":
        print("Sim, sou cadastrado")
        cadastro.already_account() 

    elif q == "N":
        print("Não, não tenho cadastro")
        cadastro.creat_account()