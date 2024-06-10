class Backtracking:
    def __init__(self, board):
        self.board = board
        self.initial_cells = [(row, col) for row in range(9) for col in range(9) if board[row][col] != 0]

    def __str__(self):
        board_str = ''
        for row in range(9):
            row_str = []
            for col in range(9):
                if self.board[row][col] == 0:
                    row_str.append('_')
                elif (row, col) in self.initial_cells:
                    row_str.append(str(self.board[row][col]))
                else:
                    row_str.append(f'\033[92m{self.board[row][col]}\033[0m')  # Green text for new numbers
            board_str += ' '.join(row_str) + '\n'
        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False


