def solution(A):
    mirror = [0]*(len(A)+1)
    for i in A:
        if 1 <= i <= len(A)+1:
            mirror[i-1] += 1
    for i in xrange(len(A)+1):
        if mirror[i] == 0:
            return i+1
    return -1