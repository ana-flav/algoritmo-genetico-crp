from genetic_algorithm import GeneticAlgorithm

import matplotlib.pyplot as plt


def main():
    T = 4  # Número de tiers
    S = 4  # Número de stacks
    CN = 12  # Número de contêineres
    PS = 100  # Tamanho da população
    MP = 0.05  # Taxa de mutação
    EN = 300  # Número de evoluções
    SP = 3  # Tamanho do torneio

    YB = [
        [0, 12, 0, 9, 13],
        [3, 8, 0, 5, 10],
        [7, 6, 0, 1, 4],
        [11, 2, 0, 14, 15]
    ]

    ga = GeneticAlgorithm(T, S, CN, YB, PS, MP, EN, SP)
    chromosome, fitness = ga.run()

    print("Melhor cromossomo:", chromosome)
    print("Melhor fitness:", fitness)


if __name__ == "__main__":
    main()