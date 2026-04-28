class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

                # get board dimensions once so we don’t recompute
        ROWS, COLS = len(board), len(board[0])

        # this keeps track of the current path (cells we’ve already used)
        # we can’t reuse the same cell in one word path
        path = set()

        def dfs(r, c, i):
            # base case: if we matched all characters in word
            # i is the index in the word we’re trying to match
            if i == len(word):
                return True

            # out of bounds OR mismatch OR already visited
            if (min(r, c) < 0 or                 # went off grid (top/left)
                r >= ROWS or c >= COLS or        # went off grid (bottom/right)
                word[i] != board[r][c] or        # current letter doesn’t match
                (r, c) in path):                 # already used this cell in current path
                return False

            # mark this cell as visited in current path
            path.add((r, c))

            # explore all 4 directions (down, up, right, left)
            # if ANY direction works, we found the word
            res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))

            # backtrack: remove from path so other paths can use this cell
            path.remove((r, c))

            return res


        # try starting DFS from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                # if any starting point finds the word → return True
                if dfs(r, c, 0):
                    return True

        # if no path matched the word
        return False
         