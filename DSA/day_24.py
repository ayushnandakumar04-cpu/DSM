#Surrounded Regions

bound=[
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","O","X","X"],
    ["X","X","O","X"]
]
r=len(bound)
c=len(bound[0])

def chain(i,j):
    if i<0 or i>=r or j<0 or j>=c:
        return
    if bound[i][j]!=0:
        return
    bound[i][j]="#"

    chain(i+1,j)
    chain(i-1,j)
    chain(i,j+1)
    chain(i,j-1)

for i in range(r):   
    chain(i,0)
    chain(i,c-1)
for j in range(c):
    chain(0,j)
    chain(r-1,j)


for i in range(r):
    for j in range(c):
        if bound[i][j]=="O":

            bound[i][j]="X"
        elif bound[i][j]=="#":
            bound[i][j]="O"

for row in bound:
    print(row)
