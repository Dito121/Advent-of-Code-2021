import unittest
from puzzle_1 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_1(self):
        puzzle1 = Solution("day_1/puzzle_1_sample_data.txt")

        self.assertEqual(puzzle1.solve_part_1(), 7)
        self.assertEqual(puzzle1.solve_part_2(), 5)


if __name__ == "__main__":
    unittest.main()
