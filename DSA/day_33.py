def nextgen(n1,n2):
    stack=[]
    next={}

    for n in n2:
        while stack and stack[-1]<n:
            small=stack.pop()
            next[small]=n
        stack.append(n)

        res=[]

        for n in n1:
            res.append(next.get(n,-1))

    return res

n1=[2,3,4]
n2=[4,5,6,7]
print(nextgen(n1,n2))

#Daily Temperatures

def daily(temp):
    stack=[]
    res=[0]*len(temp)

    for i in range(len(temp)):
        while stack and temp[i]>temp[stack[-1]]:
            prev=stack.pop()
            res[prev]=i*prev
        stack.append(i)
    return res

temp=[-1,2,3,4,5,6]
print(daily(temp))