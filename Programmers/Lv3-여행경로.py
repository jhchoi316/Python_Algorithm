def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def dfs(start, path): 
        # 모든 경로를 확인했을 경우, 추가
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        
        # start와 출발지가 같고, 방문하지 않았다면,
        for idx, ticket in enumerate(tickets):
            if ticket[0] == start and not visited[idx]:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False
                
    dfs("ICN", ["ICN"])

    answer.sort()
    
    return answer[0]