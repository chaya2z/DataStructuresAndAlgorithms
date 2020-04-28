digit, nary = map(int, input().split())

A = [0] * digit


def k_string(n, k):
    if n < 1:
        print(A)
    else:
        for i in range(k):
            A[n - 1] = i
            k_string(n - 1, k)


k_string(digit, nary)
