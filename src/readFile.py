import os
import numpy as np

class FileReader:
    def __init__(self):
        self.matrix_size = []
        self.matrix = []
        self.sequence_size = 0
        self.sequence = []
        self.bobot_sequence = []
        self.buffer = 0
        self.condition = True

    def getDirectory(self):
        # Mengembalikan directory saat ini
        return os.path.dirname(os.path.realpath(__file__))

    def read_file(self, namaFile):
        currentDir = self.getDirectory()
        try:
            with open(os.path.join(currentDir, "..", "test", namaFile), 'r') as f:
                self.condition = True
                content = f.read()
                content = content.split('\n')
                content = [x for x in content if x.strip()]

                self.buffer = int(content[0])

                #membuat matrix size
                matrix_size = content[1].split(' ')
                self.matrix_size.append(int(matrix_size[0]))
                self.matrix_size.append(int(matrix_size[1]))
                
                #membuat matrix
                for i in range (int(matrix_size[1])):
                    matrix = []
                    temp = content[2+i].split(' ')
                    for j in range (int(matrix_size[0])):
                        matrix.append(temp[j])
                    self.matrix.append(matrix)
                #membuat sequence_size
                sequence_size= content[2+int(matrix_size[1])]
                self.sequence_size = sequence_size

                #membuat sequence dan bobot_sequnce
                for i in range (0, int(sequence_size)*2, 2):

                    self.sequence.append(content[3+int(matrix_size[1])+i])
                    self.bobot_sequence.append(int(content[4+int(matrix_size[1])+i]))
        except FileNotFoundError:
            self.condition = False
            print(f"\nFile {namaFile} tidak ditemukan (pastikan ada .txt).")

    def auto(self):
        print("\n====MODE AUTO====")
        print("Silahkan isi data\n")
        token = []
        matrix_size = [[],[]]
        jumlah_token = input("Jumlah token unik:\n")
        token = input(f'masukan token sebanyak {jumlah_token}: Contoh (BD 1C 7A 55 E9)\n')
        token = token.split(' ')
        self.buffer = int(input('Ukuran Buffer: \n'))
        matrix_size = input('Ukuran Matrix: Contoh (6 6) \n')
        matrix_size = matrix_size.split(' ')
        matrix_size = list(map(int, matrix_size))
        sequence_size = int(input('Jumlah Sequence: \n'))
        ukuran_maks_sequences = int(input('Ukuran Maksimal Sequence: \n'))
        self.matrix_size = matrix_size
        self.sequence_size = sequence_size

        self.matrix = np.random.choice(token, size=(matrix_size[1], matrix_size[0]))
        for i in range(sequence_size): 
            cur_sequence = ' '.join(np.random.choice(token, size= np.random.randint(1,ukuran_maks_sequences)))
            while cur_sequence in self.sequence:
                cur_sequence = ' '.join(np.random.choice(token, size= np.random.randint(1,ukuran_maks_sequences)))
            self.sequence.append(cur_sequence)
        self.bobot_sequence = np.random.randint(1,50, size=sequence_size)




if __name__ == "__main__":
    reader = FileReader()
    reader.auto()
    print(reader.buffer)
    print(reader.matrix_size)
    print(reader.matrix)
    print(reader.sequence_size)
    print(reader.sequence)
    print(reader.bobot_sequence)
