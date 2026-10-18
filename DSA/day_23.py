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