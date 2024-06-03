#include <stdio.h>

int LinearSearch(int A[], int n, int key);

int main()
{
    printf("-------- LINEAR SEARCH --------- \n\n");
    int n, arr[50], key, foundIndex;

    printf("Enter no. of values: ");
    scanf("%d", &n);

    printf("Enter array of values (with spaces): ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter the key for searching: ");
    scanf("%d", &key);

    foundIndex = LinearSearch(arr, n, key);

    if (foundIndex != -1)
    {
        printf("Element found at position %d\n", foundIndex);
    }
    else
        printf("Element not found\n");

    printf("\n");
    return 0;
}

int LinearSearch(int A[], int n, int key)
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (key == A[i])
        {
            return i + 1;
        }
    }

    return -1;
}


/** There are 2 other ways of doing Linear search - 
    These methods are dedicated for repeated search (i.e., if the search happens atleast 2 times)
        1. Transposition (Move the element by one position)
        2. Move the key to front (Move the element in the beginning)


    Code 1: Transposition:
            for (i=0; i<arrayLength; i++) 
            {
                if (key == A[i])
                {
                    swap(A[i], A[i-1])
                    return i-1
                }
            }

    Code 2: Move the element to front
            for (i=0; i<arrayLength; i++) 
            {
                if (key == A[i])
                {
                    swap(A[i], A[0])
                    return i-1
                }
            }
 **/