from typing import List, Union, Optional


class BingoNumber:
    def __init__(self, value: int, selected: bool = False):
        self.value = value
        self.selected = selected

    def __str__(self):
        if self.selected:
            return f"[{self.value}]"
        else:
            return f"{self.value}"

    def __repr__(self):
        return f"{self.value}-{'X' if self.selected else 'O'}"


class BingoBoard:
    def __init__(
        self, initial_board_values: List[List[int]], size: int = 5, win: bool = False
    ):
        self.board: List[List[BingoNumber]] = []
        self.size = size
        self.win = win
        for row in initial_board_values:
            new_row = []

            for column in row:
                new_number = BingoNumber(column)
                new_row.append(new_number)

            self.board.append(new_row)

    def __str__(self):
        board_as_str = ""
        for row in self.board:
            for col in row:
                board_as_str += f"{col} "
            board_as_str += "\n"

        return board_as_str

    def select_value(self, selected_value: int) -> bool:
        # scan the board for the number and select it if found
        selected_value_found = False
        for row in self.board:
            for bingo_number in row:
                if bingo_number.value == selected_value:
                    bingo_number.selected = True
                    selected_value_found = True

        return selected_value_found

    def check_board_for_win(self) -> bool:

        row_wins = [True] * self.size
        col_wins = [True] * self.size
        for row_index in range(0, self.size):

            for col_index in range(0, self.size):

                if not self.board[row_index][col_index].selected:
                    col_wins[col_index] = False
                    row_wins[row_index] = False

        print("Checking for win")
        print("Rows:", row_wins)
        print("Cols:", col_wins)
        self.win = any(row_wins) or any(col_wins)
        return self.win

    def get_unselected_values(self) -> List[int]:
        unselected: List[int] = []
        for row in self.board:
            for bn in row:
                if not bn.selected:
                    unselected.append(bn.value)

        return unselected


bingo_number_test = BingoNumber(4)

print(bingo_number_test)
print(type(bingo_number_test))
print(bingo_number_test.value)
print(type(bingo_number_test.value))
val = bingo_number_test.value
print(type(val))
print(val == 4)
with open("./input.txt") as reader:

    selected_numbers = reader.readline()

    bingo_boards: List[BingoBoard] = []

    line = reader.readline()
    count = 0
    board: List[List[int]] = []
    stop = False
    while line and not stop:
        if len(line) > 1:
            count += 1
            values = line.split(" ")
            print(values)
            cleaned_values = [int(x.strip()) for x in values if x.strip() != ""]
            print(cleaned_values)

            row: List[int] = []

            for val in cleaned_values:
                row.append(val)

            board.append(row)

            if count == 5:
                count = 0
                new_board = BingoBoard(board)
                print("apppending board")
                bingo_boards.append(new_board)
                board = []

        line = reader.readline()

    numbers_list = selected_numbers.split(",")

    print(numbers_list)
    # print(bingo_boards[0])
    found_winner = False
    winning_board: Union[BingoBoard, None] = None
    winning_number: Union[int, None] = None
    print(len(bingo_boards))
    win_count = 0
    for num in numbers_list:
        print("current number", num)
        print(len(bingo_boards))

        for bb in bingo_boards:
            if not bb.win:
                print(bb)
                bb.select_value(int(num.strip()))

                if bb.check_board_for_win():
                    found_winner = True
                    winning_board = bb
                    win_count += 1
                    winning_number = int(num.strip())

        if found_winner:
            print("WINNER!")
            if win_count == len(bingo_boards):
                break

    if winning_board is not None:
        print(winning_board)
        print(winning_board.get_unselected_values())
        score = sum(winning_board.get_unselected_values())
        print(score)
        print(winning_number)
        total_score = score * winning_number
        print(total_score)
