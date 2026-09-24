#Squares of a Sorted Array
def remove_elements(n,val):
    while val in n:
        n.remove(val)
    return len(n)
n=[2,4,4,2]
val=2
print(remove_elements(n,val))
print(n)

#squares of a sorted array
n=[-4,-3,0,1,2,3]
res=[]
for num in n:
    res.append(num*num)
res.sort()
print(res)