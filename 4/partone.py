def find_xmas_in_grid(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0),  # Up
        (1, 1),   # Down-Right (Diagonal)
        (-1, -1), # Up-Left (Diagonal)
        (1, -1),  # Down-Left (Diagonal)
        (-1, 1),  # Up-Right (Diagonal)
    ]
    occurrences = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x, y, direction):
        dx, dy = direction
        positions = []
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return None
            positions.append((nx, ny))
        return positions

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == word[0]:  # Check if starting character matches
                for direction in directions:
                    found = search_from(x, y, direction)
                    if found:
                        occurrences.append(found)

    return occurrences

with open("input", "r") as f:
    m = []
    for l in f.readlines():
        m.append(l.strip())
    print(len(find_xmas_in_grid(m)))