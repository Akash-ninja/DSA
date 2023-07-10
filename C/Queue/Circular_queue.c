#include <stdio.h>

struct Queue
{
    int front;
    int rear;
    int size;
    int *queueptr; // pointer to an array
};

// Assumption made: Don't insert '0' as an element

void enqueue(struct Queue *q, int data);
int dequeue(struct Queue *q);
int rearEnd(struct Queue q);
int isEmpty(struct Queue q);
int isFull(struct Queue q);
void display(struct Queue q);

int main()
{
    printf("\n ----- CIRCULAR QUEUE USING ARRAY IMPLEMENTATION ------ \n");

    struct Queue q;
    q.front = q.rear = 0;
    q.size = 6;

    // making every index data as 0 so that ony non-zero value will be displayed
    // and giving array subscript as constant '6' (euivalent to size of Queue) as its not taking dynamic size 
    int arr[6] = {0};
    q.queueptr = arr;

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

            enqueue(&q, element);

            display(q);
            break;

        case 2:
            printf("De-queueing the element... \n");
            x = dequeue(&q);

            if (x)
                printf("Element deleted is -> %d \n", x);

            display(q);
            break;

        case 3:
            x = rearEnd(q);

            if (!x)
                printf("Queue is empty \n");
            else
                printf("Rear end element is -> %d", x);
            break;

        case 4:
            display(q);
            break;

        case 5:
            return 0;

        default:
            break;
        }
    }

    return 0;
}

int isFull(struct Queue q)
{
    if (((q.rear + 1) % q.size) == q.front)
        return 0;

    return 1;
}

int isEmpty(struct Queue q)
{
    if (q.front == q.rear)
        return 0;

    return 1;
}

void display(struct Queue q)
{
    if (!isEmpty(q))
    {
        printf("** Empty Queue ** \n");
        return;
    }

    int i = q.front + 1;
    while (i != q.front && q.queueptr[i] != 0)
    {
        printf("%d ", q.queueptr[i]);
        i = (i + 1) % q.size;
    }
    printf("\n");
}

int rearEnd(struct Queue q)
{
    if (!isEmpty(q))
        return 0;

    return q.queueptr[q.rear];
}

void enqueue(struct Queue *q, int data)
{
    if (!isFull(*q))
    {
        printf("Cannnot insert data. Queue is Full \n");
        return;
    }

    q->rear = (q->rear + 1) % q->size;
    q->queueptr[q->rear] = data;

    printf("Element inserted \n");
}

int dequeue(struct Queue *q)
{
    int poppedElement = 0;
    if (!isEmpty(*q))
    {
        printf("Cannot de-queue. Stack is empty \n");
        return poppedElement;
    }

    q->front = (q->front + 1) % q->size;
    poppedElement = q->queueptr[q->front];
    q->queueptr[q->front] = 0;
    return poppedElement;
}