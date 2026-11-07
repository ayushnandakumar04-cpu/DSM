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

a="cbabcsd"
d="abc"
res=[]

for i in range(len(a)-len(d)+1):
    ana=a[i:i+len(d)]

    if sorted(ana)==sorted(d):
        res.append(i)
print(res)


