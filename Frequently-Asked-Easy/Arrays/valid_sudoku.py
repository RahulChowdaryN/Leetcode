
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for li in board:
            if self.check_dup(li):
                return False
        for ind in range(9):
            col_li = [li[ind] for li in board]
            if self.check_dup(col_li):
                return False
        for li_strat_ind in [0,3,6]:
            for cell_start_ind, cell_end_ind in zip([0, 3, 6], [3, 6, 9]):
                row_1 = board[li_strat_ind][cell_start_ind:cell_end_ind]
                row_2 = board[li_strat_ind + 1][cell_start_ind:cell_end_ind]
                row_3 = board[li_strat_ind + 2][cell_start_ind:cell_end_ind]
                if self.check_dup(row_1 + row_2 + row_3):
                    return False
        return True

    def check_dup(self,li):
        li = [x for x in li if x !="."]
        return len(set(li)) != len(li)