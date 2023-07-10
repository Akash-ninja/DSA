#include <stdio.h>

struct Stack
{
    int size;
    int top;
    int *stackptr; // pointer to an array
};

void push(struct Stack *st, int data);
int pop(struct Stack *st);
int stackTop(struct Stack st);
int peek(struct Stack st, int pos); // data at particular 'index'
int isEmpty(struct Stack st);
int isFull(struct Stack st);
void display(struct Stack st);

int main()
{
    printf("\n ----- STACK USING ARRAY IMPLEMENTATION ------ \n");

    struct Stack st;
    st.top = -1;
    st.size = 50;

    int arr[st.size];
    st.stackptr = arr;

    while (1)
    {
        printf("\n");
        int op = 3, pos = -1, element = 0, x = -1;

        printf("Please select an operation first: \n");
        printf("1. Push an element \n");
        printf("2. Pop an element \n");
        printf("3. Know the Topmost element \n");
        printf("4. Know the element at particular position \n");
        printf("5. Display the Stack \n");
        printf("6. Exit \n");
        printf("Enter operation no.: ");
        scanf("%d", &op);

        switch (op)
        {
        case 1:
            printf("Please enter data for pushing: ");
            scanf("%d", &element);

            push(&st, element);

            printf("Element pushed \n");
            break;

        case 2:
            printf("Popping the element... \n");
            x = pop(&st);

            if (x)
                printf("Popped out element is -> %d \n", x);
            break;

        case 3:
            x = stackTop(st);

            if (!x)
                printf("Stack is empty \n");
            else
                printf("Topmost element is -> %d", x);
            break;

        case 4:
            printf("Please enter the position: ");
            scanf("%d", &pos);

            x = peek(st, pos);

            if (x)
                printf("Element at position %d is -> %d", pos, x);
            break;

        case 5:
            display(st);
            break;

        case 6:
            return 0;

        default:
            break;
        }
    }

    return 0;
}

int isFull(struct Stack st)
{
    if (st.top == st.size - 1)
        return 0;

    return 1;
}

int isEmpty(struct Stack st)
{
    if (st.top == -1)
        return 0;

    return 1;
}

void display(struct Stack st)
{
    if (!isEmpty(st))
    {
        printf("** Empty Stack ** \n");
        return;
    }

    for (int i = 0; i <= st.top; i++)
        printf("%d ", st.stackptr[i]);

    printf("\n");
}

int stackTop(struct Stack st)
{
    if (!isEmpty(st))
        return 0;

    return st.stackptr[st.top];
}

void push(struct Stack *st, int data)
{
    if (!isFull(*st))
        printf("Stack Overflow \n");

    st->top++;
    st->stackptr[st->top] = data;
}

int pop(struct Stack *st)
{
    int poppedElement = 0;
    if (!isEmpty(*st))
    {
        printf("Cannot pop. Stack is empty \n");
        return poppedElement;
    }

    poppedElement = st->stackptr[st->top];
    st->top--;
    return poppedElement;
}

int peek(struct Stack st, int pos)
{
    int x = 0;

    // since we are assuming stack operation from right end of array.
    // Therefore, index in stack is calculated
    if (st.top - pos + 1 < 0)
    {
        printf("Invalid position. Please try again \n");
        return x;
    }

    return x = st.stackptr[st.top - pos + 1];
}