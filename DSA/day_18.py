#Course Schedule
numcourse=2
prerequisite=[[1,0]]

graph=[[] for i in range(numcourse)]
indegree=[0]*numcourse
for course,p in prerequisite:
    graph[p].append(course)
    indegree[course]+=1

queue=[]
for i in range(numcourse):
    if indegree[i]==0:
      queue.append(i)
    

completed=0
while queue:
   course=queue.pop(0)
   completed+=1

   for r in graph[course]:
      indegree[r]-=1
      if indegree[r]==0:
        queue.append(r)
if completed==numcourse:
   print(True)
else:
   print(False)
      

#Find the Index of the First Occurrence in a String
heystack="sadbreak"
need="break"
for i in range(len(heystack)-len(need)+1):
   l=heystack[i:i+len(need)]==need
   print(i)
   break
   print("-1")
