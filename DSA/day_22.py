#Combination Sum

candidates = [2, 3, 4, 6]
target = 9

res = []

def solve(i, total, path):
    if total == target:
        res.append(path[:])
        return

    if total > target or i == len(candidates):
        return

    solve(i, total + candidates[i], path + [candidates[i]])
    solve(i + 1, total, path)

solve(0, 0, [])
print(res)      

#Letter Combinations of a Phone Number
digit="24"
pno={
    "1":"abc",
    "2":"def",
    "3":"ghi",
    "4":"jkl",
    "5":"mno",
    "6":"pqrs"
}
res=[""]
for d in digit:
    temp=[]
    for comb in res:
        for l in pno[d]:
          temp.append(comb+l)
    res=temp
print(res)
