target=9
nums=[1,2,3,4]
seen={}
for i,num in enumerate(nums):
    diff=target-num
    if diff in seen:
      print(seen[diff],i)
    seen[num]=i
print(seen)