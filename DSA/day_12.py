#Middle of the Linked List
def middle(head):
    fast=head
    slow=head

    while f in fast:

       f=fast.next
       slow=slow.next

    return slow

#Reorder List

v=[1,2,3,4,5]
res=[]

l=0
r=len(v)-1

while l<=r:
    res.append(v[l])
    if l!=r:
      res.append(v[r])
    l+=1
    r-=1
print(res)

#Min Stack

stack=[]

stack.append(5)
stack.append(3)
stack.append(8)
stack.append(1)

print("Stack:",stack)
print("Minimum:",min(stack))

stack.pop()

print("after pop:",stack)
print("minimum:",min(stack))