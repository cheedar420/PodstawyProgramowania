#zad1 POWIEL TYLE RAZY
'''s = input('podaj napis')
n = int(input('podaj liczbe calkowita dodatnia'))
powielacz = len(s) // n
wynik = s * powielacz
print(wynik)'''

#zad2 MAKETRANS TRANSLATE
napis = 'matematyka'
slownik = str.maketrans('aey', 'AEY')
modnapis = napis.translate(slownik)
print(modnapis)

#zad3 COUNT
s = 'MlemMlEmMleM'
c = 'm'

lowers = s.lower()
ilerazy = lowers.count(c)
print(ilerazy)

#zad 4. REPLACE
s1 = 'weeUNIweeUNIUNIUNI'
s2 = 'UNI'
s3 = s1.replace(s2, '')
print(s1)
print(s3)

#ZAD 5 SORTED()
w1 = 'KABA'
w2 = 'BAKA'
w1sortedstring = sorted(w1)
w2sortedstring= sorted(w2)

w1sorted = ''.join(w1sortedstring)
w2sorted = ''.join(w2sortedstring)
if w1sorted == w2sorted:
    print('podane slowa sa anagramami')
else:
    print('podane slowa nie sa anagramami ')