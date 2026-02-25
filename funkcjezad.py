#zad1 a)
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
