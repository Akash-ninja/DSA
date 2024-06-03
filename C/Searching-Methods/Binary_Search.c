#include<stdio.h>

int IBinarySearch(int A[], int n, int key);
int RBinarySearch(int A[], int low, int high, int key);

int main()
{
    printf("-------- BINARY SEARCH --------- \n\n");
    int n, arr[50], key, foundIndex;

    printf("Enter no. of values: ");
    scanf("%d", &n);

    printf("Enter array of values (with spaces and in sorted manner): ");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    printf("Enter the key for searching: ");
    scanf("%d", &key);

    // foundIndex = IBinarySearch(arr, n, key);
    int low=0, high=n-1;
    foundIndex = RBinarySearch(arr, low, high, key);

    if (foundIndex != -1)
    {
        printf("Element found at position %d\n", foundIndex+1);
    }
    else
        printf("Element not found\n");

    printf("\n");
    return 0;
}

int IBinarySearch(int A[], int n, int key)
{
    int low=0, high=n-1, mid=-1;

    while(low <= high) 
    {
        mid = (low + high)/2;

        if (key == A[mid]) return mid;
        else if (key < A[mid]) high = mid - 1;
        else low = mid + 1;
    }

    return -1;
}

int RBinarySearch(int A[], int low, int high, int key)
{
    int mid;

    if (low <= high)
    {
        mid = (low + high)/2;

        if (key == A[mid]) return mid;
        else if(key < A[mid]) return RBinarySearch(A, low, mid-1, key);
        else return RBinarySearch(A, mid+1, high, key);
    }

    return -1;
}