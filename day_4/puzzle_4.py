class Solution:
    def __init__(self, file: str) -> int:
        self.file = file
        self.boards = []

        with open(self.file, "r") as file:
            file = list(file)
            for i in range(len(file)):
                if file[i].strip() == "":
                    continue
                elif i == 0:
                    self.nums = list(map(int, file[i].strip().split(",")))
                    continue
                self.boards.append(list(map(int, file[i].strip().split())))

        self.filter = [[False] * len(self.boards[0])] * len(self.boards)

    def solve_part_1(self):
        for i in range(len(self.nums)):
            for row in range(len(self.boards)):
                for col in range(len(self.boards[row])):
                    if (
                        self.filter[row][col] == False
                        and self.boards[row][col] == self.nums[i]
                    ):
                        self.filter[row][col] = True

                if sum(self.filter[row]) == 5:
                    return sum(self.boards[row]) * self.nums[i]

    def solve_part_2(self):
        pass


# answer = Solution("day_4/puzzle_4_data.txt")
# print("Solution to Puzzle 4 Part 1", answer.solve_part_1())
# print("Solution to Puzzle 4 Part 2", answer.solve_part_2())
