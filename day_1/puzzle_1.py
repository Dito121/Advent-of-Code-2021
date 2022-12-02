class Solution:

    def __init__(self, file: str):
        self.file = file
        self.count = 0
        self.curr = 0
        self.prev = 0
        with open(self.file) as file:
            self.lines = file.readlines()

    def solve_part_1(self) -> int:
        self.count = 0

        for i in range(1, len(self.lines)):
            if int(self.lines[i]) > int(self.lines[i-1]):
                self.count += 1
                continue
        
        return self.count

    def solve_part_2(self) -> int:
        self.prev = int(self.lines[0]) + int(self.lines[1]) + int(self.lines[2])
        self.count = 1

        for i in range(1, len(self.lines) - 3):
            self.curr = int(self.lines[i]) + int(self.lines[i+1]) + int(self.lines[i+2])
            if self.curr > self.prev:
                self.count += 1
            self.prev = self.curr

        return self.count


# answer = Solution("day_1/puzzle_1_data.txt")
# print("Solution to Puzzle 1 part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 1 part 2: ", answer.solve_part_2())
