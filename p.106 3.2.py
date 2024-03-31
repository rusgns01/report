def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1
data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print(data)
sequential_search(data, 10)
