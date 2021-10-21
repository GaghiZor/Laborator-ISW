import numpy

ss = raw_input().strip().split()
ss = [int(i) for i in ss]

myArr = numpy.array(ss)
print(numpy.reshape(myArr, (3, 3))) # Se face conversia de la un array 1x9 la o matrice 3x3
