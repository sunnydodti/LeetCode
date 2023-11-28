class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        print(board[0][0], 5, board[0][0] == 5)
        print('----------row----------')
        for row in board:
            # print(self.check_duplicates(row))
            if self.check_duplicates(row):
                return False

        print('----------column----------')
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])

            # print(self.check_duplicates(column))
            if self.check_duplicates(column):
                return False

        print('----------blocks----------')
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if self.check_duplicates(board[i][j:j+3] + board[i+1]
                                         [j:j+3] + board[i+2][j:j+3]):
                    return False

        return True

    def check_duplicates(self, arr=[]):
        checked = []
        if arr:
            print(arr)
            for i in arr:
                print('\t', i, checked)
                if i == '.':
                    continue
                print(i, i in checked)

                if i in checked:
                    print(i, checked)
                    return True

                checked.append(i)

            return False


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    board = [
        [".", ".", ".", ".", "5", ".", ".", "1", "."],
        [".", "4", ".", "3", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "1"],
        ["8", ".", ".", ".", ".", ".", ".", "2", "."],
        [".", ".", "2", ".", "7", ".", ".", ".", "."],
        [".", "1", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."]
    ]

    S = Solution()
    print('ans: ', S.isValidSudoku(board))
