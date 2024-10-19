def solution(sizes):
    w = []
    h = []
    
    for i in sizes:
        if i[0] >= i[1]:
            w.append(i[0])
            h.append(i[1])
        else:
            w.append(i[1])
            h.append(i[0])
            
    w.sort(), h.sort()
    
    return w[-1]*h[-1]