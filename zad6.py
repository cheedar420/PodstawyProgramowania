'''plansza = [
    [3, 8, 1, 9],
    [4, 6, 5, 2],
    [7, 1, 8, 3],
    [2, 9, 4, 6]
]

for i in range(len(plansza)):
    for j in range(len(plansza[0])):
        licznik = 0
        srodkowy = plansza[i][j]
        ''''''if srodkowy < plansza[i - 1][j]:
            licznik += 1
        if srodkowy < plansza[i + 1][j + 1]:
            licznik += 1''''''

        for x in range(i - 1, (i + 1) + 1):
            for y in range(j - 1, (j + 1) + 1):
                if i < 0:
                    x = len(plansza) - 1
                elif x > len(plansza) - 1:
                    x = 0
                if y < 0:
                    y = len(plansza[0]) - 1
                elif y > len(plansza[0]) - 1:
                    y = 0

                czerwony = plansza[x][y]
                if srodkowy < czerwony:
                    licznik += 1
        print(i, j, licznik)
        '''

przeslanie = [[90, 65, 87, 83, 90, 69], [87, 65, 82, 84, 79], [66, 89, 67], [80, 82, 90, 89, 90, 87, 79, 73, 84, 89, 77]]

print(' '.join([''.join(map(chr, s)) for s in przeslanie]))

plansza = [
    [3, 8, 1, 9],
    [4, 6, 5, 2],
    [7, 1, 8, 3],
    [2, 9, 4, 6]
]

# Definiujemy sąsiadów liczby plansza[1][1] na podstawie ilustracji:
sasiedzi = [
    plansza[0][0], plansza[0][1], plansza[0][2], # Góra
    plansza[1][0],                plansza[1][2], # Boki
    plansza[2][0], plansza[2][1], plansza[2][2]  # Dół
]

# Obliczamy sumę tylko tych, które są parzyste (dzielą się przez 2 bez reszty)
suma_parzystych = sum([s for s in sasiedzi if s % 2 == 0])

print(f"Sąsiedzi: {sasiedzi}")
print(f"Suma parzystych sąsiadów: {suma_parzystych}")