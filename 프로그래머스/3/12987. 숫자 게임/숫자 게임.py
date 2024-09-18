def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    j = 0
    l = len(A)
    for i in range(l):
        if A[i] < B[j]:
            answer += 1
            j += 1
            if j == l:
                break
                
        
        
    
    return answer