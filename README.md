#                          **OneMax**
O problema OneMax é um dos problemas clássicos em algoritmos genéticos, onde o objetivo é maximizar o número de bits "1" em um vetor binário. 
Cada vetor binário representa um indivíduo em uma população, e o objetivo do algoritmo é evoluir essa população até que todos os indivíduos sejam constituídos apenas por "1s".
Este Programa foi desenvido por mim (Guilherme durante a graduação em biotecnologia na UFRJ na materia de Computação evolucionista ministrada pela Dra. Camila Silva de Magalhães

## Funções

### OneMaxUn(ind):
Propósito: Calcula a função de fitness para um indivíduo. A função fitness, neste caso, é a soma de todos os bits "1" no vetor do indivíduo.  
Entrada: Um vetor binário (ind).  
Saída: O valor da soma dos bits "1" (fitness do indivíduo).  

### OneMaxPop(pop):
Propósito: Avalia toda a população, calculando o fitness de cada indivíduo.  
Entrada: Uma população (pop), que é uma lista de vetores binários.  
Saída: Uma lista contendo os valores de fitness de todos os indivíduos.  

### GerarPop(N, L):
Propósito: Gera uma população inicial aleatória de tamanho N, onde cada indivíduo possui L bits.  
Entrada: N (número de indivíduos) e L (número de bits por indivíduo).  
Saída: Uma lista de indivíduos, onde cada indivíduo é um vetor binário.  

### Selecao(N, pop, pop_fitness):
Propósito: Realiza a seleção de indivíduos para a próxima geração usando torneio binário.  
Entrada: N (número de indivíduos), pop (a população atual), pop_fitness (os valores de fitness).  
Saída: Uma nova população selecionada.  

### Crossover(pop, Pc):
Propósito: Realiza o cruzamento de um ponto entre pares de indivíduos da população.  
Entrada: pop (a população) e Pc (probabilidade de crossover).  
Saída: Uma nova população gerada após o cruzamento.  

### Crossover_2pontos(pop, Pc):
Propósito: Realiza o cruzamento de dois pontos entre pares de indivíduos da população.  
Entrada: pop (a população) e Pc (probabilidade de crossover).  
Saída: Uma nova população gerada após o cruzamento de dois pontos.  

### Crossover_MU(pop, Pc):
Propósito: Realiza o crossover de recombinação metade uniforme, onde bits diferentes têm uma chance de trocar de posição entre os pais.  
Entrada: pop (a população) e Pc (probabilidade de crossover).  
Saída: Uma nova população após o crossover metade uniforme.  

### recombinação3(população3, Pc):
Propósito: Realiza o cruzamento entre três pais, onde o filho herda bits iguais de dois pais, ou bits do terceiro pai caso sejam diferentes.  
Entrada: população3 (a população) e Pc (probabilidade de crossover).  
Saída: Uma nova população gerada após o cruzamento de três pais.  

### BitFlip(pop, pm):
Propósito: Realiza a mutação nos indivíduos, onde cada bit tem uma probabilidade pm de ser invertido.  
Entrada: pop (a população) e pm (probabilidade de mutação por bit).  
Saída: A população após a aplicação da mutação.  

### PrintEstFit(pop_fitness):
Propósito: Calcula estatísticas da população (maior, menor e média de fitness).  
Entrada: pop_fitness (valores de fitness da população).  
Saída: Uma lista contendo o maior, o menor e a média do fitness.  

### PrintFitness(pop_fitness):
Propósito: Exibe o fitness de cada indivíduo da população.  
Entrada: pop_fitness (valores de fitness da população).  
Saída: Nenhuma (apenas imprime os valores).  

### Evolution(N, L, MaxGen, Pm, Pc, Tipo_Cross):
Propósito: Executa o processo evolutivo, incluindo seleção, crossover, mutação, e avaliação de fitness até que o critério de parada seja atingido 
(número máximo de gerações ou fitness ótimo).  
Entrada: Parâmetros do GA, como N (tamanho da população), L (tamanho do indivíduo), MaxGen (número máximo de gerações), Pm (probabilidade de mutação), 
Pc (probabilidade de crossover), e Tipo_Cross (tipo de crossover a ser usado).  
Saída: O número de gerações e o sucesso (se encontrou a solução ótima).  



# Simulação e Análise de Estatísticas Amostrais (Sim_An_Est_Amostrais.py)

Este programa foi desenvolvido por mim (Guilherme Henrique Bittencourt) como parte da matéria de Métodos Numéricos ministrada pelo Dr. Renato Simões Silva durante meu mestrado no LNCC — Laboratório Nacional de Computação Científica,
com o objetivo de praticar conceitos de estatística inferencial.   
O propósito do programa é simular o comportamento de médias e variâncias amostrais, usando diferentes tamanhos de amostras, e visualizar a distribuição dessas estatísticas.  
Na pratica o programa lê os dados de arquivos, gera amostras estatísticas, e compara essas amostras com distribuições normais para médias e variâncias. 

## Funções 

### ler_dados(arquivo)

Propósito: ler os dados de um arquivo de texto, converte cada linha em um número de ponto flutuante (float) e retorna esses números como um array NumPy.  
Um array NumPy permite a manipulação eficiente desses dados para análises estatísticas subsequentes.  
Entrada: o diretorio e nome do arquivo de dados  
Saída: Um array NumPy contendo os dados lidos do arquivo.

### gerar_amostras_estatisticas(dados, tamanho_amostra, num_amostras=10000)

Propósito: criar amostras aleatórias a partir de um conjunto de dados original, calcular estatísticas dessas amostras, e retornar as médias e variâncias dessas amostras.  
Entrada: dados (array NumPy dos dados), tamanho_amostra (número de elementos de cada nova amostra), num_amostras (quantidade de amostras que serão geradas).  
Saída: média e a variância calculadas para cada amostra são adicionadas às listas **medias_amostrais** e **variancias_amostrais**.

## Execução do Programa

### Entrada de dados
define os arquivos de dados e tamanhos das amostras geradas

### Loop principal 
Itera sobre cada arquivo e cada tamanho de amostra, gerando as estatísticas para cada combinação.  
Para cada arquivo, os dados são lidos e processados para gerar amostras estatísticas.   
As médias e variâncias dessas amostras são calculadas e usadas para criar distribuições normais.  

### Função "norm()" para Distribuições Normais
**norm()** é uma função da biblioteca SciPy que cria distribuições normais

Entrada:

**loc** (media da distribuição) no codigo utilizei estimatitiva da média da distribuição das médias amostrais (media_media = np.mean(medias_amostrais))

_(Caro leitor releembro aqui que a função mean calcula a média dos dados de uma amostra, e essa média é uma estimativa da média verdadeira da população. 
Como estamos lidando com uma amostra, e não com a população inteira, a média amostral é usada como uma aproximação ou "melhor palpite" da média populacional, 
levando em consideração que essa estimativa pode ter algum erro dependendo da representatividade e do tamanho da amostra.)_

**scale** (desvio padrão da distribuição.)

O desvio paradrão é calculado como a raiz quadrada da variância. 
No código, scale=np.sqrt(variancia_media) e scale=np.sqrt(variancia_variancia) são usados para definir o desvio padrão das distribuições normais para as médias e variâncias amostrais, respectivamente.

## Visualização dos resultados
Para cada conjunto de dados, dois gráficos são criados lado a lado: um para as médias amostrais e outro para as variâncias amostrais. Os gráficos mostram o histograma dos dados amostrais e sobrepõem a curva da distribuição normal para comparação.



