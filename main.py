import random

from genetic_algorithm import GeneticAlgorithm

import matplotlib.pyplot as plt


def main():
    # for iteration in range(1, 5):
    T = 5 # Número de tiers
    S = 5  # Número de stacks
    CN = T * S - (T - 1)  # Número de Containers
    PS = 150  # Tamanho da população
    MP = 0.05  # Taxa de mutação
    EN = 25  # Número de evoluções
    SP = 15  # Tamanho do torneio

    # YB = [
    #     [1, 0, 20, 50, 53, 49],
    #     [5, 0, 6, 7, 8, 9],
    #     [0, 1, 2, 0, 3, 4]
    # ]

    YB = [[0] * S for _ in range(T)]

    for t in range(T):
        for s in range(S):
            temp = random.randint(0, CN)
            YB[t][s] = temp

    for i, row in enumerate(YB):
        if 0 in row:
            pass
        else:
            a = random.randint(0, S - 1)
            row[a] = 0

    for linha in YB:
        print(linha)

    ga = GeneticAlgorithm(T, S, CN, YB, PS, MP, EN, SP)
    chromosome, fitness = ga.run()

    print("Melhor cromossomo:", chromosome)
    print("Melhor fitness:", fitness)


if __name__ == "__main__":
    main()