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

#Koko Eating Bananas

pile=[3,4,6,11]
h=9

left=0
right=max(pile)

while left<right:
    hr=(left+right)//2
    hour=0

    for p in pile:
        hour+=(p+hr-1)//hr

    if hour<=h:
        right=hr
    else:
        left=hr+1
print(left)


    
