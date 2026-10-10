#Fruit Into Baskets
fruits=[1,2,1,2,3]
l=0
basket={}
maximum=0

for r in range(len(fruits)):
    basket[fruits[r]]=basket.get("fruits[r]",0)+1

    while len(basket)>2:
        basket[fruits[l]] -=1

        if basket[fruits[l]]==0:
             del basket[fruits[l]]

        l+=1
    maximum=max(maximum,r-l+1)
print(maximum)

#Find All Anagrams in a String

s="cbabcde"
p="abc"

result=[]
for i in range(len(s)-len(p)+1):
    anag=s[i:i+len(p)]

    if sorted(anag)==sorted(p):
        result.append(i)
print(result)

