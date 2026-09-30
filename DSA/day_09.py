#Balanced Binary Tree
class Node:
    def __init__(self,values):
        self.values=values
        self.left=None
        self.right=None

def binary(node):
    if node is None:
        return 0
    left=binary(node.left)
    right=binary(node.right)

    if abs(left-right)>1:
        return -1
    return max(left,right)+1

root = Node(1)
root.left = Node(2)
root.right = Node(3)

if binary(root) == -1:
    print("Balanced")
else:
    print("Not Balanced")
        
#Valid Parentheses
brackets="({[]})"
stack=[]

for i in brackets:
    if i in "([{":
        stack.append(i)
    else:
        print(False)
        break

    v=stack.pop()

    if (i=="(" and v!=")" ,
        i=="["and v!="]" , 
        i=="{"and v!="}"):
        print(False)
        break
print(len(stack)==0)