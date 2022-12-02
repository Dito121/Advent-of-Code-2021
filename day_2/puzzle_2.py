class Solution:
    def __init__(self, file: str, horizon: int = 0, depth: int = 0, aim: int = 0):
        self.horizon = horizon
        self.depth = depth
        self.aim = aim
        self.file = file

        with open(self.file) as file:
            self.lines = file.readlines()

    def solve_part_1(self):
        self.horizon = 0
        self.depth = 0
        self.aim = 0

        for line in self.lines:
            if "forward" in line:
                self.horizon += int(line.strip()[-1])
            elif "down" in line:
                self.depth += int(line.strip()[-1])
            elif "up" in line:
                self.depth -= int(line.strip()[-1])
            else:
                continue

        return self.horizon * self.depth

    def solve_part_2(self):
        self.horizon = 0
        self.depth = 0
        self.aim = 0

        for line in self.lines:
            if "up" in line:
                self.aim -= int(line.strip()[-1])
            elif "down" in line:
                self.aim += int(line.strip()[-1])
            elif "forward" in line:
                self.horizon += int(line.strip()[-1])
                self.depth += int(line.strip()[-1]) * self.aim
            else:
                continue

        return self.horizon * self.depth


# answer = Solution("day_2/puzzle_2_data.txt")
# print("Puzzle 2 Part 1 Solution: ", answer.solve_part_1())
# print("Puzzle 2 Part 2 Solution: ", answer.solve_part_2())
