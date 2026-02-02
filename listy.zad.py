lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'śledź', 'pstrąg']]
#zad 1 a
print(lista2[1][2])
#b
print(list(lista2[3]))

#c
lista3 = lista1[2::2]
print(lista3)
#d
lista2.append(lista2[1] * 3)
print(lista2)
#e
lista1 = lista1 + [9,6,16,-8,7]
print(lista1)
#f
#lista1.sort()
lista1s = sorted(lista1)
print(lista1s)
print(lista1s[0], lista1s[-1])

print(max(lista1), min(lista1))

#g
'''del lista1[4]
print(lista1)'''

#h
del lista1[4:9]

#i
while 2 in lista1:
    lista1.remove(2)

lista1 = [x for x in lista1 if x!= 2]

#j
'''lista3 = [x ** 2 for x in lista1]'''

lista3 = []
for x in lista1:
    lista3.append(x ** 2)
print(lista3)

#k
lista = [178,192, 184, 182, 180, 179, 186, 190, 191,191]
xmin= min(lista)
xmax = max(lista)

listanorm = [(x - xmin) / (xmax - xmin) for x in lista]
print(listanorm)

#l
lista = [123, 89, 5600, 432, 11, 45,900, 12450,1410, 390, 9999]
lidts  = [ for x in lista if x < 1000 or x  > 9999]
           ]