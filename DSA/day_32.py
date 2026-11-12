sta="hadnothad"
ne="had"

result=-1

for i in range(len(sta)-len(ne)+1):
    if sta[i:i+len(ne)]==ne:
        result=i
        break
print(result)