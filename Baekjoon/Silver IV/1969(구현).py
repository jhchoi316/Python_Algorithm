import sys
read = sys.stdin.readline

n, m = map(int, read().split())

dna = ["A", "C", "G", "T"]
distance = 0
s = ""
dnas = []

for i in range(n):
    data = read()
    dnas.append(data)
    
for i in range(m):
    a_count, c_count, g_count, t_count = 0, 0, 0, 0
    for j in range(n):
        if dnas[j][i]==dna[0]:
            a_count += 1
        elif dnas[j][i]==dna[1]:
            c_count += 1
        elif dnas[j][i]==dna[2]:
            g_count += 1
        elif dnas[j][i]==dna[3]:
            t_count += 1
    count_list = [a_count, c_count, g_count, t_count]
    selected_dna = dna[count_list.index(max(count_list))]
    s += selected_dna
    
    for k in range(n):
        if dnas[k][i] != selected_dna:
            distance += 1

print(s)
print(distance)