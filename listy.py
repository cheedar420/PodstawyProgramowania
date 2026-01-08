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