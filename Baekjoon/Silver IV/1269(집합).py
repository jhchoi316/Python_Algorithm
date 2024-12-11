a, b = map(int, input().split())
line_a = set(map(int,input().split()))
line_b = set(map(int, input().split()))

print(len(line_a - line_b)+ len(line_b - line_a))