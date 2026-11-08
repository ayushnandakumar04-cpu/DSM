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
                  