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
