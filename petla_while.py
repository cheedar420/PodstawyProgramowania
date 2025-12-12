#Pętla while - przykłady

'''liczba = 120
licznik = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0:   #tak długo jak liczba jrest dodatnia, pętla się wykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)'''

#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć: ')
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć: ')
print(licznik)'''

#Zadanie 2.

popr_haslo = 'maslo'
haslo = input('Podaj hasło: ')
proba = 1
while haslo != popr_haslo and proba <= 5:
    print('wpisz haslo jeszcze raz: ')
    haslo = input('podaj poprawne hasło: ')
    proba = proba + 1
if haslo == popr_haslo:
    print('udało ci sie')
else:
    print('nie wejdziesz do systemu T_T')