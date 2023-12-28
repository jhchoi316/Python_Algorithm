numbers1 = list(map(int,input().split(" ")))
numbers2 = list(map(int,input().split(" ")))
numbers3 = list(map(int,input().split(" ")))

def get_output(numbers):
    
    if numbers.count(0) == 0:
        print('E')
    elif numbers.count(0) == 1:
        print('A')
    elif numbers.count(0) == 2:
        print('B')
    elif numbers.count(0) == 3:
        print('C')
    elif numbers.count(0) == 4:
        print('D')
          
get_output(numbers1)
get_output(numbers2)
get_output(numbers3)

