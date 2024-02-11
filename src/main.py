import readFile
import bruteforce
import numpy as np
import time

print('Apakah anda akan menggunakan file atau auto?')
print('1. File')
print('2. Auto')


pilihan =  int(input('Pilihan: '))
while pilihan <0 or pilihan>2:
    pilihan =  int(input('Masukan pilihan dengan benar: '))

if pilihan == 1:
    namaFile = input('\nPastikan file ada dalam folder "test".\nContoh nama file (soal.txt).\nMasukan nama file anda: ')
    reader = readFile.FileReader()
    reader.read_file(namaFile)
    while not (reader.condition) :
        namaFile= input('Masukan nama file dengan benar: ')
        reader.read_file(namaFile)
    print('\n\n==========FILE DITEMUKAN==========')
    print('\nJawaban: ')
    mJejak = np.zeros((reader.matrix_size[1],reader.matrix_size[0]))
    bruteforce.solusi(mJejak, reader.matrix, reader.matrix_size[1], reader.matrix_size[0], reader.buffer, reader.sequence, reader.bobot_sequence)
    

elif pilihan == 2:
    reader = readFile.FileReader()
    reader.auto()
    print("==============================================")
    print('\nMatrix: ')
    for i in range(len(reader.matrix)):
        print(reader.matrix[i])
    print('\nSequences (unik): ')
    for i in range(len(reader.sequence)):
        print(str(reader.sequence[i]) + '     (bobotnya:' + str(reader.bobot_sequence[i]) + ')')
    mJejak = np.zeros((reader.matrix_size[1],reader.matrix_size[0]))
    print('\nJawaban:')
    bruteforce.solusi(mJejak, reader.matrix, reader.matrix_size[1], reader.matrix_size[0], reader.buffer, reader.sequence, reader.bobot_sequence)