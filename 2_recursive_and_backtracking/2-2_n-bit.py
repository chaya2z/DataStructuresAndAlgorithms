bit: int = int(input())

A = [0] * bit


def binary(n):
    if n < 1:
        print(A)
    else:
        A[n - 1] = 0
        binary(n - 1)
        A[n - 1] = 1
        binary(n - 1)


binary(bit)
