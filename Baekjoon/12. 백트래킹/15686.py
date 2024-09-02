import sys
n, m = map(int, input().split())

min_distance = sys.maxsize

home = []
chicken = []

for i in range(n):
    graph = list(map(int, input().split()))
    
    for j in range(n):
        if graph[j] == 1:
            home.append((i,j))
        elif graph[j] == 2:
            chicken.append((i,j))

visited = [False] * len(chicken)

def dfs(index, count):
    global min_distance
    
    if count == m:
        result = 0
        
        for i in home:
            distance = sys.maxsize
            for j in range(len(visited)):
                if visited[j]:
                    check = abs(i[0]-chicken[j][0]) + abs(i[1]-chicken[j][1])
                    distance = min(distance, check)
                
            result += distance
        min_distance = min(min_distance, result)
        
        return
        
    for i in range(index, len(chicken)):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, count+1)
            visited[i] = False
            

dfs(0,0)

print(min_distance)

# import sys
# from itertools import combinations

# input = sys.stdin.readline

# n, m = map(int, input().split())
# city = list(list(map(int, input().split())) for _ in range(n))
# result = 999999
# house = []      # 집의 좌표
# chick = []      # 치킨집의 좌표

# for i in range(n):
#     for j in range(n):
#         if city[i][j] == 1:
#             house.append([i, j])
#         elif city[i][j] == 2:
#             chick.append([i, j])

# for chi in combinations(chick, m):  # m개의 치킨집 선택
#     temp = 0            # 도시의 치킨 거리
#     for h in house: 
#         chi_len = 999   # 각 집마다 치킨 거리
#         for j in range(m):
#             chi_len = min(chi_len, abs(h[0] - chi[j][0]) + abs(h[1] - chi[j][1]))
#         temp += chi_len
#     result = min(result, temp)

# print(result)