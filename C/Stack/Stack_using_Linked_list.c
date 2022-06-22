#include <stdio.h>
#include <stdlib.h>
#define CREATE_NODE (struct Node *)malloc(1 * sizeof(struct Node))

struct Node
{
    int data;
    struct Node *next;
} *top = NULL; // Global pointer

/* Assumption: Every operation done before first node */

void push(int data);
int pop();
int stackTop();
int peek(int pos); // data at particular 'index'
int isEmpty();
int isFull();
void display(struct Node *p);
int countNodes(struct Node *p);

int main()
{
    printf("\n ----- STACK USING LINKED LIST IMPLEMENTATION ------ \n");

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

            push(element);

            printf("Element pushed \n");
            display(top);
            break;

        case 2:
            printf("Popping the element... \n");
            x = pop();

            if (x)
                printf("Popped out element is -> %d \n", x);

            display(top);
            break;

        case 3:
            x = stackTop();

            if (!x)
                printf("Stack is empty \n");
            else
                printf("Topmost element is -> %d", x);
            break;

        case 4:
            printf("Please enter the position: ");
            scanf("%d", &pos);
            if (pos > countNodes(top))
            {
                printf("Position not available. Please try again. \n");
                break;
            }

            x = peek(pos);

            if (x)
                printf("Element at position %d is -> %d", pos, x);
            break;

        case 5:
            display(top);
            break;

        case 6:
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
    if (top == NULL)
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

int stackTop()
{
    if (!isEmpty())
        return 0;

    return top->data;
}

void push(int data)
{
    if (!isFull(top))
        printf("Stack Overflow \n");

    struct Node *temp;

    temp = CREATE_NODE;
    temp->data = data;
    temp->next = top;
    top = temp;
}

int pop()
{
    int poppedElement = 0;
    if (!isEmpty())
    {
        printf("Cannot pop. Stack is empty \n");
        return poppedElement;
    }

    struct Node *p = top;
    top = top->next;
    poppedElement = p->data;
    free(p);
    return poppedElement;
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

int peek(int pos)
{
    struct Node *p = top;

    if (!p)
        return 0;

    for (int i = 2; p != NULL && i <= pos; i++)
        p = p->next;

    return p->data;
}