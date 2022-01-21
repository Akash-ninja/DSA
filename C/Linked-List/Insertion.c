#include <stdio.h>
#include <stdlib.h>
#define CREATE_NODE (struct Node *)malloc(1 * sizeof(struct Node))

struct Node
{
    int data;
    struct Node *next;
} *head = NULL; // Global pointer

void display(struct Node *p);
int countNodes(struct Node *p);
void insert(int value, int pos);

int main()
{
    printf("------- SINGLY LINKED LIST INSERTION ------ \n");

    while (1)
    {
        printf("\n\n");
        int op = 3, pos = -1, value = 0;
        printf("Please select an operation first: \n");
        printf("1. Insert at first position \n");
        printf("2. Insert at Any position \n");
        printf("3. Insert at Last position \n");
        printf("4. Display my list \n");
        printf("5. Exit \n");
        printf("Enter operation no.: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("Inserting in first position... \n");
            printf("Please enter data: ");
            scanf("%d", &value);
            insert(value, 0);
            display(head);
            break;

        case 2:
            printf("Please enter the position: ");
            scanf("%d", &pos);
            if (pos >= countNodes(head))
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
            printf("Inserting in last position... \n");
            printf("Please enter data: ");
            scanf("%d", &value);
            pos = countNodes(head);
            insert(value, pos);
            display(head);
            break;

        case 4:
            display(head);
            break;

        case 5:
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
        temp->next = NULL;
        head = temp;
    }
    else if (pos == 0)
    {
        temp->next = head;
        head = temp;
    }
    else
    {
        int i;
        p = head;
        for (i = 2; i <= pos; i++)
        {
            p = p->next;
        }
        temp->next = p->next;
        p->next = temp;
    }
}