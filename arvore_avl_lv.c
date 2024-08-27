#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

struct node {
    int iVal;
    int iAlt;
    struct node* esq;
    struct node* dir;
};

int f_iAlt(struct node* n) {
    if (n == NULL)
        return 0;
    return n->iAlt;
}

int f_balance(struct node* n) {
    if (n == NULL)
        return 0;
    return f_iAlt(n->esq) - f_iAlt(n->dir);
}

struct node* new_node(int iVal) {
    struct node* node = (struct node*)malloc(sizeof(struct node));
    node->iVal = iVal;
    node->iAlt = 1;
    node->esq = NULL;
    node->dir = NULL;
    return node;
}

struct node* dir_rotate(struct node* y) {
    struct node* x = y->esq;
    struct node* z = x->dir;

    x->dir = y;
    y->esq = z;

    y->iAlt = 1 + ((f_iAlt(y->esq) > f_iAlt(y->dir)) ? f_iAlt(y->esq) : f_iAlt(y->dir));
    x->iAlt = 1 + ((f_iAlt(x->esq) > f_iAlt(x->dir)) ? f_iAlt(x->esq) : f_iAlt(x->dir));

    return x;
}

struct node* esq_rotate(struct node* x) {
    struct node* y = x->dir;
    struct node* z = y->esq;

    y->esq = x;
    x->dir = z;

    x->iAlt = 1 + ((f_iAlt(x->esq) > f_iAlt(x->dir)) ? f_iAlt(x->esq) : f_iAlt(x->dir));
    y->iAlt = 1 + ((f_iAlt(y->esq) > f_iAlt(y->dir)) ? f_iAlt(y->esq) : f_iAlt(y->dir));

    return y;
}

struct node* insert_node(struct node* node, int iVal) {
    if (node == NULL)
        return new_node(iVal);

    if (iVal < node->iVal)
        node->esq = insert_node(node->esq, iVal);  /* possível inserção à esquerda */
    else if (iVal > node->iVal)
        node->dir = insert_node(node->dir, iVal); /* possível inserção à direita */
    else {
        printf("Valores iguais não são permitidos.\n");
        return node;
    }

    node->iAlt = 1 + ((f_iAlt(node->esq) > f_iAlt(node->dir)) ? f_iAlt(node->esq) : f_iAlt(node->dir));

    int balance = f_balance(node);  /* f_balance = esquerda - direita */

    if (balance > 1 && iVal < node->esq->iVal)   /* esquerda e esquerda */
        return dir_rotate(node);

    if (balance < -1 && iVal > node->dir->iVal) /* direita e direita */
        return esq_rotate(node);

    if (balance > 1 && iVal > node->esq->iVal) { /* esquerda e direita */
        node->esq = esq_rotate(node->esq);
        return dir_rotate(node);
    }

    if (balance < -1 && iVal < node->dir->iVal) { /* direita e esquerda */
        node->dir = dir_rotate(node->dir);
        return esq_rotate(node);
    }

    return node;
}

struct node* min_node(struct node* node) { /* retorna o menor nó (o nó mais à esquerda) */
    struct node* a = node;
    while (a->esq != NULL)
        a = a->esq;
    return a;
}

struct node* delete_node(struct node* root, int iVal) {
    if (root == NULL)
        return root;

    if (iVal < root->iVal)
        root->esq = delete_node(root->esq, iVal);
    else if (iVal > root->iVal)
        root->dir = delete_node(root->dir, iVal);
    else {
        if ((root->esq == NULL) || (root->dir == NULL)) { /* possui um ou nenhum filho */
            struct node* temp = root->esq ? root->esq : root->dir; /* um nó temporário temp é atribuído ao filho não nulo. */

            if (temp == NULL) { /* se não tiver nenhum filho aqui fica nulo */
                root = NULL;
            } else
                *root = *temp;

            free(temp);
        } else { /* possui dois filhos */
            struct node* temp = min_node(root->dir); /* o nó de valor mais próximo */

            root->iVal = temp->iVal;
            root->dir = delete_node(root->dir, temp->iVal);
        }
    }

    if (root == NULL)
        return root;

    root->iAlt = 1 + ((f_iAlt(root->esq) > f_iAlt(root->dir)) ? f_iAlt(root->esq) : f_iAlt(root->dir));

    int balance = f_balance(root); /* f_balance = esquerda - direita */

    if (balance > 1 && f_balance(root->esq) >= 0)  /* esquerda e esquerda */
        return dir_rotate(root);

    if (balance < -1 && f_balance(root->dir) <= 0)  /* direita e direita */
        return esq_rotate(root);

    if (balance > 1 && f_balance(root->esq) < 0) { /* esquerda e direita */
        root->esq = esq_rotate(root->esq);
        return dir_rotate(root);
    }

    if (balance < -1 && f_balance(root->dir) > 0) { /* direita e esquerda */
        root->dir = dir_rotate(root->dir);
        return esq_rotate(root);
    }

    return root;
}

void print_tree(struct node* root, int space) {
    if (root == NULL)
        return;

    space += 10;

    print_tree(root->dir, space);

    printf("\n");
    for (int i = 10; i < space; i++)
        printf(" ");
    printf("%d\n", root->iVal);

    print_tree(root->esq, space);
}

int search_node(struct node* root, int iVal) {
    if (root == NULL)
        return 0;

    if (root->iVal == iVal)
        return 1;

    if (iVal < root->iVal)
        return search_node(root->esq, iVal);

    return search_node(root->dir, iVal);
}


int main() {
    setlocale(LC_ALL, "Portuguese");
    int choice, value;
    struct node* root = NULL;

    do {
        printf("\n\n*********** MENU **********\n");
        printf("(1) Inserir Valor\n");
        printf("(2) Excluir Valor\n");
        printf("(3) Busca\n");
        printf("(4) Imprimir Árvore\n");
        printf("(0) Sair\n\n");
        printf("Selecione uma opção: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("\n------- INSERÇÃO DE NÓ ------\n");
                do {
                    printf("\nInforme o valor a ser inserido (-1 para retornar): ");
                    scanf("%d", &value);
                    if (value == -1)
                        break;
                    root = insert_node(root, value);
                    printf("\n# ÁRVORE:\n");
                    print_tree(root, 0);
                } while (value != -1);
                break;
            case 2:
                printf("\n------ EXCLUSÃO DE NÓ ------\n");
                do {
                    printf("\nInforme o valor a ser removido (-1 para retornar): ");
                    scanf("%d", &value);
                    if (value == -1)
                        break;
                    root = delete_node(root, value);
                    printf("\n# ÁRVORE:\n");
                    print_tree(root, 0);
                } while (value != -1);
                break;
            case 3:
                printf("\n------ BUSCA ------\n");
                do {
                    printf("\nInforme o valor a ser buscado (-1 para retornar): ");
                    scanf("%d", &value);
                    if (value == -1)
                        break;
                    if (search_node(root, value)) {
                        printf("O valor EXISTE na árvore.\n");
                    } else {
                        printf("O valor NÃO existe na árvore.\n");
                    }
                } while (value != -1);
                break;
            case 4:
                printf("\n------ IMPRESSÃO ------\n");
                if (root) {
                    printf("\n# ÁRVORE:\n");
                    print_tree(root, 0);
                } else {
                    printf("\nÁrvore vazia.\n");
                }
                break;
        }
    } while (choice != 0);

    return 0;
}
