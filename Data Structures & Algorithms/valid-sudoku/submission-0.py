class Solution:
    """
    Final solution improved with hints and documentation online.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [ set() for i in range(9) ]
        cols = [ set() for i in range(9) ]
        cells = [ set() for i in range(9) ]

        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element == ".":
                    continue

                cell = (i // 3) * 3 + (j // 3)
                if element in rows[i] or element in cols[j] or element in cells[cell]:
                    return False

                rows[i].add(element)
                cols[j].add(element)
                cells[cell].add(element)

        return True


        