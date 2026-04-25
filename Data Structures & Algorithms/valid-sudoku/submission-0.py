class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # track what we've seen in each column, row, and 3x3 square
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        # loop through every cell in the board
        for r in range(9):
            for c in range(9):

                # skip empty cells
                if board[r][c] == ".":
                    continue

                val = board[r][c]

                # check if this value already exists in:
                # - same row
                # - same column
                # - same 3x3 square
                if (val in rows[r] or 
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]):
                    return False  # invalid sudoku

                # add value to corresponding row, column, and square
                rows[r].add(val)
                cols[c].add(val)

                # (r // 3, c // 3) maps cell to its 3x3 box
                # example: (0,0),(0,1),(1,2) → all go to (0,0)
                squares[(r // 3, c // 3)].add(val)

        # if no duplicates found, board is valid
        return True