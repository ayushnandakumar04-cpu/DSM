#Lowest Common Ancestor of a Binary Search Tree
root=6
p=2
q=8

while root:
    if p < root and q < root:
        print(root.left)
    elif p > root and q > root:
        print(root.right)
    else:
        print(root)

#Climbing Stairs
n=4
a,b=1,1

for i in range(n-1):
    a,b=b,a+b
print(a,b)


