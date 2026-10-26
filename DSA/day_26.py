#Merge k Sorted Lists

import heapq

def merge(lists):

    heap=[]
    res=[]

    for i in range(len(lists)):
        for v in lists[i]:
            heapq.heappush(heap,v)
    while heap:
        res.append(heapq.heappop(heap))
    return res

lists=[[1,2,3],[4,5],[9,8]]
print(merge(lists))
    
#Implement Trie (Prefix Tree)

trie = {}

def insert(word):
    current = trie

    for ch in word:
        if ch not in current:
            current[ch] = {}
        current = current[ch]

    current["*"] = True


def search(word):
    current = trie

    for ch in word:
        if ch not in current:
            return False
        current = current[ch]

    return "*" in current


def startsWith(prefix):
    current = trie

    for ch in prefix:
        if ch not in current:
            return False
        current = current[ch]

    return True


insert("apple")
print(search("apple"))
print(search("app"))
print(startsWith("app"))

insert("app")
print(search("app"))