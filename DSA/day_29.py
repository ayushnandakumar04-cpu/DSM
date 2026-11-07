#Longest Consecutive Sequence
def consecutive(num):
    long=0
    right=set(num)

    for r in right:
        if r-1 not in right:
            current=r
            count=1
        while current-1 in right:
            current+=1
            count+=1

        long=max(long,r)
    return long

num=[-3,-4,-5,-6,1,2,3]
print(consecutive(num))

#Product of Array Except Self

def array(num):
  
    
    n=len(num)
    res=[1]*n

    prefix=1
    for i in range(n):
        res[i]=prefix
        prefix*=num[i]

    suffix=1
    for i in range(n-1,-1,-1):
        res[i]*=suffix
        suffix*=num[i]

    return res

num=[1,2,3,4]
print(array(num))
    


