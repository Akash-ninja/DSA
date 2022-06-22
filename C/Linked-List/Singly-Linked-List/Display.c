#include <stdio.h>
#include <stdlib.h>
#define CREATE_NODE (struct Node *)malloc(1 * sizeof(struct Node))

struct Node
{
    int data;
    struct Node *next;
} *first = NULL; // Global pointer

void createLinkedList(int A[], int n)
{

    int i;
    struct Node *t, *last;

    first = CREATE_NODE;
    first->data = A[0];
    first->next = NULL;
    last = first;

    for (i = 1; i < n; i++)
    {
        t = CREATE_NODE;
        t->data = A[i];
        t->next = NULL;
        last->next = t;
        last = t;
    }

    printf("Linked list created successfully \n");
}

void display(struct Node *p)
{
    while (p != NULL)
    {
        printf("%d ", p->data);
        p = p->next;
    }
}

void recursiveDisplay(struct Node *p)
{
    if (p != NULL) 
    {
        printf("%d ", p->data);
        recursiveDisplay(p->next);
    }
}

int main()
{
    printf("Code Execution started...!\n");

    int A[] = {10, 70, 50, 39, 500, 1729, 234};
    int n = sizeof(A) / sizeof(A[0]);

    createLinkedList(A, n);
    recursiveDisplay(first);

    printf("\n");
    return 0;
}