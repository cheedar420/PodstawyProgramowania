'''n = int(input('podaj liczbe calk dodatnia'))
silnia = 1
for h in range(1, n + 1):
    silnia = silnia * h

print(f'silnia wynosi {silnia})'''

lista = [4, 12, 8, 1, 5, 6, 3]
n = len(lista)
pary = 0
for i in range(n):
    x = lista[i]
    for j in range(n):
        y = lista[j]

        if j != i:
            if (x + y)%3 == 0:
                pary += 1

print(lista)
print(pary)

