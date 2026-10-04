#Palindrome Linked List

total = []
arr= [1, 2, 2, 1]
for value in arr:
    total.append(value)
if total == total[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#flood_hill

image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
new_color = 2
old_color = image[sr][sc]
if old_color != new_color:
    stack = [(sr, sc)]
    while stack:
        r, c = stack.pop()
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            continue
        if image[r][c] != old_color:
            continue
        image[r][c] = new_color
        stack.append((r + 1, c))
        stack.append((r - 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))
print(image)

