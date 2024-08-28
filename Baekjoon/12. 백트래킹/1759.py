def dfs(start, visited, result):
    global n, m
    check = 0
    for i in range(5):
        if vowels[i] in result:
            check += 1
    
    if len(result) == n and 0<check<n-1:
        print(''.join(map(str, result)))
        check = 0
        return

    for i in range(start, m):
        if not visited[i]:
            result.append(alpha[i])
            visited[i] = True
            dfs(i+1, visited, result)
            result.pop()
            visited[i] = False
        
n, m = map(int, input().split())
alpha = list(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
alpha.sort()
visited = [False]*m
result = []

dfs(0, visited, result)