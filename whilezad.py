#while zad 1
'''licznik2 = 0
wejscie = ''
print('wprowadzaj liczby, aby zakończyć wpisz q')
while wejscie != 'q':
    wejscie = input('podaj liczbe(lub zakończ): ')

    if wejscie == 'q':
        break
    liczba = float(wejscie)
    if liczba < 2:
        licznik2 = licznik2 + 1

print(f'ilość podanych liczb mniejszych niż 2 wynosi: {licznik2}')'''

#zad 3
n = 20
wynik = 0
while n >= 0:
    n -= 1
    if n % 2 == 1:
        continue
    wynik += n
print(wynik)

#zad 4
i = 10
'''while i >= 1:
    print(i)
    i -= 1'''

for i in range(10, 0, -1):
    print(i)