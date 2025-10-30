napis = 'informatyka'

#FRAMENT TEKSTU:
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

# ZAWIERANIE SIĘ ZNAKU W SŁOWIE:
if 'x' in napis:
    print('należy')
else:
    print('nie należy')

#ŁĄCZENIE NAPISÓW:
napis2 = napis + 'jestnajlepsza'
print(napis2)

#FUNKCJE ZMIENNYCH TYPU STRING
#szukanie danego fragmentu w tekscie
napis3 = 'matematyka'
index_gdzie_jest = napis3.find('tem')
print(index_gdzie_jest)

napis4 = 'buhhuhbuhhuh'
index_gdzie_jest2 = napis4.find('huh')
index_gdzie_jest3 = napis4.find('huh', index_gdzie_jest2 + 1)
index_gdzie_jest3 = napis4.find('xyn', index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)

if napis4.find('xyn') != -1:
    print('xyn jest w napisie')
else:
    print('xyn nie jest w napisie')

#2 podział tekstu na fragmenty
'''piec_liczb = input('podaj 5 liczb, oddziel je przecinkiem: ')
piec_liczb_po_podziale = piec_liczb.split(',')
print(piec_liczb_po_podziale)
trzecia_liczba = int(piec_liczb_po_podziale[2])
print(trzecia_liczba)'''

#3 łączenie napisów
lista_napisow = ['windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '$'.join(lista_napisow)
print(cale_zdanie)

lista_napisow2 = ['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 = '\n'.join(lista_napisow2)
print(cale_zdanie2)

#4 zliczanie danego znaku w tekscie
napis5 = 'prawdopodobieństwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)