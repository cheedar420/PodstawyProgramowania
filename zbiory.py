zbior = {5, 6, 6, 1, 1, 5, 9}
print(zbior)

zbior2 = {'kot', 'pies' , 'kot', 'pies', 'meow'}
print(len(zbior2))

A = set(range(0, 20, 2)) # 0, 2, 4, 6, 8, 10, 12, 16, 18
B = {1, 2, 3, 4, 6, 12}

#suma zbiorow
sumaAB = A.union(B)
print(sumaAB)

sumaAB2 = set(list(A) + list(B))
print(sumaAB2)

#czesc wspolna
iloczynAB = A.intersection(B)
print(iloczynAB)

#roznica
roznicaAB = A.difference(B)
print(roznicaAB)

#dodawanie elementu do zbioru:
c = {1, 7, 4, 5}
c.add(10)
print(c)
