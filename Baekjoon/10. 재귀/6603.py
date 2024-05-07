arr =[]
resultList = []

def comb(startIndex, curCount, resultList ,visited, k):
    if curCount == 6:
        print(*resultList)
        return
    
    for i in range(startIndex, k):
        if visited[i] == 0:
            visited[i] = 1
            resultList.append(arr[i])
            comb(i+1, curCount+1, resultList, visited, k)
            resultList.pop()
            visited[i] = 0

while True:
    inputList = list(map(int, input().split()))
    
    if len(inputList) == 1:
        break
    else:
        k = inputList[0]
        visited = [0] * k
        arr = inputList[1:]
        comb(0, 0, resultList, visited, k)
        print()