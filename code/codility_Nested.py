def solution(S):
    stack = []
    for s in S:
        if s == ')':
            if stack != []:
                stack.pop()
            else:
                return 0
        else:
            stack.append('(')
    
    if stack != []:
        return 0
    return 1