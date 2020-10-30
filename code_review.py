# script: Number race
from os import system
from random import randint

# functions


def dices():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    total = d1 + d2

    return [d1, d2, total]


def lanzamientos(n):
    i = 1
    suma=0
    pares=0
    impares=0
    while i <= n:
        dd = dices()
        suma +=  dd[2]
        if(suma % 2) == 0:
            pares+=1
        else:
            impares+=1     
        print("Tiro  Nro: ",i)
        print('d1: ', dd[0])
        print('d2: ', dd[1])
        print('Total: ', dd[2])
        if dd[2] == 12:
            break
        i += 1
        print("--------------------------------")
        key = input('Lanzar nuevamente')
        print("--------------------------------")


    return [suma,pares,impares]



def main():
    veces = int(input('Digite Nuemero de Lanzamientos a Realizar:   '))
    print("--------------------------------")
    if veces >= 1:
        valor = lanzamientos(veces)
        print("---------------------------------------------")
        print('Sumatoria de los Lanzamientos:', valor[0])
        print("---------------------------------------------")
        print('Total Pares Generados:', valor[1])
        print("---------------------------------------------")
        print('Total Impares Generados:', valor[2])
        print("---------------------------------------------")
    else:
        print('Digite un numero valido de Lanzamientos')
        print("--------------------------------")
        main()


# main
system('clear')
main()
key = input('---------Terminar---------')