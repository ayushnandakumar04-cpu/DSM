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

