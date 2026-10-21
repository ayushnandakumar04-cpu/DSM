grid = [
    ["1", "1", "0", "0"],
    ["1", "0", "0", "1"],
    ["0", "0", "1", "1"],
    ["0", "0", "0", "0"]
]

count = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "1":
            count += 1
            stack = [(i, j)]

            while stack:
                x, y = stack.pop()

                if (x < 0 or x >= len(grid) or
                    y < 0 or y >= len(grid[0]) or
                    grid[x][y] == "0"):
                    continue

                grid[x][y] = "0"

                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

print(count)

# is graphite bipartite
def isBipartite(graph):
    n = len(graph)
    color = [-1] * n

    for i in range(n):
        if color[i] == -1:
            queue = [i]
            color[i] = 0

            while queue:
                node = queue.pop(0)

                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)

                    elif color[neighbor] == color[node]:
                        return False

    return True
print(True)