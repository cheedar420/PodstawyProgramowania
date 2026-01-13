# listy a napisy
napis = 'informatyka'

'''lista = []
for l in napis:
    lista.append(l)
print(lista)'''

lista = list(napis)
print(lista)

#zakres i lista
zakres = range(3,10, 2)
lista2 = list(zakres)
print(lista2)

#indeksowanie elementów listy
lista3 = ['meow', 66, 'efnn', [56, 3, 6, 9]]
print(lista3[1:3]) #wycinanie fragmentu listy
print(lista3[2][3]) #obsluga listy zagnieżdżonej
print(lista3[3][::2])#obsluga listy zagnieżdżonej

#powielanie listy(dodawanie list
lista4 = ['meow']
lista5 = ['rtwttwtwy']
lista6 = lista4 + lista5
print(lista6)

lista4.extend(lista5)
print(lista4)

#"mnozenie" listy przez index
lista9 = [0] * 1000
'''lista10 = [lista9] * 1000
print(lista10)'''

#Sortowanie i odwracanie listy
lista10 = [9,3,5,6,2]
#lista10.sort()
lista10.reverse()
print(lista10)

#Wyrażenia listowe/listy składane
lista11 = list(range(1, 11))
lista11kwadraty = [x ** 2 for x in lista11 if x % 2 == 0]
print(lista11kwadraty)

#Usuwanie elementów listy:
#na bazie jego wartości
lista12 = [2,9,3,4,5,2,2]
#lista12.remove(4)
while 2 in list12:
    lista12.remove(2)
print(lista12)

#na bazie indeksu
lista13 = [5,1,8,3,9,10]
del lista13[2] #indeks 2
print(lista13)