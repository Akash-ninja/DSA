#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
};

Node *create(int A[], int n)
{
    Node *t;
    Node *last;

    Node *head = new Node;
    head->data = A[0];
    head->next = nullptr;
    last = head;

    for (int i = 1; i < n; i++)
    {
        t = new Node;
        t->data = A[i];
        t->next = nullptr;
        last->next = t;
        last = t;
    }

    return head;
}

void display(Node* p)
{
    while (p != NULL)
    {
        cout << " " << p->data;
        p = p->next;
    }
}

int main()
{
    cout << "Code Execution started...!\n";

    int A[] = {10, 70, 50, 39, 500, 1729, 2000};
    int n = sizeof(A) / sizeof(A[0]);

    Node *ptrHead = create(A, n);

    display(ptrHead);

    cout << endl;

    return 0;
}