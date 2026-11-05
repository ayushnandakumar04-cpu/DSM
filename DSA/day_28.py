#Daily Temperatures

temp=[78,23,33,44,54,68,89]
res=[0]*len(temp)
stack=[]

for i in range(len(temp)):
    while stack and temp[i]>temp[stack[-1]]:
        p=stack.pop()
        res[p]=i-p
    stack.append(i)

print(res)

#Container With Most Water

arr=[1,2,9,5,7,8,9,0]
max_water=0
left=0
right=len(arr)-1

while left<right:
    m=right-left
    h=min(arr[left],arr[right])

    water=m*h
    l=max(max_water,water)
    if arr[left]<arr[right]:
        left+=1
    else:
        right-=1
print(l)



