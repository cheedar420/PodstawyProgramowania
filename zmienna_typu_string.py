napis = 'informatyka'

#fragment tekstu:
#1 wycinanie od ... do
print(napis[2:5]) #czyli tak naprawdę od 2 do 4 T_T

#2 wycinanie od .. do co ileś
print(napis[2:10:2])

#3 wycinanie od początku
print(napis[:3])

#4 wycinanie do końca
print(napis[7:])

#5 czytanie do końca
print(napis[::-1])

#6 zawieranie się znaku w słowie
if 'a' in napis:
    print('należy')
else:
    print('nie należy')

