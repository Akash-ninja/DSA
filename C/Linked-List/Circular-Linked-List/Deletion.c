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
int circularDelete(int pos);
void createList(int A[], int n);

int main()
{
    printf("------- CIRCULAR LINKED LIST DELETION ------ \n");

    while (1)
    {
        printf("\n\n");
        int op = 5, pos = -1, n, arr[50], x;
        printf("Please select an operation first: \n");
        printf("1. Create List using Array values \n");
        printf("2. Delete first node \n");
        printf("3. Delete at Any position \n");
        printf("4. Delete Last node \n");
        printf("5. Display my list \n");
        printf("6. Exit \n");
        printf("Enter operation no.: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("Enter no. of values you want to enter: ");
            scanf("%d", &n);
            printf("Enter values (with spaces): ");
            for (int i = 0; i < n; i++)
            {
                scanf("%d", &arr[i]);
            }
            createList(arr, n);
            printf("Linked list created successfully... \n");
            display(head);
            break;

        case 2:
            printf("Deleting in first position... \n");
            x = circularDelete(0);
            if (x == -1)
                printf("Cannot delete, List is empty \n");
            else
            {
                printf("Element deleted is - %d \n", x);
            }
            display(head);
            break;

        case 3:
            printf("Please enter the position: ");
            scanf("%d", &pos);
            if (pos >= countNodes(head))
            {
                printf("Position not available. Please try again. \n");
                break;
            }

            x = circularDelete(pos);
            if (x == -1)
                printf("Cannot delete, List is empty \n");
            else
                printf("Element deleted is - %d \n", x);

            display(head);
            break;

        case 4:
            printf("Deleting in last position... \n");
            pos = countNodes(head);

            x = circularDelete(pos);
            if (x == -1)
                printf("Cannot delete, List is empty \n");
            else
                printf("Element deleted is - %d \n", x);

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
        printf("** Empty Linked List **");

    do
    {
        printf("%d ", p->data);
        p = p->next;
    } while (p != head);
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

int circularDelete(int pos)
{
    int deletedData = -1;
    struct Node *p, *q;

    if (head == NULL)
        return deletedData;

    if (pos == 0 || countNodes(head) == 1)
    {
        p = head;
        while (p->next != head)
            p = p->next;

        p->next = head->next;
        deletedData = p->data;
        free(p);

        if (countNodes(head) == 1)
            head = NULL;
    }
    else
    {
        p = head;
        q = NULL;
        for (int i = 2; i <= pos; i++)
        {
            q = p;
            p = p->next;
        }
        if (q->next)
            q->next = p->next;

        deletedData = p->data;
        free(p);
    }
    return deletedData;
}

void createList(int A[], int n)
{
    struct Node *p, *temp;

    head = CREATE_NODE;
    head->data = A[0];
    head->next = head;
    p = head;

    for (int i = 1; i < n; i++)
    {
        temp = CREATE_NODE;
        temp->data = A[i];
        temp->next = p->next;
        p->next = temp;
        p = temp;
    }
}