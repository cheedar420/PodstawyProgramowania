oceny = {'matematyka': 3, 'fizyka': 5, 'polski': 4}
#klucze: 'matematyka, fizyka itd
#wartości: 3, 5, 4

#1 dostawanie sie do wartości pod danym kluczem
print(oceny['fizyka']) #pobieramy wartosc przypisana do klucza fizyka

#2 modyfikacja wartości pod kluczem
oceny['polski'] = 5
print(oceny['polski'])

#3 dodawanie klucza do słownika
oceny['historia'] = 6
print(oceny)

#4 sklejanie slownika z listy kluczy i listy wartosci:
klucze = ['Bitwa pod Grunwaldem', 'Chrzest Polski', 'III Rozbiór Polski']
wartosci = [1410, 966, 1795]

'''for k, w zip(klucze, wartosci):
    print(k, w)'''
slownik={}
for i in range(len(wartosci)):
    '''print(klucze[i], wartosci[i])'''
    slownik[klucze[i]]  = wartosci[i]
print(slownik)

slownik2= dict(zip(klucze, wartosci))
print(slownik2)

slownik3 = dict(janusz = 23, maria = 67, mati = 17)
print(slownik3)

#5 usuwanie klucza ze slownika
del oceny['fizyka']
print(oceny)

#6 chodzenie w petli po słowniku:
for k in oceny:
    print(k, oceny[k])

for i in oceny.items():
    print(i)