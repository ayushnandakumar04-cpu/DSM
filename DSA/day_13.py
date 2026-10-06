#Binary Search
num=[1,2,3,4,6,8]
target=8
left=0
right=len(num)-1
while left<=right:
    m=left+right//2
    if num[m]==target:
        print("found")
        break
    elif num[m]<=target:
        left+=1
    else:
        right-=1
else:
    print("Not found")


#Search Insert Position

arr=[1,2,5,6]
tar=5
left=0
right=len(arr)-1

while left<right:
    m=left+right//2
    if arr[m]==tar:
        print(m)
        break
    elif arr[m]<tar:
        left+=1
    else:
        right-=1
else:
    print(left)

# First Bad Version

arr=[1,3,4,5]
first_bad= 8

left=0
right=len(arr)-1

while left<right:
    m=left+right//2
    if arr[m]==first_bad:
        print(m)
        break    
    elif arr[m]<=first_bad:
        left+=1
    else:
        right-=1
else:
    print(first_bad)



