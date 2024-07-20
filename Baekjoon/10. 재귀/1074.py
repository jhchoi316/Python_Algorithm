N, r, c = list(map(int, input().split()))

def func(N, r, c):
    if N == 1:
        return 2 * r + c
    # 2사분면
    if r < (2**N)//2 and c < (2**N)//2:
        return func(N-1, r, c)
    # 1사분면
    elif r < (2**N)//2 and c >= (2**N)//2:
        return 2**(2*N-2) + func(N-1, r, c-2**(N-1))
    # 3사분면
    elif r >= (2**N)//2 and c < (2**N)//2:
        return 2**(2*N-1) + func(N-1, r-2**(N-1), c)
    # 4사분면
    elif r >= (2**N)//2 and c >= (2**N)//2:
        return 3*2**(2*N-2) + func(N-1, r-2**(N-1), c-2**(N-1))

print(func(N, r, c))