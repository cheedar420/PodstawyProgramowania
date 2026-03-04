#zad1 a)
from operator import truediv


def vsuma(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]
wynik = vsuma(u, v)
print(wynik)

def viloczyn(u,v):
    il = []
    for i in range(len(u)):
        iloczyn = u[i] * v[i]
        il.append(iloczyn)
    return sum(il)

wynik2 = viloczyn(u, v)
print(wynik2)

#zad 2.1
def czyanagramy(s1, s2):
    return sorted(s1) == sorted(s2) #wynik porownania = wartosc logiczna
print(czyanagramy('kamils', 'slimak'))

def jakitrojkat(a, b, c):
    if a+b+c > 2 * max([a,b,c]):
        if a ** 2 + b ** 2 + c ** 2 == max([a, b, c]) ** 2:
            print('prostokatny')
        elif a ** 2 + b ** 2 + c ** 2 > max([a, b, c]) ** 2:
            print('ostrokątny')
        elif a ** 2 + b ** 2 + c ** 2 < max([a, b, c]) ** 2:
            print('rozwartokątny')

jakitrojkat(13, 5, 12)

#zad 2
lista1 = ['kot', 'pies' , 'mysz']
lista2 = [lista1, lista1 * 3, 4, 8, 9, [10,11,12,13,1]]

zagniezdzona = lista2[5][1:4]
print(zagniezdzona)

#zad3
liczby = ['123', '56', '7890', '59', '456', '822']
listaliczb = list(map(int, liczby))
print(sum(listaliczb))

#zad4
suma = 0
lista2d =
for i in range(len(lista2d)):
    element = lista2d[i][i]
    suma+= element
print(suma)

f = fghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfghfgh
 #2. 4 2.5 2.6 2.7 2.8