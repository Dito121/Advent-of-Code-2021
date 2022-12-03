import unittest
from puzzle_4 import Solution


class test_problems(unittest.TestCase):
    def test_puzzle_4(self):
        puzzle4 = Solution("day_4/puzzle_4_sample_data.txt")

        self.assertEqual(puzzle4.solve_part_1(), 4512)
        # self.assertEqual(puzzle4.solve_part_2(), )


if __name__ == "__main__":
    unittest.main()
