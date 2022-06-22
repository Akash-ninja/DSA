#include <stdio.h>
#include <stdlib.h>
#define CREATE_NODE (struct Node *)malloc(1 * sizeof(struct Node))

struct Node
{
    int data;
    struct Node *next;
} *head = NULL; // Global pointer

void display(struct Node *p);
void createList(int A[], int n);
void sortedInsert_method1(int key);
void sortedInsert_method2(int key);

int main()
{
    printf("\n ------- INSERTION IN SORTED LIST --------- \n");

    int n, arr[20], key;
    printf("Please create linked list first with array values-- \n");
    printf("Enter no. of values you want to enter: \n");
    scanf("%d", &n);
    printf("Enter values (with spaces and in ascending order): \n");
    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    createList(arr, n);
    printf("\nLinked list created successfully... \n");
    display(head);

    printf("\nPlease insert key you want to insert: ");
    scanf("%d", &key);

    sortedInsert_method2(key);
    printf("\n Key got inserted successfully \n");
    display(head);

    printf("\n");
    return 0;
}

void display(struct Node *p)
{
    if (p == NULL)
    {
        printf("** Empty Linked List **");
    }

    while (p != NULL)
    {
        printf("%d ", p->data);
        p = p->next;
    }
}

void createList(int A[], int n)
{
    struct Node *p, *temp;

    head = CREATE_NODE;
    head->data = A[0];
    head->next = NULL;
    p = head;

    for (int i = 1; i < n; i++)
    {
        temp = CREATE_NODE;
        temp->data = A[i];
        temp->next = NULL;
        p->next = temp;
        p = temp;
    }
}

// using single pointer 'p'
void sortedInsert_method1(int key)
{
    struct Node *p, *temp;

    temp = CREATE_NODE;
    temp->data = key;

    p = head;

    if (head == NULL)
    {
        temp->next = NULL;
        head = temp;
    }
    else
    {
        // Take p to the location where key has to be inserted
        while (p->next != NULL && key > p->data && key > p->next->data)
            p = p->next;

        // If node has to inserted before first one
        if (p == head && key < p->data)
        {
            temp->next = head;
            head = temp;
        }
        else
        {
            temp->next = p->next;
            p->next = temp;
        }
    }
}

// using 2 pointers 'p' and 'q'
void sortedInsert_method2(int key)
{
    struct Node *p, *q, *temp;

    temp = CREATE_NODE;
    temp->data = key;

    p = head;

    if (head == NULL)
    {
        temp->next = NULL;
        head = temp;
    }
    else
    {
        // Take p to the location where key has to be inserted
        while (p && key > p->data)
        {
            q = p;
            p = p->next;
        }

        // If node has to inserted before first one
        if (p == head)
        {
            temp->next = head;
            head = temp;
        }
        else
        {
            temp->next = q->next;
            q->next = temp;
        }
    }
}