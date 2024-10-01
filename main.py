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
    SP = 10  # Tamanho do torneio

    YB = [
        [4, 18, 19, 10, 0],
        [2, 0, 12, 13, 9],
        [6, 11, 21, 15, 0],
        [0, 17, 3, 14, 8],
        [1, 0, 0, 0, 0]
    ]

    # YB = [[0] * S for _ in range(T)]
    #
    # valores_unicos = list(range(1, CN + 1))
    #
    # random.shuffle(valores_unicos)
    #
    # indice = 0
    # for t in range(T):
    #     for s in range(S):
    #         if indice < len(valores_unicos):
    #             YB[t][s] = valores_unicos[indice]
    #             indice += 1
    #
    # for i, row in enumerate(YB):
    #     # Verifica se a linha já tem um zero
    #     if 0 not in row:
    #         a = random.randint(0, S - 1)
    #         row[a] = 0
    #
    # for linha in YB:
    #     print(linha)

    ga = GeneticAlgorithm(T, S, CN, YB, PS, MP, EN, SP)
    chromosome, fitness = ga.run()

    print("Melhor cromossomo:", chromosome)
    print("Melhor fitness:", fitness)


if __name__ == "__main__":
    main()