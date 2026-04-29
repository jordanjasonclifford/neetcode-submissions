class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if grid is empty, no islands
        if not grid:
            return 0

        # number of rows
        ROWS = len(grid)

        # number of columns
        COLS = len(grid[0])

        # track visited cells so we don’t revisit
        visited = set()

        # count of islands
        islands = 0

        # directions: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            # queue for BFS
            q = deque()

            # start from this cell
            q.append((r, c))

            # mark it visited
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                # check all 4 directions
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc

                    # skip if out of bounds
                    if nr < 0 or nc < 0:
                        continue
                    if nr >= ROWS or nc >= COLS:
                        continue

                    # skip if water
                    if grid[nr][nc] == "0":
                        continue

                    # skip if already visited
                    if (nr, nc) in visited:
                        continue

                    # otherwise, it's valid land we haven’t seen
                    q.append((nr, nc))

                    # mark visited immediately
                    visited.add((nr, nc))

        # scan the grid
        for r in range(ROWS):
            for c in range(COLS):

                # if it's land AND not visited yet → new island
                if grid[r][c] == "1" and (r, c) not in visited:

                    # explore entire island
                    bfs(r, c)

                    # count it
                    islands = islands + 1

        return islands