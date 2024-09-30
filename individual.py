import random

class Individual:
    def __init__(self, GN, S):
        self.chromosome = [random.randint(0, S - 1) for _ in range(GN)]
        self.fitness = None

    def evaluate_fitness(self, T, S, CN, GN, YB):
        IGC = 0  
        RN = 0  

        YB_copy = [row[:] for row in YB]
        
        for k in range(1, CN + 1):
            indT, indS = -1, -1 

            for i in range(T):
                for j in range(S):
                    if YB_copy[i][j] == k:
                        indT, indS = i, j
            
            for i in range(indT):
                if YB_copy[i][indS] != 0: 

                    CC = YB_copy[i][indS]  
                    find = False  

                    while not find:
                        relS = self.chromosome[IGC] 
                        if relS != indS:  
                            if YB_copy[0][relS] == 0:
                                find = True
                                RN += 1 
                                maxT = 0
                                IGC += 1
                                for ii in range(T - 1, -1, -1): 
                                    if YB_copy[ii][relS] == 0: 
                                        maxT = ii  
                                        break
                                YB_copy[maxT][relS] = CC
                                YB_copy[i][indS] = 0  
                            else:
                                IGC += 1
                        else:
                            IGC += 1

            # verificação nova
            if YB_copy[indT][indS] == k:  
                YB_copy[indT][indS] = 0 

        self.fitness = RN
        # print(f"Fitness calculado: {RN}")
        return RN  # Retornar o número de relocations
 
