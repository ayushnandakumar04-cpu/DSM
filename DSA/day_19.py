#Implement Stack using Queues
from collections import deque

queue=deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop())
print(queue.pop())
print(queue.pop())

#Triangle

triangle=[[1,2],[3,4],[6,5,7],[4,1,8,7]]
d=triangle[:][-1]

for i in range(len(triangle)-2,-1,-1):
    for j in range(len(triangle[i])):
        d[j]=triangle[i][j]+min(d[j],d[j+1])
print(d[j])

#Palindrome Partitioning
s="abc"
res=[]

def backend(start,path):
    if len(s)==start:
        res.append(path[:])
        return

    for i in range(start,len(s)):
        p=s[start:i+1]

        if p==p[::-1]:
            path.append(p)
            backend(i+1,path)
            path.pop
            
backend(0, [])
print(res)

#Last Stone Weight
stone=[2,7,1,8,2,1]

while len(stone)>1:
    stone.sort()

    first=stone.pop()
    second=stone.pop()

    if first!=second:
        s=first-second
        stone.append(s)
        print(stone[0])
    
    