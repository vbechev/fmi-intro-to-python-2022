import unittest

from solution import calculate_final_vector


class TestCalculateFinalVector(unittest.TestCase):

    def test_negative_step(self):
        self.assertEqual(calculate_final_vector((0, 0), ['C0FFC0']), (-1, 0)) # Light Green
        self.assertEqual(calculate_final_vector((0, 0), ['FFFFC0']), (0, -1)) # Light Yellow
        self.assertEqual(calculate_final_vector((0, 0), ['FFC0C0']), (1, 0))  # Light Red
        self.assertEqual(calculate_final_vector((0, 0), ['C0C0FF']), (0, 1))  # Light Blue

    def test_positive_step(self):
        self.assertEqual(calculate_final_vector((0, 0), ['00C000']), (1, 0))  # Dark Green
        self.assertEqual(calculate_final_vector((0, 0), ['C0C000']), (0, 1))  # Dark Yellow
        self.assertEqual(calculate_final_vector((0, 0), ['C00000']), (-1, 0)) # Dark Red
        self.assertEqual(calculate_final_vector((0, 0), ['0000C0']), (0, -1)) # Dark Blue

    def test_black_stops(self):
        hexes = ['FFC0C0', 'FFC0C0', 'FFC0C0', '000000', 'FFC0C0', 'FFC0C0', 'FFC0C0']
        self.assertEqual(calculate_final_vector((0, 0), hexes), (3, 0))

    def test_white_ignored(self):
        hexes = ['FFC0C0', 'FFFFFF', 'FFC0C0', 'FFFFFF', 'FFC0C0', 'FFFFFF', 'FFC0C0']
        self.assertEqual(calculate_final_vector((0, 0), hexes), (4, 0))

    def test_empty_list(self):
        hexes = []
        self.assertEqual(calculate_final_vector((-69, -69), hexes), (-69, -69))

    def test_mixed_case(self):
        hexes = ['FFC0C0', 'c0c0ff', 'FfC0c0', 'C0C0Ff']
        self.assertEqual(calculate_final_vector((0, 0), hexes), (2, 2))

    def test_starting_vector(self):
        hexes = ['FFC0C0', 'FFC0C0', 'FFC0C0']
        starting_vector = (8998, 0)
        self.assertEqual(calculate_final_vector(starting_vector, hexes), (9001, 0))

    def test_a_metric_shit_ton_of_hexes(self):
        hexes = ['C0FFC0', '00c000', 'FfFfFf', 'C0c000', 'C0C0FF', 'ffffc0', 'C00000', 'FFFFFF',
                 'c0fFC0', 'ffC0C0'] * 100 + ['000000', 'C0FFC0', 'C0C0FF']
        starting_vector = (58, -58)
        self.assertEqual(calculate_final_vector(starting_vector, hexes), (-42, 42))

if __name__ == '__main__':
    unittest.main()
    