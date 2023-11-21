import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def ler_dados(arquivo):
    with open(arquivo, 'r') as f:
        dados = [float(line.strip()) for line in f]
    return np.array(dados)

def gerar_amostras_estatisticas(dados, tamanho_amostra, num_amostras=10000):
    medias_amostrais = []
    variancias_amostrais = []

    for _ in range(num_amostras):
        amostra = np.random.choice(dados, size=tamanho_amostra, replace=True)
        media_amostral = np.mean(amostra)
        variancia_amostral = np.var(amostra, ddof=1)  # ddof=1 para usar n-1 no denominador

        medias_amostrais.append(media_amostral)
        variancias_amostrais.append(variancia_amostral)

    return np.array(medias_amostrais), np.array(variancias_amostrais)

#lista de arquivos
arquivos = ['data1q.dat', 'data1t.dat', 'data1x.dat', 'data1y.dat']

tamanhos_amostra = [5, 10, 50]

for arquivo in arquivos:
    dados = ler_dados(arquivo)

    for tamanho_amostra in tamanhos_amostra:
        medias_amostrais, variancias_amostrais = gerar_amostras_estatisticas(dados, tamanho_amostra)

        # média e a variância das amostras de média e variância
        media_media = np.mean(medias_amostrais)#estimativa da média da distribuição das médias amostrais que sempre da algo beeem perto de 3
        variancia_media = np.var(medias_amostrais, ddof=1)
        media_variancia = np.mean(variancias_amostrais)
        variancia_variancia = np.var(variancias_amostrais, ddof=1)


        # distribuição normal para média e variância
        dist_media = norm(loc=media_media, scale=np.sqrt(variancia_media)) # distribuição normal para as médias amostrais.
        dist_variancia = norm(loc=media_variancia, scale=np.sqrt(variancia_variancia))

        # histograma e distribuição normal para média
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 2, 1)
        plt.hist(medias_amostrais, bins=23, density=True, edgecolor='black', alpha=0.7, label='Histograma')
        plt.plot(np.sort(medias_amostrais), dist_media.pdf(np.sort(medias_amostrais)), label='Distribuição Normal')
        plt.title(f'Média Amostral - {arquivo} (n={tamanho_amostra})')
        plt.legend()

        # histograma e distribuição normal para variância
        plt.subplot(1, 2, 2)
        plt.hist(variancias_amostrais, bins=27, density=True, edgecolor='black', alpha=0.7, label='Histograma')
        plt.plot(np.sort(variancias_amostrais), dist_variancia.pdf(np.sort(variancias_amostrais)), label='Distribuição Normal')
        plt.title(f'Variância Amostral - {arquivo} (n={tamanho_amostra})')
        plt.legend()

        plt.tight_layout()
        plt.show()
