#include <stdio.h>

void InsertionSort(int A[], int n);

int main()
{
    printf("-------- INSERTION SORT --------- \n\n");
    int n, arr[50];

    printf("Enter no. of values: ");
    scanf("%d", &n);

    printf("Enter array of values (with spaces): ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    InsertionSort(arr, n);

    printf("\nValues after Sorting: ");
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }

    printf("\n");
    return 0;
}

void swap(int *p, int *q)
{
    int temp;

    temp = *p;
    *p = *q;
    *q = temp;
}

void InsertionSort(int A[], int n)
{
    int x, j;

    // for passes
    // This algo assumes first element is already sorted
    for (int i = 1; i < n; i++)
    {
        x = A[i];
        j = i - 1;

        // shift the elements if element greater than to be inserted
        while (j > -1 && A[j] > x)
        {
            A[j + 1] = A[j];
            j--;
        }

        // insert the element at the proper place
        A[j + 1] = x;
    }
}