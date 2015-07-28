def solution(N, A):
    counters = [0]*N
    max_counter = 0
    highest = 0
    for k,i in enumerate(A):
        if 1 <= i <= N:
            if max_counter > counters[i-1]:
                counters[i-1] = max_counter
            counters[i-1] += 1
            if highest < counters[i-1]:
                highest = counters[i-1]
        elif i == N+1:
            max_counter = highest
 
    for i in xrange(N):
        if counters[i] < max_counter:
            counters[i] = max_counter
    return counters