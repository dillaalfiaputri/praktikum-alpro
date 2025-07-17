# CREATE -- > bracket, constructor
myTuple = ('Alif',83)
myTuple2 = tuple(('Alif','Alfy'))

# OREDERED -- > urutan data tetap
print('Data :',myTuple)
print('Data :',myTuple2)
print('-------------------------')

# DUPLICATE -- > data ganda
myTuple = ('Alif',83,83)
myTuple2 = tuple(('Alif','Alfy','Alfy'))
print('Duplikat :',myTuple)
print('Duplikat :',myTuple2)
print('-------------------------')

# INDEX -- > 0
# ex: tampilkan no. index angka 83
# myIndex = myTuple.index(83)
# print('Index angka 83 :',myIndex)
# print('

# UNCHANGEABLE -- > tidak dapat dirubah
# ex: ubah data index 1 dengan 90
myTuple[1] = 90
print('Hasil Edit :',myTuple)
print('-------------------------')