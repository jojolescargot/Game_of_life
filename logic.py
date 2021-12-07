import numpy as np

class GameofLife:

    def __init__(self, size):

        self.A = np.random.randint(low=0, high=2, size=(size, size), dtype=int) # = [[0,0,0,0...,0], [], ... [0,0,0,0...,0]]

        #self.A = np.zeros((size,size), dtype=int)

        #self.A[5, 2:5] = 1

        self.size = size

    def step(self):

        somme_case_adjacente = np.zeros((self.size, self.size), dtype=int)

        for i in range(self.size): # On parcout les lignes
            for j in range(self.size): # On parcourt les colonnes
                somme_case_adjacente[i, j] = self.A[(i-1)%self.size, (j-1)%self.size] + self.A[(i + 1) %self.size, j%self.size]  + self.A[(i + 1)%self.size, (j - 1)%self.size ] + self.A[(i + 1)%self.size, (j + 1)%self.size ] + self.A[i%self.size , (j+1)%self.size ] + self.A[i%self.size , (j-1)%self.size ] + self.A[(i-1)%self.size, (j + 1)%self.size ] +self.A[(i-1)%self.size, j%self.size]

        for i in range(self.size): # On parcout les lignes
            for j in range(self.size): # On parcourt les colonnes
                if self.A[i, j] == 0 and somme_case_adjacente[i, j] == 3:
                    self.A[i, j] = 1
                elif self.A[i, j] == 1 and somme_case_adjacente[i, j] != 2 and somme_case_adjacente[i, j] != 3:
                    self.A[i, j] = 0
        
    