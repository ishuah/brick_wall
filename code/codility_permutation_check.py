def solution(A):
    N = len(A)
    perm_check = [0]*N
    for i in A:
        if not 1 <= i <= N:
            return 0
        else:
            if perm_check[i-1] != 0:
                return 0
            else:
                perm_check[i-1] += 1
    return 1