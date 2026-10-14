#Edit Distance
word1="zebras"
word2="bas"

count=0

for i in range(min(len(word1),len(word2))):
    if word1[i]==word2[i]:
        count+=1

count+=abs(len(word1)-len(word2))
print(count)

#Merge k Sorted Lists

list=[[2,3,3],[4,5,6],[2,8]]
res=[]

for l in list:
    res+=l
res.sort()
print(res)