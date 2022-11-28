# Projeto de conversor de temperatura 
# Usuário define qual escala e qual valor irá ser digitado
# A saída retorna o valor convertido nas demais escalas
# Celsuius(C), Farenheit(F), Kelvin(K), Rankine(Ra)

# Josué da Silva Souza Filho - 2115180016
# 03/07/2022

while(True):
    cnt = str(input("\nContinue?\nDigite s/n: ")).upper()   # Comando se decide continuar a testar ou se deseja parar o código
    if cnt == "N": break
    elif cnt == "S": print("Digite as informações")
    else: 
        print("Digite um comando válido")
        break

    print("\nC - celcius\t F - Farenheit\nK - Kelvin\t Ra - Rankine") #No console demonstrará qual as escalas disponíveis 
    escSelecionada = str(input("\nDigite a escala desejada: ")).upper()
    tempSelecionada = float(input("Digite a temperatura: "))

    def celsius(): #Comando partindo do celsius
        F = tempSelecionada*(9/5) + 32
        K = tempSelecionada + 273.15
        Ra = (9/5)*tempSelecionada + 491.
        print("A temperatura escolhida foi", tempSelecionada, "°",escSelecionada, "sendo assim:")
        print(round(F, 2),"°F", round(K, 2),"K", round(Ra, 2),"°Ra")

    def farenheit(): #Comando partindo de farenheit
        C = (tempSelecionada - 32) * (5/9)
        K = C + 273.15
        Ra = tempSelecionada + 459.67
        print("A temperatura escolhida foi", tempSelecionada, "°",escSelecionada, "sendo assim:")
        print(round(C, 2),"°C", round(K, 2),"K", round(Ra, 2),"°Ra")

    def kelvin(): #Comando partindo de kelvin
        C = tempSelecionada - 273.15
        F = (9/5)*C + 32
        Ra = tempSelecionada * (9/5)
        print("A temperatura escolhida foi", tempSelecionada, escSelecionada, "sendo assim:")
        print(round(C, 2),"°C", round(F, 2),"°F", round(Ra, 2),"°Ra")

    def rankine(): #Comando partindo de rankine
        C = (tempSelecionada - 491.67)*(5/9)
        F = (9/5)*C + 32  
        K = C + 273.15
        print("A temperatura escolhida foi", tempSelecionada, "°Ra", "sendo assim:")
        print(round(C, 2), round(F, 2), round(K, 2))
    
    if escSelecionada == "C": #Início da tomada de decisão do código para converter para as seguintes escalas
        celsius()
    elif escSelecionada == "F":
        farenheit()
    elif escSelecionada == "K":
        kelvin()
    elif escSelecionada == "RA":
        rankine()
    else: 
        print("Digite uma escala válida")
        break

print("ERROR - FIM")
# Se o usuário decidir não rodar mais, ou qualquer comando fora do esperado ele para e o usuário deve reiniciar o código