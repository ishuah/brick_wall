def solution(A):
    return list(set(range(1, len(A)+2)) - set(A))[0]