def solution(n, costs):
    answer = 0
    
    costs.sort(key = lambda x: x[2])
    vertex = set([costs[0][0]])
    
    while len(vertex) != n:
        for v in costs:
            if v[0] in vertex and v[1] in vertex:
                continue
                
            # 둘 중 하나라도 방문하지 않았다면
            if v[0] in vertex or v[1] in vertex:
                vertex.update([v[0], v[1]])
                answer += v[2]
                break

    return answer
