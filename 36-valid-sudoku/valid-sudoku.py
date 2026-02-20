class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # so for this one, the goal is I need to do both the Cols as well as  the rows,  but not only that, the 3x3 boards are also in play
        rowsSet=collections.defaultdict(set)
        colsSet=collections.defaultdict(set)
        sqSet=collections.defaultdict(set)



        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rowsSet[r] or board[r][c] in colsSet[c] or board[r][c] in sqSet[(r//3,c//3)]):
                    return False
                rowsSet[r].add(board[r][c])
                colsSet[c].add(board[r][c])
                sqSet[(r//3,c//3)].add(board[r][c])
        return True

        