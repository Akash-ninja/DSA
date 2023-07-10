#include <stdio.h>
#include <stdlib.h>
#define CREATE_NODE (struct Node *)malloc(1 * sizeof(struct Node))

struct Node
{
    struct Node *prev;
    int data;
    struct Node *next;
} *head = NULL, *last = NULL; // Global pointer

void display(struct Node *p);
int countNodes(struct Node *p);
void insert(int value, int pos);
void insertLast(int value);

int main()
{
    printf("------- DOUBLY LINKED LIST INSERTION ------ \n");

    while (1)
    {
        printf("\n\n");
        int op = 5, pos = -1, value = 0;
        printf("Please select an operation first: \n");
        printf("1. Insert at first position \n");
        printf("2. Insert at Any position \n");
        printf("3. Insert at Last position \n");
        printf("4. Create List using Insertion at last \n");
        printf("5. Display my list \n");
        printf("6. Exit \n");
        printf("Enter operation no.: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("Please enter data: ");
            scanf("%d", &value);
            printf("Inserting in first position... \n");
            insert(value, 0);
            display(head);
            break;

        case 2:
            printf("Please enter the position: ");
            scanf("%d", &pos);
            if (pos > countNodes(head))
            {
                printf("Position not available. Please try again. \n");
                break;
            }
            printf("Please enter data: ");
            scanf("%d", &value);
            insert(value, pos);
            display(head);
            break;

        case 3:
            printf("Please enter data: ");
            scanf("%d", &value);
            printf("Inserting in last position... \n");
            pos = countNodes(head);
            insert(value, pos);
            display(head);
            break;

        case 4:
            printf("Please enter data: ");
            scanf("%d", &value);
            printf("Creating list... \n");
            insertLast(value);
            printf("List created successfully... \n");
            display(head);
            break;

        case 5:
            display(head);
            break;

        case 6:
            return 0;

        default:
            break;
        }
    }

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

int countNodes(struct Node *p)
{
    int cnt = 0;
    while (p != NULL)
    {
        p = p->next;
        cnt++;
    }

    return cnt;
}

void insert(int value, int pos)
{
    struct Node *p;

    struct Node *temp = CREATE_NODE;
    temp->data = value;

    if (head == NULL)
    {
        temp->prev = NULL;
        temp->next = NULL;
        head = temp;
    }
    else if (pos == 0)
    {
        temp->prev = NULL;
        temp->next = head;
        head = temp;
    }
    else
    {
        int i;
        p = head;
        for (i = 2; i <= pos; i++)
            p = p->next;

        temp->next = p->next;
        temp->prev = p;

        if (p->next)
            p->next->prev = temp;

        p->next = temp;
    }
}

// Will only work when list is not created
void insertLast(int value)
{
    struct Node *temp;

    temp = CREATE_NODE;
    temp->data = value;
    temp->next = NULL;
    temp->prev = NULL;

    if (head == NULL)
        head = last = temp;
    else
    {
        last->next = temp;
        temp->prev = last;
        last = temp;
    }
}