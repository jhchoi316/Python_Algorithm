from collections import deque

def solution(tickets):
    answer = []
    queue = deque()
    
    for i in range(len(tickets)):
        if tickets[i][0] == "ICN": 
            visited = [0 for _ in range(len(tickets))]
            visited[i] = -1
            queue.append([tickets[i][1], tickets[i], visited])
    
    while queue:
        a = queue.popleft()
        current, ans, visited = a[0], a[1], a[2]
        
        if len(ans) == len(tickets)+1:
            answer.append(ans)
            continue
            
        for i in range(len(tickets)):
            if tickets[i][0] == current:
                if visited[i] == 0:
                    new_visited = visited[:]
                    new_ans = ans[:]
                    new_visited[i] = -1
                    new_ans.append(tickets[i][1])
                    queue.append([tickets[i][1], new_ans, new_visited])

    answer.sort()
    return answer[0]

    