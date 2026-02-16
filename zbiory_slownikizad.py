'''lista2d = [
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
    print(e, lista1d.count(e))'''

slowa = [
"LETTER",
"BALLOON",
"SUCCESS",
"HAPPY",
"COFFEE",
"BOOKKEEPER",
"ASSESS",
"MISSISSIPPI",
"ADDRESS",
"TOOLBOX"
]
ilosc = []
slowaset = set(slowa)
lslowa = len(slowaset)
for i in range(lslowa):
    iset = list(slowaset)[i]
    iiset = set(iset)
    liczba = len(iiset)
    ilosc.append(liczba)
print(ilosc)

maxx = ''
maxlrl = 0
for x in slowa:
    xbior = set(x)
    lrl = len(xbior)
    if lrl > maxlrl:
        maxlrl = lrl
        maxx = x
print(maxx)

#sp 2

maxslowo = max(slowa, key = lambda x: len(set(x)))
print(maxslowo)

#zad 2.2


zbior = set()
for x in slowa:
    for y in x:
        zbior.add(y)
print(zbior)

for l in zbior:
    lista = []
    for s in slowa:
        if l in s:
            lista.append(s)
    print(f'{l}: {lista}')