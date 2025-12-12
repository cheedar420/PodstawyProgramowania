#Tabliczka mnożenia
for i in range(1, 21):
    for j in range(1, 21):
        print(i * j, end = '\t')
    print()

#Trójkąt prostokątny
'''n = int(input('Wysokość strójkąta = '))
for x in range(n):
    for y in range(x + 1):
        print('*', end = '')
    print()'''

n = int(input('Wysokość strójkąta = '))
for x in range(n):
    print('x' * (x + 1))

#Trójkąt równoramienny dowolny
n = int(input('Wysokość strójkąta = '))
spacja = n - 1
gwiazdki = 1


for i in range(n):
    print(' ' * spacja, end = '')
    print('x' * gwiazdki)
    spacja = spacja - 1
    gwiazdki = gwiazdki + 2