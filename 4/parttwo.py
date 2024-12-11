def find_x_mas(grid):
    rows, cols = len(grid), len(grid[0])
    results = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_x_mas(x, y):
        # Define the diagonal patterns for the "X" shape
        top_left_to_bottom_right = [(x - 1, y - 1), (x, y), (x + 1, y + 1)]
        bottom_left_to_top_right = [(x + 1, y - 1), (x, y), (x - 1, y + 1)]

        def check_diagonal(diagonal):
            if all(is_valid(px, py) for px, py in diagonal):
                letters = [grid[px][py] for px, py in diagonal]
                return letters == ["M", "A", "S"] or letters == ["S", "A", "M"]
            return False

        # Check both diagonals
        return (
            check_diagonal(top_left_to_bottom_right)
            and check_diagonal(bottom_left_to_top_right)
        )

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == "A" and check_x_mas(x, y):
                results.append((x, y))

    return results

with open("input", "r") as f:
    m = []
    for l in f.readlines():
        m.append(l.strip())
    print(len(find_x_mas(m)))