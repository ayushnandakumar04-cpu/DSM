# move zeroes
num = [0, 1, 0, 2, 3]
j=0
for i in range(0,len(num)):
    if num[i]!=0:
        num[j],num[i]=num[i],num[j]
        j+=1
print(num)

#Single Number
num=[2,2,1]
res=0
for n in num:
    res=res^n
print(res)

#Majority Element
nums = [2, 2, 3]

for n in nums:
    if nums.count(n) > len(nums)//2:
        print(n)
        break