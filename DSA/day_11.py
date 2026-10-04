#maximum subarray
n=[-2,-1,1,2,-3,4,5,-6]
c=n[0]
m=n[0]
for i in range(1,len(n)):
    c=max(n[i],c+n[i])
    maximum=max(m,c)
print(maximum)

#Two Sum II - Input Array Is Sorted
arr=[2,8,12,18]
t=10
left=0
right=len(arr)-1

while left<right:
    tot=arr[left]+arr[right]
    if t==tot:
        print(left+1,right+1)
        break
    elif tot < t:
        left+=1
    else:
        right-=1

#Group Anagrams
word=["eat","tea","rat","ate","nat","ban"]
grp={}
for w in word:
    r="".join(sorted(w))
    if r not in grp:
        grp[r]=[]
    grp[r].append(w)
print(list(grp.values()))


        

