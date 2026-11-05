#Remove Duplicates from Sorted Array

n=[1,1,2,2,3,3]
j=1

for i in range(1,len(n)):
    if n[i]!=n[i-1]:
        n[j]=n[i]
        j+=1
print(n[:j])

#Reverse String
s = "float"
rev=s[::-1]
print(rev)

#Valid Palindrome
d = "madam"
if d == d[::-1]:
    print("valid")
else:
    print("not valid")

#two pair sum

num=[1,2,3,4]
tar=6

for n in num:
    diff =tar-n

if diff in num :
    print(diff,n)
