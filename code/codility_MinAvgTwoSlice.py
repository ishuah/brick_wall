def solution(A):
    n = len(A)
    min_position = 0
    min_avg = (A[0] + A[1])/2.0
    for i in range(n-2):
        if min_avg > (A[i] + A[i+1])/2.0:
            min_avg = (A[i] + A[i+1])/2.0
            min_position = i
        if min_avg > (A[i] +A[i+1] + A[i+2])/3.0:
            min_avg = (A[i] + A[i+1] + A[i+2])/3.0
            min_position = i
    
    if min_avg > (A[-1] + A[-2])/2.0:
        min_avg = (A[-1] + A[-2])/2.0
        position = i
    return min_position