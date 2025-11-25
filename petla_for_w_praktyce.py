#zad 15.(pdf)
'''X = list(range(0, 103, 3)) #od 0 do 102 co 3
print(f'x\ty')
for x in X:
    y = 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')'''

#a.
'''print(f'x\ty')
for x in range(0,103, 3):
    y = 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')'''

#b.
print(f'x\t\ty')
for x in range(-30, 61):
    x = x/10
    y = 0.5 * x + 3
    #print(x, y)
    if x>=0:
         print(f'{x}\t\t{y}')
    else:
        print(f'{x}\t{y}')

#zad 16.
lista1 = list(range(3, 31, 3))
lista2 = list(range(11, 111, 11))
lista3 = list(range(13, 131, 13))

#sp.1
for x, y, z in zip(lista1, lista2, lista3):
    print(f'{x}\t{y}\t{z}')

#sp.2
for i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')

lista = [10,16,89,59]
#another classisc
#1. chodzenie bezposrednio po elementavh listy(do zmiennej b trafiaja bezposrednio elementy listy
for b in lista:
    print(b)

#2. Chodzenie po liście z użyciem indeksów
#2.1 co to jest indeks?(miejsce elementu na liscie
#lista[2]
#2 - indeks
#lista[2] - element znajdujacy sie pod indeksem 2 =89

#2.2
for k in range(len(lista)): #range(0, 4)
    print(lista[k])

#Zad 17.
n = int(input('podaj ilość liczb'))
suma = 0

for x in range(n):
    liczba = int(input('podaj liczbę'))
    suma = suma + liczba

print(suma)