from matplotlib import pyplot as plt

from individual import Individual
import random

class GeneticAlgorithm:
    def __init__(self, T, S, CN, YB, PS, MP, EN, SP):
        """
        :param T: Número de tiers
        :param S: Número de stacks
        :param CN: Número de contêineres
        :param YB: Matriz Yard Bay
        :param PS: Tamanho da população
        :param MP: Taxa de mutação
        :param EN: Número de evoluções
        :param SP: Tamanho do torneio
        :GN: Ajuste conforme o artigo manda, tamanho do cromossomo
        :population: vetor de população
        """
        self.T = T  # Número de tiers
        self.S = S  # Número de stacks
        self.CN = CN  # Número de contêineres
        self.YB = YB  # Matriz Yard Bay
        self.PS = PS  # Tamanho da população
        self.MP = MP  # Taxa de mutação
        self.EN = EN  # Número de evoluções
        self.SP = SP  # Tamanho do torneio
        self.GN = CN * 10  # Ajuste conforme o artigo manda
        self.population = []
        self.best_individuals_by_gen = [] # Melhores (top 1) indivíduos por geração

    def initialize_population(self):
        self.population = [Individual(self.GN, self.S) for _ in range(self.PS)]

    def evaluate_population(self):
        for individual in self.population:
            individual.evaluate_fitness(self.T, self.S, self.CN, self.GN, self.YB)

    def selection(self):
        selected = []
        for _ in range(self.SP):
            tournament = random.sample(self.population, self.SP)
            best_individual = min(tournament, key=lambda ind: ind.fitness)
            selected.append(best_individual)
        return selected
    def elitism(self):
        best_individual = min(self.population, key=lambda ind: ind.fitness)
        return best_individual
    def crossover(self, parent1, parent2):
        crossPoint = random.randint(1, self.GN - 2)
        child1_chromosome = parent1.chromosome[:crossPoint] + parent2.chromosome[crossPoint:]
        child2_chromosome = parent2.chromosome[:crossPoint] + parent1.chromosome[crossPoint:]
        child1 = Individual(self.GN, self.S)
        child2 = Individual(self.GN, self.S)
        child1.chromosome = child1_chromosome
        child2.chromosome = child2_chromosome
        return child1, child2

    def mutate(self, individual):
        for i in range(self.GN):
            if random.random() <= self.MP:
                individual.chromosome[i] = random.randint(0, self.S - 1)

    def run(self):

        self.initialize_population()
        self.evaluate_population()

        for _ in range(self.EN):
            P_estrela = []  
            crossN = (self.PS * self.SP) // 2

            # fitness_values = [ind.fitness for ind in self.population]
            # variance = self.calculate_variance(fitness_values)
            # self.variances.append(variance)

            for i in range(crossN):
                selected_parents = self.selection() 
                C1_new, C2_new = self.crossover(selected_parents[0], selected_parents[1]) 
                P_estrela.append(C1_new)
                P_estrela.append(C2_new)
            # best = self.elitism()
            # P_estrela.append(best)
            for i in range(self.PS):
                self.mutate(P_estrela[i])

            self.population = P_estrela
            self.evaluate_population()

            best_individual = min(self.population, key=lambda ind: ind.fitness)
            self.best_individuals_by_gen.append(best_individual.fitness)
        # self.plot_variance()

        # return best_individual.chromosome, best_individual.fitness, self.best_individuals_by_gen
        return self.best_individuals_by_gen

    # def calculate_variance(self, fitness_values):
    #     # variância populacional
    #     mean = sum(fitness_values) / len(fitness_values)
    #     variance = sum((x - mean) ** 2 for x in fitness_values) / len(fitness_values)
    #     return variance

  