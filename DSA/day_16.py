#String Compression

ch=["a","a","b","b","b"]
j=0
res=[]
while j<len(ch):
    c=ch[j]
    count=0
    while j<len(ch) and ch[j]==c:
        count +=1
        j+=1

    res.append(ch)
    if count > 1:
        res.extend(str(count))
print(res)

#Remove Linked List Elements

head=[1,2,3,4,6,6]
values=6
res=[]

for i in head:
    if i!=values:
        res.append(i)
print(res)


    