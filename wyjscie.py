# 1. co mozna wyświetlać printem?
print(9)
print((2 + 2) * 2)
x= 34
print(x)
print('informatyka')
print(round(2.234, 2))
print(2 == 3 and 1 > 0)
print([6,9,2,5])

#2. formatowanie wyświetlania tekstu
imie = input('podaj imię')
nazwisko = input('podaj nazwisko')
wiek = int(input('podaj wiek'))

#sposób 1(jak nie robić)
'''print('witaj '+ imie + ' ' + nazwisko + '. masz ' + str(wiek) + ' lat. za 5 lat będziesz mieć ' + str(wiek + 5) + ' lat.')'''

#sposób 2
print(f'witaj {imie} {nazwisko}. masz {wiek} lat. za 9 lat bedziesz mieć {wiek + 9} lat.')
liczba = 4.1234
print(f'kwota = {liczba: 0.3f}')

#sposób 3.1
print('witaj {} {}. masz {} lat. za 5 lat będziesz mieć {} lat.'.format( imie, nazwisko, wiek, wiek + 5))

#sposób 3.2
print('witaj {1} {0}. masz {3} lat. za 5 lat bedziesz mieć {2} lat.'.format(nazwisko, imie, wiek + 5, wiek))

