#include <stdio.h>

void BubbleSort(int A[], int n);

int main()
{
    printf("-------- BUBBLE SORT --------- \n\n");
    int n, arr[50];

    printf("Enter no. of values: ");
    scanf("%d", &n);

    printf("Enter array of values (with spaces): ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    BubbleSort(arr, n);

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

void BubbleSort(int A[], int n)
{
    int flag;

    // for passes
    for (int i = 0; i < n - 1; i++)
    {
        flag = 0;

        // heaviest element is sorted (thereby reducing no. of comparison)
        for (int j = 0; j < n - 1 - i; j++)
        {
            if (A[j] > A[j + 1])
            {
                swap(&A[j], &A[j + 1]);
                flag = 1;
            }
        }

        // makes algorithm adaptive - dont check for comparison if array is already sorted
        if (flag == 0)
            break;
    }
}