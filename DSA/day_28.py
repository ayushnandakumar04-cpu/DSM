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