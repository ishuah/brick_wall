# O(N) 
def solution(A):
    N = len(A)
    first = A[0]
    last = sum(A[1:])
    min = abs(first - last)
    for n in xrange(1, N-1):
        first += A[n]
        last -= A[n]
        if min > abs(first-last):
            min = abs(first-last)
    return min