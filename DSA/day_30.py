t='hgrt'
s='ouyb'

if len(s)!=len(t):
    res= False

else:
    s_dict={}
    t_dict={}
    res=True

    for i in range(len(s)):
        if s[i] in s_dict:
            if s_dict[s[i]]!=t[i]:
                res=False
                break
            else:
                s_dict[s[i]]=t[i]

            if t[i] in t_dict:

              if t_dict[t[i]]!=s[i]:
                  res=False
                  break
              else:
                  t_dict[t[i]]=s[i]
print(res)

# Zigzag Conversion

s="PAYPHSADBTYION"
num=3

if num==1 or num>=len(s):
    print(s)
else:
    r=[""]*num
    current=0
    direction=1

    for c in s:
        r[current]+=c

        if current==0:
            direction=1
        elif current==num-1:
            direction=-1

        current+=direction

        result=""
    for row in r:
        result+=row
    print(result)



