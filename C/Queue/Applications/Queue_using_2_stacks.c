#include <stdio.h>

struct Stack
{
    int size;
    int top;
    int *stackptr;
};

void enqueue(struct Stack *st, int data);
int dequeue(struct Stack *st1, struct Stack *st2);
void display(struct Stack st1, struct Stack st2);

void push(struct Stack *st, int data);
int pop(struct Stack *st);
int isEmpty(struct Stack st);
int isFull(struct Stack st);

int main()
{
    printf("\n ----- QUEUE USING 2 STACKS ------ \n");

    // initialize stack S1
    struct Stack st1;
    st1.top = -1;
    st1.size = 10;

    int arr1[st1.size];
    st1.stackptr = arr1;

    // initialize stack S2
    struct Stack st2;
    st2.top = -1;
    st2.size = 10;

    int arr2[st2.size];
    st2.stackptr = arr2;

    while (1)
    {
        printf("\n");
        int op = 3, pos = -1, element = 0, x = -1;

        printf("Please select an operation first: \n");
        printf("1. En-queue an element \n");
        printf("2. De-queue an element \n");
        printf("3. Display the queue \n");
        printf("4. Exit \n");
        printf("Enter operation no.: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("Please enter data for En-queuing: ");
            scanf("%d", &element);

            enqueue(&st1, element);
            break;

        case 2:
            printf("De-queuing the element... \n");
            x = dequeue(&st1, &st2);

            if (x != -1)
                printf("Popped out element is -> %d \n", x);
            break;

        case 3:
            display(st1, st2);
            break;

        case 4:
            return 0;

        default:
            break;
        }
    }

    return 0;
}

int isEmpty(struct Stack st)
{
    if (st.top == -1)
        return 1;

    return 0;
}

int isFull(struct Stack st)
{
    if (st.top == st.size - 1)
        return 1;

    return 0;
}

void push(struct Stack *st, int data)
{
    if (isFull(*st))
    {
        printf("Stack Overflow \n");
        return;
    }

    st->top++;
    st->stackptr[st->top] = data;

    printf("Element Inserted \n");
}

int pop(struct Stack *st)
{
    int poppedElement = 0;
    if (isEmpty(*st))
    {
        printf("Cannot pop. Stack is empty \n");
        return poppedElement;
    }

    poppedElement = st->stackptr[st->top];
    st->top--;
    return poppedElement;
}

void enqueue(struct Stack *st, int data)
{
    push(*(&st), data);
}

int dequeue(struct Stack *st1, struct Stack *st2)
{
    int x = -1, tdata = 0;

    if (isEmpty(*st2))
    {
        if (isEmpty(*st1))
        {
            printf("Cannot De-queue. Queue is empty \n");
            return x;
        }
        else
        {
            while (!isEmpty(*st1))
            {
                tdata = pop(*(&st1));
                push(*(&st2), tdata);
            }
        }
    }

    return pop(*(&st2));
}

void display(struct Stack st1, struct Stack st2)
{
    int i = st2.top, j = 0;
    printf("\n");

    printf("Queue is-> ");
    if (isEmpty(st2) && isEmpty(st1))
    {
        printf("Queue is empty. Nothing to display \n");
        return;
    }

    while (!isEmpty(st2) && i > -1)
    {
        printf("%d ", st2.stackptr[i]);
        i--;
    }
    while (!isEmpty(st1) && j <= st1.top)
    {
        printf("%d ", st1.stackptr[j]);
        j++;
    }

    printf("\n");
}
