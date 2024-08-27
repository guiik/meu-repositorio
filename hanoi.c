#include <stdio.h>
#include <stdlib.h>

struct disco {
    int peso;
    struct disco *pProx;
};

struct disco *pta = NULL, *ptb = NULL, *ptc = NULL;

void imprimir(struct disco *torre, char *nome_torre) {
    printf("TORRE %s - ", nome_torre);
    struct disco *pAux = torre;

    while (pAux != NULL) {
        printf("%d ", pAux->peso);
        pAux = pAux->pProx;
    }

    printf("\n");
}

void montar_torre(int tam) {
    if (tam < 0) {
        printf("TAMANHO DE TORRE INVALIDO\n");
        return;
    }

    int i;
    struct disco *novo_disco;

    for (i = tam; i >= 1; i--) {
        novo_disco = (struct disco *)malloc(sizeof(struct disco));

        if (novo_disco == NULL) {
            printf("Erro ao alocar memoria\n");
            return;
        }

        novo_disco->peso = i;
        novo_disco->pProx = pta;
        pta = novo_disco;
    }
}

void mover_disco(struct disco **origem, struct disco **destino) {
    struct disco *disco_aux = *origem;

    if (disco_aux == NULL)
        return;

    *origem = disco_aux->pProx;
    disco_aux->pProx = *destino;
    *destino = disco_aux;
}

void hanoi(int n, struct disco **origem, struct disco **destino, struct disco **auxiliar) {
    if (n == 1) {
        mover_disco(origem, destino);
        imprimir(pta, "A");
        imprimir(ptb, "B");
        imprimir(ptc, "C");
        printf("\n");
    } else {
        hanoi(n - 1, origem, auxiliar, destino);
        mover_disco(origem, destino);
        imprimir(pta, "A");
        imprimir(ptb, "B");
        imprimir(ptc, "C");
        printf("\n");
        hanoi(n - 1, auxiliar, destino, origem);
    }
}

int main() {
    int n;

    printf("Digite o número de discos: ");
    scanf("%d", &n);
    printf("Para resolver a Torre de Hanoi, faça:\n\n");

    montar_torre(n);
    imprimir(pta, "A");
    imprimir(ptb, "B");
    imprimir(ptc, "C");
    printf("\n");

    hanoi(n, &pta, &ptc, &ptb);

    return 0;
}
    
