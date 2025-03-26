# input
print('HASIL UJIAN' )
nilai = int(input('Masukkan nilai : '))

# proses
if nilai >= 70 :
    status = 'Lulus'
    if nilai >= 80 :
       predikat = 'Memuaskan'
    else :
        predikat = 'Cukup'
else :
    status = 'Gagal'
    predikat = 'Kurang'

#output
print('Status : ',status)
print('predikat : ',predikat)
print('------------------')