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

# Pobieramy od użytkownika rozmiar tablicy
n = int(input("Podaj liczbę wierszy i kolumn: "))

# Zewnętrzna pętla odpowiada za wiersze
for i in range(n):
    # Wewnętrzna pętla odpowiada za kolumny w danym wierszu
    for j in range(n):
        # Obliczamy wartość jako sumę indeksów
        wynik = i + j

        # Wypisujemy wynik.
        # end=" " sprawia, że liczby są w jednej linii.
        # f"{wynik:<3}" dba o równe odstępy (wyrównanie do 3 znaków).
        print(f"{wynik:<3}", end=" ")

    # Po wypisaniu wszystkich kolumn w wierszu, przechodzimy do nowej linii
    print()
