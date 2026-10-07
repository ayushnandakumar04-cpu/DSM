#Capacity To Ship Packages Within D Days

arr=[1,2,3,4,5,6,7,8,9,10]
days=5

left=max(arr)
right=sum(arr)

while left<right:
    cap=(left+right)//2

    tot=0
    current=0
    req_days=1

    for weight in arr:
        if current+weight>cap:
            req_days+=1
            current=0

        current+=weight

    if req_days<=days:
        right=cap
    else:
        left=cap+1
print(left)        

#Same Tree
tree1=[1,2,3]
tree2=[4,5,6]
if tree1==tree2:
    print("same tree")
else:
    print("not same tree")

#Symmetric Tree

tree=[1,2,3,4,3,2,1]
left=[1,2,3]
right=[3,2,1]
if left==right[::-1]:
    print("symetric")
else:
    print("not symmetric")
