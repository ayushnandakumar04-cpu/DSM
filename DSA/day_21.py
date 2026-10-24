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
            
#maximu product array

def maxProduct(n):
    max_pro=n[0]
    min_pro=n[0]
    res=[]

    for i in range(1,len(n)):
        if n[i]<0:
            max_pro,min_pro=min_pro,max_pro
        max_pro=max(n[i],max_pro*n[i])
        min_pro=min(max_pro*n[i],n[i])

        res=max(max_pro,min_pro)

    return res
n=[3,4,-5,-7]
print(maxProduct(n))

#Top K Frequent Words

def topkfrequent(words,k):
    count={}
    for w in words:
        count[w]=count.get(w,0)+1
    count=sorted(count.items(),key=lambda x:(-x[1],x[0]))

    return [w[0] for w in count[:k]]

words=["i","love","leetcode"]
k=3
print(topkfrequent(words,k))
