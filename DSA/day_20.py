#Edit Distance
word1="zebras"
word2="bas"

count=0

for i in range(min(len(word1),len(word2))):
    if word1[i]==word2[i]:
        count+=1

count+=abs(len(word1)-len(word2))
print(count)