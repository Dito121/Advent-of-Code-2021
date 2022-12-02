class Solution:
    def __init__(self, file: str, n: int = 5):
        self.file = file
        self.epsilon = ""
        self.gamma = ""
        self.n = n
        self.count = [0] * self.n

        with open(self.file, "r") as file:
            self.lines = file.readlines()

    def solve_part_1(self):
        for line in self.lines:
            binary = line.strip()
            for i in range(len(binary)):
                if binary[i] == "1":
                    self.count[i] += 1
                else:
                    self.count[i] -= 1

        for i in range(len(self.count)):
            if self.count[i] >= 0:
                self.gamma += "1"
                self.epsilon += "0"
            else:
                self.gamma += "0"
                self.epsilon += "1"

        self.gamma = int(self.gamma, 2)
        self.epsilon = int(self.epsilon, 2)

        return self.gamma * self.epsilon

    def solve_part_2(self):
        


# answer = Solution("day_3/puzzle_3_data.txt", n=12)
# print("Solution to Puzzle 3 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 3 Part 2: ", answer.solve_part_2())
