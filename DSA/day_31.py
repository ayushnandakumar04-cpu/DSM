s="ABCADY"
k=1
l=0
max_value=0
max_length=0
count={}

for r in range(len(s)):
    count[s[r]]=count.get(s[r],0)+1
    max_value=max(max_value,count[s[r]])

    while (r-l+1)-max_value+1>k:
        count[s[l]]-=l
        l+=1

    max_length=max(max_length,(r-l+1))
print(max_length)
