class Solution:
    def __init__(self, file: str, n: int = 5):
        self.file = file
        self.epsilon = ""
        self.gamma = ""
        self.n = n
        self.count = [0] * self.n

        with open(self.file, "r") as file:
            self.lines = file.readlines()
        self.filtered_o2 = self.lines
        self.filtered_co2 = self.lines
        self.find_most_common()

    def find_most_common(self) -> None:
        self.epsilon = ""
        self.gamma = ""
        self.count = [0] * self.n

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

    def solve_part_1(self) -> int:
        return int(self.gamma, 2) * int(self.epsilon, 2)

    def solve_part_2(self) -> int:
        p_i = 0
        while len(self.filtered_o2) > 1:
            if self.gamma[p_i] == "1":
                self.filtered_o2 = list(
                    filter(lambda line: line[p_i] == "1", self.filtered_o2)
                )
            else:
                self.filtered_o2 = list(
                    filter(lambda line: line[p_i] == "0", self.filtered_o2)
                )
            p_i += 1
            print(self.filtered_o2)

        p_i = 0
        while len(self.filtered_co2) > 1:
            if self.gamma[p_i] == "1":
                self.filtered_co2 = list(
                    filter(lambda line: line[p_i] == "0", self.filtered_co2)
                )
            else:
                self.filtered_co2 = list(
                    filter(lambda line: line[p_i] == "1", self.filtered_co2)
                )
            p_i += 1
            print(self.filtered_co2)

        return int(self.filtered_o2[0], 2) * int(self.filtered_co2[0], 2)


# answer = Solution("day_3/puzzle_3_data.txt", n=12)
# print("Solution to Puzzle 3 Part 1: ", answer.solve_part_1())
# print("Solution to Puzzle 3 Part 2: ", answer.solve_part_2())
