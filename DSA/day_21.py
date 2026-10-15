weight=[1,2,3,4,5,6,7]
h=6

left=max(weight)
right=sum(weight)

while left<right:
    mid=(left+right)//2
    count=1
    total=0

    for w in weight:
        if total+w>mid:
            count+=1
            total=0
        total+=w
    if count<=h:
        right=mid
    else:
        left=mid+1
print(left)
            
