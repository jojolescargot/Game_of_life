import numpy as np
# import time 

class GameofLife:

    def __init__(self, size):

        self.A = np.random.randint(low=0, high=2, size=(size, size), dtype=int)
        self.size = size

    def step(self):
        # start_time = time.time()
        somme_case_adjacente = np.zeros((self.size, self.size), dtype=int)

        for i in range(self.size): # On parcout les lignes
            for j in range(self.size): # On parcourt les colonnes
                somme_case_adjacente[i, j] = self.A[(i-1)%self.size, (j-1)%self.size] + self.A[(i + 1) %self.size, j%self.size]  + self.A[(i + 1)%self.size, (j - 1)%self.size ] + self.A[(i + 1)%self.size, (j + 1)%self.size ] + self.A[i%self.size , (j+1)%self.size ] + self.A[i%self.size , (j-1)%self.size ] + self.A[(i-1)%self.size, (j + 1)%self.size ] +self.A[(i-1)%self.size, j%self.size]



        self.A = self.A * (somme_case_adjacente == 2) + (somme_case_adjacente == 3) * 1 
        # print( time.time()-start_time )