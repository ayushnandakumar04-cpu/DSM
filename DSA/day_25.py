#Jump Game
def junp(num):
    max_val=0

    for i in range(len(num)):
        if i>max_val:
            return False
        max_val=max(max_val+i,num[i])
    return True
num=[3,2,4,5,6]
print(junp(num))

#Insert Interval

def insert(interval,newInterval):
    res=[]
    for inteer in interval:
        if inteer[1]<newInterval[0]:
            res.append(inteer)
        elif inteer[1]>newInterval[0]:
            res.append(newInterval)
            inteer=newInterval
        else:
            newInterval[0]=min(inteer[0],newInterval[0])
            newInterval[1]=max(inteer[1],newInterval[1])
    res.append(newInterval)
    return res
interval = [[1, 3], [6, 9]]
newInterval = [2, 5]

print(insert(interval, newInterval))