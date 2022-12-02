import unittest
from puzzle_2 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_2(self):
        puzzle2 = Solution("day_2/puzzle_2_sample_data.txt")

        self.assertEqual(puzzle2.solve_part_1(), 150)
        self.assertEqual(puzzle2.solve_part_2(), 900)


if __name__ == "__main__":
    unittest.main()
