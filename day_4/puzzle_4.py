class Solution:
    def __init__(self, file: str) -> int:
        self.file = file
        self.scores = []
        self.boards = []

        with open(self.file, "r") as file:
            for line in file:
                if len(line.strip()) == 0:
                    continue
                self.boards.append(line.strip().split())
        self.nums = self.boards[0]
        del self.boards[0]

    def check_boards(self):
        for i in range(1, len(self.boards), 5):
            board = self.boards[i : i + 5]
            row_count = col_count = [0] * 5

            for j in range(len(board)):
                for k in range(len(board[j])):
                    pass

    def solve_part_1(self):
        pass


# answer = Solution("day_4/puzzle_4_data.txt")
# print("Solution to Puzzle 4 Part 1", answer.solve_part_1())
# print("Solution to Puzzle 4 Part 2", answer.solve_part_2())
