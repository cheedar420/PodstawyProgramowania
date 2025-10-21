 #instr. warunkowa if
#przyklad 1
liczba = int(input('podaj liczbe od 1 do 3'))

if liczba == 1:
    print('jeden')
if liczba == 2:
    print('dwa')
if liczba == 3:
    print('trzy')

#przyklad 2
if liczba == 1:
    print('jeden')
elif liczba == 2:
    print('dwa')
elif liczba == 3:
    print('trzy')

#przyklad 3
liczba = int(input('podaj liczbe całkowitą dodatnią'))

if liczba % 2==0:
    print('parzysta')
if liczba % 3 ==0:
    print('podzielna przez 3')
if liczba > 0:
    print('dodatnia')

#przyklad 4
liczba = int(input('podaj liczbe od 1 do 3'))
if liczba == 1:
    print('jeden')
elif liczba == 2:
    print('dwa')
elif liczba == 3:
    print('trzy')
else:
    print('czytać nie umiesz?')