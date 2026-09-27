#Maximum Average Subarray I
arr=[2,3,4,5,6,-1]
k=4
w_s=sum(arr[:4])
m=w_s
for i in range(k,len(arr)):
    w_s=w_s+arr[i]-arr[i-k]
    m=max(w_s,m)
    d=m/k
print(d)

#Valid Anagram
word1="anagram"
word2="nagaram"
w1=sorted(word1)
w2=sorted(word2)
if  w1==w2:
    print("anagram")
else:
    print("not anagram")

#Roman to Integer
word="IX"
values={
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
tot=0
for i in range(len(word)):
    if i+1<len(word) and values[word[i]]<values[word[i+1]]:
        tot-=values[word[i]]
    else:
        tot+=values[word[i]]
print(tot) 