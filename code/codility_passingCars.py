def solution(A):
    east = 0
    passing_pairs = 0
    
    for i in range(len(A)):
        if A[i] == 1:
            passing_pairs += east
            if passing_pairs > 1000000000:
                return -1
        else:
            east +=1
    return passing_pairs