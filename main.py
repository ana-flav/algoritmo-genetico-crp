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
    # [13, 3, 12, 16, 0],
    # [1, 0, 10, 2, 12],
    # [11, 0, 14, 10, 12],
    # [7, 19, 20, 0, 11],
    # [8, 12, 19, 10, 0]
    # ]

    YB = [[0] * S for _ in range(T)]

    valores_unicos = list(range(1, CN + 1))

    random.shuffle(valores_unicos)

    indice = 0
    for t in range(T):
        for s in range(S):
            if indice < len(valores_unicos):
                YB[t][s] = valores_unicos[indice]
                indice += 1

    for i, row in enumerate(YB):
        # Verifica se a linha já tem um zero
        if 0 not in row:
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