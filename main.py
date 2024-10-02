import time
import matplotlib.pyplot as plt
from genetic_algorithm import GeneticAlgorithm

def ler_matrizes(arquivo):
    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    matrizes = []
    matriz_atual = []
    tamanho_atual = None

    for linha in linhas:
        linha = linha.strip()
        if 'x' in linha:
            if matriz_atual:
                matrizes.append((tamanho_atual, matriz_atual))
                matriz_atual = []
            tamanho_atual = linha
        elif linha:
            matriz_atual.append(list(map(int, linha.split())))

    if matriz_atual:
        matrizes.append((tamanho_atual, matriz_atual))

    return matrizes

def main():
    matrizes = ler_matrizes('matrizes.txt')
    tempos_execucao = []

    for tamanho, YB in matrizes:
        T, S = map(int, tamanho.split('x'))
        CN = T * S - (T - 1)  # Número de Containers
        PS = 15  # Tamanho da população
        MP = 0.05  # Taxa de mutação
        EN = 10  # Número de evoluções
        SP = 5  # Tamanho do torneio

        ga = GeneticAlgorithm(T, S, CN, YB, PS, MP, EN, SP)
        best_individuals_by_gen = []
        
        start_time = time.time()
        best_individuals_by_gen =  ga.run()
        end_time = time.time()
        
        tempo_execucao = end_time - start_time
        tempos_execucao.append(tempo_execucao)
        print(f"Tamanho da matriz: {tamanho}, Tempo de execução: {tempo_execucao:.4f} segundos")

    # Plotar gráfico de tempo por tamanho da matriz
    tamanhos = [tamanho for tamanho, _ in matrizes]
    plt.figure(figsize=(10, 5))
    plt.plot(tamanhos, tempos_execucao, marker='o')
    plt.xlabel('Tamanho da Matriz (T x S)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Tempo de Execução do Algoritmo Genético por Tamanho da Matriz')
    plt.grid(True)
    plt.show()
    
    ## Plotar o gráfico de melhor individuo por geração, da ultima geração
    def plot_variance(self):
        plt.plot(range(1, EN + 1), best_individuals_by_gen)
        plt.title('Melhor fitness ao Longo das Gerações')
        plt.xlabel('Geração')
        plt.ylabel('Fitness')
        plt.grid()
        plt.show()
    plot_variance(best_individuals_by_gen)
if __name__ == "__main__":
    main()