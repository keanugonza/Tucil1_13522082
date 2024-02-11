import numpy as np
import time
import os

def bruteForce (row, col, depth, condition, hasil, koordinat, mJejak, MATRIX, M_ROW, M_COL, BUFFER, ALL_PATH, ALL_KOORDINAT):
	if(BUFFER < depth):
		return
	
	elif (depth == BUFFER):
		ALL_PATH.append(hasil)
		ALL_KOORDINAT.append(koordinat)
		return
	
	if condition: #proses vertikal
		for j in range(M_COL):
			curJejak = np.copy(mJejak)
			if (curJejak[row][j] == 0 ):
				curJejak[row][j] = 1
				curHasil = hasil + MATRIX[row][j] + " "
				bruteForce(row,j,depth+1,False,curHasil, [*koordinat,(j+1,row+1)], curJejak, MATRIX, M_ROW, M_COL, BUFFER, ALL_PATH, ALL_KOORDINAT)
	else:   #proses horizontal
		for i in range(M_ROW):
			curJejak = np.copy(mJejak)
			if (curJejak[i][col] == 0 ):
				curJejak[i][col] = 1
				curHasil = hasil + MATRIX[i][col] + " "
				bruteForce(i,col,depth+1,True,curHasil, [*koordinat,(col+1,i+1)], curJejak, MATRIX, M_ROW, M_COL, BUFFER, ALL_PATH, ALL_KOORDINAT)
		
def matchedSequence(ALL_PATH, sequence, bobot_sequence, ALL_KOORDINAT, hasilKoordinat, hasilBobot, hasilPath):
    bobotMax =0
    cocok = False
    j = -1
    for path in ALL_PATH:
		
        j += 1
        bobotNow = 0
        for i in range(len(sequence)):

            if sequence[i] in path:
                bobotNow = bobotNow + bobot_sequence[i]
                cocok = True
    
        if bobotMax < bobotNow and cocok:
            path_final = path
            bobotMax = bobotNow
            koordinat = ALL_KOORDINAT[j]
	
    hasilBobot.append(bobotMax)
    if bobotMax != 0:
        hasilKoordinat.append(koordinat)
        hasilPath.append(path_final)


def solusi(mJejak, MATRIX, M_ROW, M_COL, BUFFER,sequence,bobot_sequence):
	start = time.time()
	ALL_PATH = []
	ALL_KOORDINAT = []
	PATH =[]
	KOORDINAT=[]
	for i in range (1,BUFFER+1):
		bruteForce(0,0,0,True,"",[],mJejak,MATRIX,M_ROW,M_COL,i,ALL_PATH,ALL_KOORDINAT)
		PATH += ALL_PATH
		KOORDINAT += ALL_KOORDINAT
	koordinatHasil = []
	bobotMax = []
	hasilPath = []
	matchedSequence(ALL_PATH, sequence, bobot_sequence, ALL_KOORDINAT, koordinatHasil, bobotMax,hasilPath)
	end = time.time()

	for bobot in bobotMax:
		print(bobot)
	if bobot != 0:
		print(hasilPath[0])
		for koordinat in koordinatHasil:
			for koordinat2 in koordinat:
				print(koordinat2)
	
	waktu_ms = "{:.3f}".format((end- start)*1000)
	waktu_detik = "{:.3f}".format(end- start)
	print(f'\nWaktu dibutuhkan: {waktu_ms} ms / {waktu_detik} detik.')
	
	save = input('\nApakah anda ingin menyimpan jawaban (y/n)?\n')

	if (save=='y' or save =='Y'):
		namaSave = input('Masukan / buat nama file untuk menyimpan: ')
		currentDir = os.path.dirname(os.path.realpath(__file__))
		with open(os.path.join(currentDir, "..", "test", f"{namaSave}.txt"), 'w') as f:
			f.write(str(bobot) + '\n')
			if bobot != 0:
				f.write(str(hasilPath[0]) + '\n')
				for koordinat in koordinatHasil:
					for koordinat2 in koordinat:
						f.write(str(koordinat2) + '\n')
			f.write(f'\nWaktu dibutuhkan: {waktu_ms} ms / {waktu_detik} detik.')
		print(f'\nTelah tersimpan di file "{namaSave}"')
	else:
		print('\nJawaban tidak tersimpan!!!')			
        
# # Driver code
# if __name__ == "__main__":
# 	matrix = [ [ "7A", "55", "E9", "E9", "1C", "55"], 
# 		        ['55', '7A', '1C', '7A', 'E9', '55'], 
# 		        ['55', '1C', '1C', '55', 'E9', 'BD'], 
# 		        ['BD', '1C', '7A', '1C', '55', 'BD'],
# 				['BD', '55', 'BD', '7A', '1C', '1C'],
# 				['1C', '55', '55', '7A', '55', '7A']]
# 	visit = [ [ 0, 0, 0, 0,0,0], 
# 		[ 0, 0, 0, 0,0,0], 
# 		[ 0, 0, 0, 0,0,0], 
# 		[ 0, 0, 0, 0,0,0],
# 		[ 0, 0, 0, 0,0,0],
# 		[ 0, 0, 0, 0,0,0]]
# 	sequence = ['BD E9 1C', 'BD 7A BD', 'BD 1C BD 55']
# 	bobot_sequence = [15,20,30]
# 	print(sequence)
# 	print(bobot_sequence)

