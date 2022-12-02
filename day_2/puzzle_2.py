class Solution:
    def __init__(self, file: str, horizon: int = 0, depth: int = 0):
        self.horizon = horizon
        self.depth = depth
        self.file = file

        with open(self.file) as file:
            for line in file:
                if "forward" in line:
                    self.horizon += int(line.strip()[-1])
                elif "down" in line:
                    self.depth += int(line.strip()[-1])
                elif "up" in line:
                    self.depth -= int(line.strip()[-1])
                else:
                    continue

    def solve_part_1(self):
        return self.horizon * self.depth

    def solve_part_2(self):
        pass


# answer = Solution("day_2/puzzle_2_data.txt")
# print("Puzzle 2 Part 1 Solution: ", answer.solve_part_1())
# print("Puzzle 2 Part 2 Solution: ", answer.solve_part_2())
