#include <stdio.h>
#include <stdlib.h>
#define CREATE_NODE (struct Node *)malloc(1 * sizeof(struct Node))

struct Node
{
    int data;
    struct Node *next;
} *head = NULL; // Global pointer

void display(struct Node *p);
void recursiveDisplay(struct Node *p);
int countNodes(struct Node *p);
void circularInsert(int value, int pos);

int main()
{
    printf("\n------- CIRCULAR LINKED LIST INSERTION ------ \n");

    while (1)
    {
        printf("\n");
        int op = 3, pos = -1, value = 0;
        printf("Please select an operation first: \n");
        printf("1. Insert before first position \n");
        printf("2. Insert at Any position \n");
        printf("3. Insert after Last position \n");
        printf("4. Display my list \n");
        printf("5. Exit \n");
        printf("Enter operation no.: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("Please enter data: ");
            scanf("%d", &value);
            printf("Inserting in first position... \n");
            circularInsert(value, 0);
            recursiveDisplay(head);
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
            circularInsert(value, pos);
            recursiveDisplay(head);
            break;

        case 3:
            printf("Please enter data: ");
            scanf("%d", &value);
            printf("Inserting in last position... \n");
            pos = countNodes(head);
            circularInsert(value, pos);
            recursiveDisplay(head);
            break;

        case 4:
            recursiveDisplay(head);
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
        return;
    }

    do
    {
        printf("%d ", p->data);
        p = p->next;
    } while (p != head);
}

void recursiveDisplay(struct Node *p)
{
    if (p == NULL)
    {
        printf("** Empty Linked List **");
        return;
    }

    static int flag = 0;

    if (p != head || flag == 0)
    {
        flag = 1;
        printf("%d ", p->data);
        recursiveDisplay(p->next);
    }

    flag = 0;
}

int countNodes(struct Node *p)
{
    int cnt = 0;

    if (!p)
        return cnt;

    do
    {
        p = p->next;
        cnt++;
    } while (p != head);

    return cnt;
}

void circularInsert(int value, int pos)
{
    struct Node *p;

    struct Node *temp = CREATE_NODE;
    temp->data = value;

    if (head == NULL)
    {
        head = temp;
        head->next = temp;
    }
    else if (pos == 0)
    {
        temp->next = head;
        p = head;
        while (p->next != head)
        {
            p = p->next;
        }
        p->next = temp;
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
