#Boyer-Moore voting, or simple hashmap counting

def majority(n):
    cand=0
    count=0

    for num in n:
        if count==0:
            cand=num
        elif num==cand:
            count+=1
        else:
            count-=1
    return cand
n=[1,1,2,2,2]
print(majority(n))

def majority(n):
    count={}

    for num in n:
         count[num]=count.get(0,num)+1

         if count[num]>len(n)//2:
            return num

n=[1,1,2,2,2,2]
majority(n)
            

