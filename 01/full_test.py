import unittest

from solution import calculate_final_vector


class TestCalculateFinalVector(unittest.TestCase):
    """Test the calculate_final_vector function.
    
    The function should be invoked with a starting vector and a list of color hex codes.
    Every color in the list describes a single step (+-1 on x/y).
    The function should calculate the final position (vector), based on the starting
    vector and the directional instructions from the color hex codes.
    """

    def test_negative_step(self):
        """Light colors should result in a step of -1 in the respective direction."""
        self.assertEqual(calculate_final_vector((0, 0), ['C0FFC0']), (-1, 0)) # Light Green
        self.assertEqual(calculate_final_vector((0, 0), ['FFFFC0']), (0, -1)) # Light Yellow
        self.assertEqual(calculate_final_vector((0, 0), ['FFC0C0']), (1, 0))  # Light Red
        self.assertEqual(calculate_final_vector((0, 0), ['C0C0FF']), (0, 1))  # Light Blue

    def test_positive_step(self):
        """Dark colors should result in a step of 1 in the respective direction."""
        self.assertEqual(calculate_final_vector((0, 0), ['00C000']), (1, 0))  # Dark Green
        self.assertEqual(calculate_final_vector((0, 0), ['C0C000']), (0, 1))  # Dark Yellow
        self.assertEqual(calculate_final_vector((0, 0), ['C00000']), (-1, 0)) # Dark Red
        self.assertEqual(calculate_final_vector((0, 0), ['0000C0']), (0, -1)) # Dark Blue

    def test_black_stops(self):
        """Black (#000000) should stop the execution of the function."""
        hexes = ['FFC0C0', 'FFC0C0', 'FFC0C0', '000000', 'FFC0C0', 'FFC0C0', 'FFC0C0']
        self.assertEqual(calculate_final_vector((0, 0), hexes), (3, 0))

    def test_white_ignored(self):
        """White (#FFFFFF) should be ignored."""
        hexes = ['FFC0C0', 'FFFFFF', 'FFC0C0', 'FFFFFF', 'FFC0C0', 'FFFFFF', 'FFC0C0']
        self.assertEqual(calculate_final_vector((0, 0), hexes), (4, 0))

    def test_empty_list(self):
        """Empty input should have no effect on the initial vector."""
        hexes = []
        self.assertEqual(calculate_final_vector((-69, -69), hexes), (-69, -69))

    def test_mixed_case(self):
        """It should be possible to have both lower and upper-case letters in the hex codes."""
        hexes = ['FFC0C0', 'c0c0ff', 'FfC0c0', 'C0C0Ff']
        self.assertEqual(calculate_final_vector((0, 0), hexes), (2, 2))

    def test_starting_vector(self):
        """The final vector should take into account the starting vector argument."""
        hexes = ['FFC0C0', 'FFC0C0', 'FFC0C0']
        starting_vector = (8998, 0)
        self.assertEqual(calculate_final_vector(starting_vector, hexes), (9001, 0))

    def test_a_metric_shit_ton_of_hexes(self):
        """A metric shit ton of hexes should work the same way as a metric shit gram of hexes."""
        hexes = ['C0FFC0', '00c000', 'FfFfFf', 'C0c000', 'C0C0FF', 'ffffc0', 'C00000', 'FFFFFF',
                 'c0fFC0', 'ffC0C0'] * 100 + ['000000', 'C0FFC0', 'C0C0FF']
        starting_vector = (58, -58)
        self.assertEqual(calculate_final_vector(starting_vector, hexes), (-42, 42))


if __name__ == '__main__':
    unittest.main()
