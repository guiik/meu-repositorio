import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Informações teóricas sobre as variáveis
teoria = {
    'q': {'media': 3, 'desvio_padrao': np.sqrt(3)},
    'x': {'media': 3, 'desvio_padrao': np.sqrt(3)},
    'y': {'media': 3, 'desvio_padrao': np.sqrt(9)},
    'T': {'media': 3, 'desvio_padrao': np.sqrt(2.1)}
}

# Função para ler dados de um arquivo
def ler_dados(arquivo):
    return np.loadtxt(arquivo) #numpy.loadtxt para ler os dados de um arquivo e retorna um array NumPy.

# Função para gerar amostras estatísticas (médias e variâncias)
def gerar_amostras_estatisticas(dados, tamanho_amostra, num_amostras=10000):
    medias_amostrais = np.mean(np.random.choice(dados, size=(num_amostras, tamanho_amostra), replace=True), axis=1)
    variancias_amostrais = np.var(np.random.choice(dados, size=(num_amostras, tamanho_amostra), replace=True), axis=1, ddof=1) # ddof=1 -> n-1
    return medias_amostrais, variancias_amostrais

# Tamanhos de amostra a serem considerados
tamanhos_amostra = [5, 10, 50]

# Lista de arquivos
arquivos = ['data1q.dat', 'data1x.dat', 'data1y.dat', 'data1t.dat']

# Loop sobre cada arquivo
for arquivo in arquivos:
    dados = ler_dados(arquivo)

    # Loop sobre cada tamanho de amostra
    for tamanho_amostra in tamanhos_amostra:
        # Gerar amostras estatísticas para médias e variâncias
        medias_amostrais, variancias_amostrais = gerar_amostras_estatisticas(dados, tamanho_amostra)

        # Estatísticas das amostras de médias e variâncias
        dist_media = norm(loc=np.mean(medias_amostrais), scale=np.std(medias_amostrais))
        dist_variancia = norm(loc=np.mean(variancias_amostrais), scale=np.std(variancias_amostrais))

        # Plotagem dos resultados
        plt.figure(figsize=(12, 4))

        # Subplot 1: Média Amostral
        plt.subplot(1, 2, 1)
        plt.hist(medias_amostrais, bins=50, density=True, edgecolor='black', alpha=0.7, label='Histograma')
        plt.plot(np.sort(medias_amostrais), dist_media.pdf(np.sort(medias_amostrais)), label='Distribuição Normal')
        plt.title(f'Média Amostral - {arquivo} (n={tamanho_amostra})')
        plt.legend()

        # Subplot 2: Variância Amostral
        plt.subplot(1, 2, 2)
        plt.hist(variancias_amostrais, bins=50, density=True, edgecolor='black', alpha=0.7, label='Histograma')
        plt.plot(np.sort(variancias_amostrais), dist_variancia.pdf(np.sort(variancias_amostrais)), label='Distribuição Normal')
        plt.title(f'Variância Amostral - {arquivo} (n={tamanho_amostra})')
        plt.legend()

        # Ajuste de layout e exibição do gráfico
        plt.tight_layout()
        plt.show()
