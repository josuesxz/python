import random as sensor
import datetime as dt

dia = dt.datetime.now()
d = str(dia.day) +'/' + str(dia.month) + '/' + str(dia.year) #chamamos a função apos declar e definimos o que queremos mostrar

minuto = 0
add = 0
hora = 0
with open("dados_a.txt", 'a') as data:
    data.write('Dia ' + d + '\n') #no arquivo com tudo ja formatado vai nos dar bom embasamento

while True: #1 dia
    carros = sensor.randint(0, 484) #numeros de carros que podem passar por minuto
    add = carros + add
    minuto = minuto + 1 # "contador" de minutos
    if minuto == 60: break #nova analise de media a cada hora
    Media = add/minuto
    a = round(Media, 2) #arredonda em 2 casa decimais
    print(a)
    hora = hora + 1
    with open("dados_a.txt", 'a') as coleta:
        coleta.write(str(a) + '\n')
    if hora == 12: break # fica monitorando por 12 horas até ser reativado no dia seguinte

print("Fim do monitoramento")