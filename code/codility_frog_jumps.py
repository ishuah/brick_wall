def solution(X, Y, D):
    d = Y - X
    hops = d/D
    if d%D > 0:
        hops +=1
    return hops