# word pattern
p_t_n="abba"
w="cat dog dog cat"
ws=w.split()
map={}
for i in range(len(p_t_n)):
    if p_t_n[i] in map:
        if map[p_t_n[i]]!=ws[i]:
            print(False)
            break
    else:
        map[p_t_n[i]]=ws[i]
else:
   print(True)
    
#randsome note
r="a"
m="aa"
for char in r:
    if char in m:
        magazine=m.replace(char, "",1)
        print(False)
        break
else:
    print(True)

# missing

#

arr=[3,4,6]

max_num=max(arr)
min_num=min(arr)

total=0
for i in range(min_num,max_num+1):
    total=total+i

arr=sum(arr)
if arr!=total:
    print(total-arr,"missing")
else:
    print("no missing")