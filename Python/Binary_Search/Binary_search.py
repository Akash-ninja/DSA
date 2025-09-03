import math

# array should be sorted
arr = [10, 14, 19, 23, 28, 45, 98, 103, 456]

search_key = 28


def binary_search_rec(arr, start, end, key):

    if start <= end:
        mid = math.floor((start + end) / 2)

        if key == arr[mid]:
            return mid
        elif arr[mid] < key:
            return binary_search_rec(arr, mid + 1, end, key)
        else:
            return binary_search_rec(arr, start, mid - 1, key)

    return -1


def binary_search(arr, start, end, key):

    while start <= end:
        mid = math.floor((start + end) / 2)

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return -1


position = binary_search(arr, 0, len(arr) - 1, search_key)

if position == -1:
    print(f"The key {search_key} is not present in the list")
else:
    print(f"The key {search_key} is present in the list at position: {position+1}")
