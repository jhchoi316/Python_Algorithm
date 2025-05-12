def solution(A,B):
    answer = 0

    sort_A = sorted(A)
    sort_B = sorted(B, reverse=True)
    
    for i in range(len(sort_A)):
        answer += sort_A[i] * sort_B[i]
            

    return answer