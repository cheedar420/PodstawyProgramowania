login = 'meow'
haslo = 'woof'

print((login == 'meow') ^ (haslo == 'woof'))
#wtedy druknie false ze wzgledu na operator ^

liczba1 = float(input('podaj pierwsza liczbę'))
liczba2 = float(input('podaj drugą liczbę'))
dzialanie = str(input('podaj dzialanie(dodawanie,odejmowanie, mnożenie, dzielenie, potęgowanie'))
znak_dzialania = ''
wynik = None

if dzialanie == 'dodawanie':
    wynik = liczba1 + liczba2
    znak_dzialania = '+'

elif dzialanie == 'odejmowanie':
    wynik = liczba1 - liczba2
    znak_dzialania = '-'
elif dzialanie == 'mnożenie':
    wynik = liczba1 * liczba2
    znak_dzialania = '*'
elif dzialanie == 'dzielenie':
    if liczba2 == 0:
        print('nie mozna dzielic przez 0')
        exit()
    wynik = liczba1 / liczba2
    znak_dzialania = '/'
elif dzialanie == 'potęgowanie':
    wynik = liczba1 ** liczba2
    znak_dzialania = '**'

else:
    print('wprowadzowno nieprawidlowe dzialanie')
    exit()

if wynik is not None:
    print(f"wynik działania: {liczba1} {znak_dzialania} {liczba2} = {wynik}")


