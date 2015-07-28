def solution(X, A):
    leaves_needed = X
    leaves_dropped_positions = [-1]*X
    for i in xrange(len(A)):
        if leaves_dropped_positions[A[i]-1] == -1:
            leaves_dropped_positions[A[i]-1] = i
            leaves_needed -= 1
            if leaves_needed == 0:
                return i
    return -1