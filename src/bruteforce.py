import numpy as np

def bruteForce (row, col, depth, condition, hasil, koordinat, mJejak, MATRIX, M_ROW, M_COL, DEPTH_MAX, ALL_PATH, ALL_KOORDINAT):
	if(DEPTH_MAX < depth):
		return
	
	elif (depth == DEPTH_MAX):
		ALL_PATH.append(hasil)
		ALL_KOORDINAT.append(koordinat)
		return
	
	if condition: #proses vertikal
		for j in range(M_COL):
			curJejak = np.copy(mJejak)
			if (curJejak[row][j] == 0 ):
				curJejak[row][j] = 1
				curHasil = hasil + MATRIX[row][j] + " "
				bruteForce(row,j,depth+1,False,curHasil, [*koordinat,(row+1,j+1)], curJejak, MATRIX, M_ROW, M_COL, DEPTH_MAX, ALL_PATH, ALL_KOORDINAT)
	else:   #proses horizontal
		for i in range(M_ROW):
			curJejak = np.copy(mJejak)
			if (curJejak[i][col] == 0 ):
				curJejak[i][col] = 1
				curHasil = hasil + MATRIX[i][col] + " "
				bruteForce(i,col,depth+1,True,curHasil, [*koordinat,(i+1,col+1)], curJejak, MATRIX, M_ROW, M_COL, DEPTH_MAX, ALL_PATH, ALL_KOORDINAT)
		
def matchedSequence(ALL_PATH, sequence, bobot_sequence, ALL_KOORDINAT, hasilKoordinat, hasilBobot):
    bobotMax =0
    cocok = False
    j = -1
    for path in ALL_PATH:
		
        j += 1
        bobotNow = 0
        for i in range(len(sequence)):
            curSequence = " ".join(sequence[i])
            if curSequence in path:
                bobotNow = bobotNow + bobot_sequence[i]
                cocok = True
    
        if bobotMax < bobotNow and cocok:
            bobotMax = bobotNow
            koordinat = ALL_KOORDINAT[j]
	
    hasilKoordinat.append(koordinat)
    hasilBobot.append(bobotMax)


        
# Driver code
if __name__ == "__main__":
	
	matrix = [ [ "AA", "BB", "CC", "DD"], 
		        [ "FF", "GG", "HH", "II"], 
		        [ "KK", "LL", "MM", "NN"], 
		        [ "PP", "QQ", "RR", "SS"],]
	visit = [ [ 0, 0, 0, 0], 
		[ 0, 0, 0, 0], 
		[ 0, 0, 0, 0], 
		[ 0, 0, 0, 0],]
	sequence = [["AA", "KK"], ["NN", "SS"]]
	bobot_sequence = [15,20]
	ALL_PATH = []
	ALL_KOORDINAT = []
	koordinatHasil = []
	bobotMax = []
	bruteForce(0,0,0,True,"",[],visit,matrix,4,4,4,ALL_PATH,ALL_KOORDINAT)
	matchedSequence(ALL_PATH, sequence, bobot_sequence, ALL_KOORDINAT, koordinatHasil, bobotMax)
	for bobot in bobotMax:
		print(bobot)
	for koordinat in koordinatHasil:
		for koordinat2 in koordinat:
			print(koordinat2)

