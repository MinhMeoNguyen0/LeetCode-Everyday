"""
LeetCode 200 - Number of Islands (BFS / DFS)

Given an m x n 2D binary grid of '1's (land) and '0's (water), return the
number of islands. An island is land cells connected horizontally or
vertically, surrounded by water. All four edges of the grid are water.

Example:
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ] -> 3

Approach - flood fill, count connected components of land:
    Scan every cell. Each unvisited '1' is a brand-new island: count it,
    then flood-fill from it to mark its whole connected land mass visited.
    Flipping '1' -> '0' in place means no separate visited set, and cells
    already claimed by an island are never recounted.

    Iterative DFS with an explicit stack (rather than recursion) avoids
    Python's recursion limit on long snake-shaped islands. A BFS queue
    works identically - see the folder's template.py for both skeletons.

    Every cell is processed at most once: O(m*n) time. Extra space is the
    stack/queue, O(min(m, n)) in the worst case.
"""


def num_islands(grid: list[list[str]]) -> int:
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue

            # Found an unclaimed '1' -> a brand-new island. Flood-fill
            # its whole connected land mass so it is never recounted.
            islands += 1
            stack = [(r, c)]
            grid[r][c] = "0"  # Mark visited in place.

            while stack:
                cr, cc = stack.pop()
                # Four neighbors only: up, down, left, right (no diagonals).
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    # Bounds check first, then "is it unvisited land?".
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))

    return islands


if __name__ == "__main__":
    assert num_islands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]) == 1
    assert num_islands([
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]) == 3
    assert num_islands([["0", "0"], ["0", "0"]]) == 0
    assert num_islands([["1"]]) == 1
    assert num_islands([
        ["1", "0", "1"],
        ["0", "0", "0"],
        ["1", "0", "1"],
    ]) == 4
    assert num_islands([]) == 0
    print("All Number of Islands checks passed.")
