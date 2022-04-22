print('=====================')
N = input('Rule : (N)  ')
jumlah = 0
Cetak = ""

for i in range(1, int(N)+1):
    if (i == 1):
        Cetak = Cetak + str(i)
        jumlah = i
    elif (i % 15 == 0):
        Cetak = Cetak + ' + ' + 'BMG'
        jumlah = jumlah
    else:
        Cetak = Cetak + ' + ' + str(i)
        jumlah = jumlah + i

print('Result : \n', Cetak, " = ", jumlah)
