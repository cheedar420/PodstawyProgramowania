lista2d = [
    [5,2,8,5,1],
    [3,8,2,9,5],
    [1,4,4,2,7],
    [6,3,9,1,4],
    [8,2,5,6,3]
]
zbior = set()
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior.add(element)
print(zbior)

zbiorcaly = set()
for x in lista2d:
    zbior2 = set(x)
    zbiorcaly.union(zbior2)
print(zbiorcaly)

#zad1.2
lista1d = []
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        lista1d.append(element)

lista1dzbior = set(lista1d)
for e in lista1dzbior:
    print(e, lista1d.count(e))