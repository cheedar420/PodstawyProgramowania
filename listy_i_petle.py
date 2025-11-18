#jak NIE programowac wielokrotnie powtarzanych czynności
'''a = float(input('podaj liczbe'))
b = float(input('podaj liczbe'))
c = float(input('podaj liczbe'))
d = float(input('podaj liczbe'))
e = float(input('podaj liczbe'))

suma = (a + b + c + d + e)
print(suma)'''
#jak robic:
'''liczba = 0
suma = 0

for u in range(5):
    liczba = float(input('podaj liczbe'))      #np 3
    suma = suma + liczba                       #wiec suma = 3
    print(suma)'''

#1. listy
lista = ['poggers', 56, [6, 7], 4.56, [[5, 6], 1]]
print(lista[2][1])
print(lista[4][0][1])

#2. listy i pętle
lista2 = ['kot', 'pies', 'mati', 'foka']


# Pętla for:
#-> wyciaga dane z listy (jedna po drugiej)
#-> wykonuje się tyle razy ile elementów ma lista
for z in lista2:
    print(z)

#Pętla, która wykona sie 3 razy
lista3 = [420, 777, 7]
for n in lista3:
    print('ok')

#Pętla, która wykona sie 1000 razy
lista4 = [0] * 1000
for i in lista4:
    print('yippie')

#3. Generatory i pętle
przedzial = range(1, 10) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

for i in przedzial:
    print(i, end= ' ')

#pętla która wykona się 10 razy(best)
for i in range(10): #od 0 do 9 - wiec 10 razy, range(0,10)
    print(i, end= ' ')

lista5 = [0]
lista5.append(5)
print(lista5)

#inf-inity
'''for i in lista5:
    print('hello world')
    lista5.append(0)'''

#4. Pętla while
liczba = 5
while liczba > 0:
    print(liczba)
    liczba = liczba - 1
