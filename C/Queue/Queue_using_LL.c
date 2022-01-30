#include <stdio.h>
#include <stdlib.h>
#define CREATE_NODE (struct Node *)malloc(1 * sizeof(struct Node))

struct Node
{
    int data;
    struct Node *next;
} *front = NULL, *rear = NULL; // Global pointer

void enqueue(int data);
int dequeue();
int rearEnd();
int isEmpty();
int isFull();
void display(struct Node *p);

int main()
{
    printf("\n ----- QUEUE USING LINKED LIST IMPLEMENTATION ------ \n");

    while (1)
    {
        printf("\n");
        int op = 3, pos = -1, element = 0, x = -1;

        printf("Please select an operation first: \n");
        printf("1. En-queue an element \n");
        printf("2. De-queue an element \n");
        printf("3. Know the Rear-end element \n");
        printf("4. Display the Queue \n");
        printf("5. Exit \n");
        printf("Enter operation no.: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("Please enter data for Enqueuing: ");
            scanf("%d", &element);

            enqueue(element);

            printf("Element inserted \n");
            display(front);
            break;

        case 2:
            printf("De-queueing the element... \n");
            x = dequeue();

            if (x)
                printf("Element deleted is -> %d \n", x);

            display(front);
            break;

        case 3:
            x = rearEnd();

            if (!x)
                printf("Queue is empty \n");
            else
                printf("Rear end element is -> %d", x);
            break;

        case 4:
            display(front);
            break;

        case 5:
            return 0;

        default:
            break;
        }
    }

    return 0;
}

int isFull()
{
    struct Node *temp = CREATE_NODE;
    if (temp == NULL)
        return 0;

    return 1;
}

int isEmpty()
{
    if (front == NULL)
        return 0;

    return 1;
}

void display(struct Node *p)
{
    if (p == NULL)
        printf("** Empty Linked List **");

    while (p != NULL)
    {
        printf("%d ", p->data);
        p = p->next;
    }
}

int rearEnd()
{
    if (!isEmpty())
        return 0;

    return rear->data;
}

void enqueue(int data)
{
    if (!isFull())
        printf("Queue Full. Cannot create any node \n");

    struct Node *temp;

    temp = CREATE_NODE;
    temp->data = data;
    temp->next = NULL;

    if (front == NULL)
    {
        front = rear = temp;
        return;
    }

    rear->next = temp;
    rear = temp;
}

int dequeue()
{
    int poppedElement = 0;
    if (!isEmpty())
    {
        printf("Cannot de-queue. Queue is empty \n");
        return poppedElement;
    }

    struct Node *p = front;

    if (front->next == NULL)
        rear = front = NULL;
    else
        front = front->next;

    poppedElement = p->data;
    free(p);
    return poppedElement;
}