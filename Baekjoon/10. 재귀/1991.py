N = int(input())
tree = {}

for i in range(N):
    root, l_node, r_node = input().split()
    tree[root] = [l_node, r_node]

def preOrder(root):
    if root != '.':
        print(root, end="")
        preOrder(tree[root][0])
        preOrder(tree[root][1])

def inOrder(root):
    if root != '.':
        inOrder(tree[root][0])
        print(root, end="")
        inOrder(tree[root][1])

def postOrder(root):
    if root != '.':
        postOrder(tree[root][0])
        postOrder(tree[root][1])
        print(root, end="")

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')