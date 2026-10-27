#can fish
def canfish(num,prerequisites):
    g=[[]for i in range(num)]
    indegree=[0]*num

    for a,b in prerequisites:
        g[b].append(a)
        indegree[a]+=1

    queue=[]

    for i in range(num):
        if indegree[i]==0:
          queue.append(i)

    count=0
    while queue:
        course = queue.pop(0)
        count += 1

        for next_course in g[course]:
            indegree[next_course] -= 1

            if indegree[next_course] == 0:
                queue.append(next_course)

    return count == num


num = 2
prerequisites = [[1, 0]]
print(canfish(num,prerequisites))
