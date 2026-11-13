sta="hadnothad"
ne="had"

result=-1

for i in range(len(sta)-len(ne)+1):
    if sta[i:i+len(ne)]==ne:
        result=i
        break
print(result)

#Asteroid Collision

def asteroid(aster):
    stack=[]

    for a in aster:
        while stack and a<0 and stack[-1]>0:
            if stack[-1]<abs(a):
                stack.pop()
                continue
            elif stack[-1]==abs(a):
                stack.pop()
            break
        else:

          stack.append(a)
    return stack

aster=[2,4,-2]
print(asteroid(aster))