#Pętla while - przykłady

'''liczba = 120
licznik = 0

#W pętli while podajemy warunek TRWANIA pętli
while liczba > 0:   #tak długo jak liczba jrest dodatnia, pętla się wykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)'''
import time

#Zadanie 1.
'''x = input('Podaj liczbę lub q aby zakończyć: ')
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik = licznik + 1
    x = input('Podaj liczbę lub q aby zakończyć: ')
print(licznik)'''

#Zadanie 2.

'''popr_haslo = 'maslo'
haslo = input('Podaj hasło: ')
proba = 1
while haslo != popr_haslo and proba <= 5:
    print('wpisz haslo jeszcze raz: ')
    haslo = input('podaj poprawne hasło: ')
    proba = proba + 1
if haslo == popr_haslo:
    print('udało ci sie') 
else:
    print('nie wejdziesz do systemu T_T')'''

'''from random import randint
#zad6
wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2)>= 2):
    akcja += 1
    druzyna = randint(1,2)
    if druzyna == 1:
        wynik1 += 1
    if druzyna == 2:
        wynik2 +=1

    print(f'akcja:{akcja}')
    print(f'{wynik1}:{wynik2}')
    time.sleep(1)

if wynik1 > wynik2:
    print('wygrywa: drużyna 1')
else:
    print('wygrywa: drużyna 2')'''

'''#zad 7
liczba = int(input('podaj liczbe: '))
while liczba > 0:
    cyfra = liczba % 10
    liczba = liczba // 10
    print(cyfra, end = '')'''

#zad 8
'''liczba = int(input('podaj liczbe'))
d = 2
ileczyn = 0
ilerczyn = 0
while liczba > 1:
    if liczba % d== 0:
        ilerczyn += 1
    while liczba% d == 0:
        liczba = liczba // d
        ileczyn += 1
    d += 1
print(ileczyn)
print(ilerczyn)
'''
from random import randint
#zad 5
x, y = 0, 0
ruchy= ['p'] * 10 + ['d'] * 5 + ['l'] * 5 + ['g'] * 10 + ['q']

while True:
    #ruch = input('podaj ruch(g,d,l,p) - aby zakończyć (q): ')
    ruch = ruchy[randint(0, len(ruchy) - 1)]
    if ruch == 'q':
        print('koniec gry')
        break
    elif ruch == 'g':
        if y < 9:
            y += 1
        else:
            print('ruch niemożliwy')
    elif ruch == 'd':
        if y > 0:
            y -= 1
        else:
            print('ruch niemożliwy')
    elif ruch == 'l':
        if x > 0:
            x -= 1
        else:
            print('ruch niemożliwy')
    elif ruch == 'p':
        if x < 9:
            x += 1
        else:
            print('ruch niemożliwy')
    else:
        print('nieznany ruch')
    print(f'({x}, {y})')
    time.sleep(0.5)