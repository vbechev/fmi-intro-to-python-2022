import unittest

from solution import calculate_final_vector


class TestCalculateFinalVector(unittest.TestCase):
    """Test the calculate_final_vector function."""

    def test_simple_move(self):
        """Sanity test for a simple 2-step move."""
        self.assertEqual(calculate_final_vector((0, 0), ['00c000', 'c0c000']),
                         (1, 1))

if __name__ == '__main__':
    unittest.main()

