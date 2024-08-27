import random

def OneMaxUn(ind):
    fitness = 0
    for i in ind:
        fitness += i
    return fitness

def OneMaxPop (pop):
    fitness_pop=[]
    cont=0
    #print ('popilação', pop)
    for i in range (len(pop)):
        ind = i
        fitness= OneMaxUn (pop[i])
        fitness_pop.append(fitness)
        #print ( "individuo", i+1, pop[i]," fitness", fitness)
        cont += 1
    return fitness_pop

def GerarPop (N,L):
    pop=[] #matriz
    ind=[] #linha
    #print (type(N))
    for i in range (N):
        for j in range (L):
            u= random.random()
            bit=0
            if u > 0.5 :
                bit=1
            ind.append(bit)
        pop.append(ind)
        #print( "individuo", i+1, ind)
        ind = []
    return pop

def Selecao (N, pop, pop_fitness):
    new_pop=[]
    for i in range (N):
        sel_a= random.randint(0,N-1)
        sel_b= random.randint(0,N-1)
        #print ("individuo",sel_a+1, pop[sel_a], "X individuo",sel_b+1, pop[sel_b])
        
        if pop_fitness[sel_a] >= pop_fitness[sel_b]:
            new_pop.append(pop[sel_a])
            #print("individuo", sel_a+1, pop[sel_a], "GANHOU")
        else:
            new_pop.append(pop[sel_b])
            #print ("individuo", sel_b+1, pop[sel_b], "GANHOU")
    #print (new_pop)
    return new_pop
        
def Crossover(pop, Pc):
    cros_pop=[]
    for i in range (0, len(pop), 2):
        pai1= pop[i]
        pai2= pop[i+1]
        u = random.random()
        if u < Pc:
            #print ("pai 1-", pai1, "pai 2-", pai2)
            corte= random.randint(0, len(pai1) - 1)
            #print ("corte:", corte)
            filho1= pai1 [:corte] + pai2 [corte:]
            filho2= pai2 [:corte] + pai1 [corte:]
            #print(" filho 1-", filho1, "\n filho 2-", filho2)
            cros_pop.append(filho1)
            cros_pop.append(filho2)
        else:
            cros_pop.append(pai1)
            cros_pop.append(pai2)
    return cros_pop


def Crossover_2pontos(pop, Pc):
    cros_pop=[]
    for i in range (0, len(pop), 2):
        pai1= pop[i]
        pai2= pop[i+1]
        filho1= []
        filho2 = []
        u = random.random()
        if u < Pc:
           # print ("pai 1-", pai1, "pai 2-", pai2)
            cortea= random.randint(0, len(pai1) - 1)
            corteb= random.randint(0, len(pai1) - 1)
            #print ("cortea:", cortea)
           # print ("corteb:", corteb)
            if cortea < corteb:
                for j in range ( len(pai1)):
                    cont = j
                    if cont < cortea:
                        filho1.append(pai1[j])
                        filho2.append(pai2[j])
                    if cont >= cortea and cont <= corteb:
                        filho1.append(pai2[j])
                        filho2.append(pai1[j])
                    if cont > corteb:
                        filho1.append(pai1[j])
                        filho2.append(pai2[j])
                #print ('filho1 - ', filho1)
                #print ('filho2 - ', filho2)
            if cortea > corteb:
                for j in range ( len(pai1)):
                    cont = j
                    if cont > cortea:
                        filho1.append(pai1[j])
                        filho2.append(pai2[j])
                    if cont <= cortea and cont >= corteb:
                        filho1.append(pai2[j])
                        filho2.append(pai1[j])
                    if cont < corteb:
                        filho1.append(pai1[j])
                        filho2.append(pai2[j])
               # print ('filho1 - ', filho1)
                #print ('filho2 - ', filho2)
            if cortea == corteb:
                for j in range ( len(pai1)):
                    cont = j
                    if cont == cortea:
                        filho1.append(pai2[j])
                        filho2.append(pai1[j])
                    else:
                        filho1.append(pai1[j])
                        filho2.append(pai2[j])
                #print ('filho1 - ', filho1)
                #print ('filho2 - ', filho2)
            cros_pop.append(filho1)
            cros_pop.append(filho2)   
        else:
            cros_pop.append(pai1)
            cros_pop.append(pai2)
    return cros_pop


def Crossover_MU (pop, Pc):
    cros_pop= []
    p= 0.5
    for i in range (0, len(pop), 2):
        pai1= pop[i]
        pai2= pop[i+1]
        u1 = random.random()
        if u1 < Pc:
            #print ("pai 1-", pai1, "pai 2-", pai2)
            filho1=[]
            filho2=[]
            for j in range ( len(pai1)):
                #print ("caracter do pai 1", pai1[j])
                #print ("caracter do pai 2", pai2[j])
                if pai1[j] != pai2[j]:
                    u= random.random()
                    #print ('caracter', j+1, 'PORCENAGEM', u)
                    if u < p:
                        #print ('deveria trocar')
                        filho1.append(pai2[j])
                        filho2.append(pai1[j])
                    else:
                        #print ('nao deveira trocar')
                        filho1.append(pai1[j])
                        filho2.append(pai2[j])
                else:
                    #print ('caracter igual')
                    filho1.append(pai1[j])
                    filho2.append(pai2[j])
            #print('filho1-1', filho1, 'filho2-', filho2)
            cros_pop.append(filho1)
            cros_pop.append(filho2)
        else:
            cros_pop.append(pai1)
            cros_pop.append(pai2)
                        
                           
    #print('teste', cros_pop)      
    return cros_pop
            

def recombinação3(população3, Pc):
    filhos_recomb3=[]
    #print ('pop', população3)
    for tiraptchurum in range(len(população3)):
        u = random.random()
        aleat1=random.randint(0,len(população3)-1)
        dad1=população3[aleat1]
        if u < Pc:
            aleat2=random.randint(0,len(população3)-1)
            aleat3=random.randint(0,len(população3)-1)
            dad2=população3[aleat3]
            dad3=população3[aleat2]
            filho_vez=[]
            for namadrugada in range(len(dad1)):
                if dad1[namadrugada]==dad2[namadrugada]:
                    filho_vez.append(dad1[namadrugada])
                else:
                    filho_vez.append(dad3[namadrugada])
            filhos_recomb3.append(filho_vez)
        else:
            filhos_recomb3.append(dad1)
    #print ('teste',filhos_recomb3) 
    return filhos_recomb3


def BitFlip (pop,pm):
    for i in range (len(pop)):
        #print(" \n individuo", i+1, " antes da mutação", pop[i])
        for j in range (len( pop [i])):
            #print ('antes', pop[i][j])
            r = random.random()
            #print ("R :", r)
            if r < pm :
                if pop [i][j] == 1:
                    pop [i][j] = 0
                else:
                    pop[i][j] = 1
            #print ('dps',pop[i][j])
        #print("individuo", i+1, " apos da mutação", pop[i])
    #print ('população', pop)
    return pop
     
            
def PrintEstFit(pop_fitness):
    maior_fit= max(pop_fitness)
    #print ("maor fit é", maior_fit)
    menor_fit= min(pop_fitness)
    #print ("menor fitness é", menor_fit)
    media_fit=0
    for i in pop_fitness:
        media_fit += i
    media_fit= media_fit / len (pop_fitness)
    #print ("fitness medio:", media_fit)
    Estatistica = [maior_fit, menor_fit, media_fit]
    return Estatistica
    
def PrintFitness (pop_fitness):
    for i in range (len(pop_fitness)):
        print ( "individuo", i+1, "fiteness:", pop_fitness[i])

def Evolution (N, L, MaxGen, Pm, Pc, Tipo_Cross):
    Resultado_Otimo = L
    PopA = GerarPop (N, L)
    #print("população:", PopA)
    Pop_Fitness = OneMaxPop(PopA)
    Best_Fitness= max(Pop_Fitness)
    Gen=1

    while Gen <= MaxGen and Best_Fitness < Resultado_Otimo:
        PopA = Selecao (N, PopA, Pop_Fitness)
        if Tipo_Cross != 2 and Tipo_Cross !=3 and Tipo_Cross != 4:
            PopA= Crossover (PopA, Pc)
        if Tipo_Cross ==2:
            PopA= Crossover_2pontos (PopA, Pc)
        if Tipo_Cross ==3:
            PopA= recombinação3 (PopA, Pc)
        if Tipo_Cross ==4:
            PopA= Crossover_MU (PopA, Pc)
        
        PopA= BitFlip (PopA, Pm)
        Pop_Fitness = OneMaxPop(PopA)
        Best_Fitness= max(Pop_Fitness)
        Estatistica = PrintEstFit (Pop_Fitness)
        print ( "geração", Gen, "maior Fit", Estatistica[0], "menor Fit", Estatistica[1], "Fit medio", Estatistica[2])
        Gen = Gen + 1
    if Best_Fitness == Resultado_Otimo:
        Sucesso = 1
    else:
        Sucesso = 0
    return Gen , Sucesso

        
         
    
    






semente= 2
#N= int(input("quantos individuos?")) 
#L= int(input("quantidade de cromossomos?"))
#print ('para realizar o Crossover de um ponto digite 1, \n para realizar o Crossover de dois ponto digite 2, \n para realizar o Crossover de três progenitores digite 3, \n para realizar o Crossover de recombinação metade uniforme digite 4') 
#Tipo_Cross= int(input ('Qual crossover vamos realizar?'))
Tipo_Cross = 4
N=2000
L=1500


Pc= 0.7
Pm= 1/L
run=1
Nruns=10
MaxGen=300
Sucesso_Acumulado = 0
Gen_Acumulado= 0

while run<= Nruns :
    random.seed(semente)
    Lista_Gen=[]
    Gen , Sucesso = Evolution (N, L, MaxGen, Pm, Pc, Tipo_Cross)
    print ('rodada =', run)
    print ('Numero de gerações: ', Gen-1)
    Lista_Gen.append(Gen)
    print (Sucesso)
    Sucesso_Acumulado += Sucesso
    Gen_Acumulado += Gen
    run +=1
    semente +=1

Taxa_Sucesso = Sucesso_Acumulado / Nruns
Media_Gen = Gen_Acumulado / Nruns
print ("taxa de sucesso", Taxa_Sucesso)
print ("Media geraçoes", Media_Gen)


   

  



