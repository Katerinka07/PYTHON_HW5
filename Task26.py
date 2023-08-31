def multiplication(A, B):
    if B == 0:
        return 1
    return A *(multiplication(A, B - 1))
A = int(input('Введите положительное число: '))
B = int(input('Введите положительное число: '))

print(multiplication(A, B))