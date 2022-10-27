import unittest

from solution import (nums_to_text, text_to_nums, nums_to_angle,
                      angles_to_nums, is_phone_tastic)


class TestNumsToText(unittest.TestCase):
    """Test the nums_to_text function."""

    def test_simple_conversion(self):
        """Sanity test for a single number."""
        self.assertEqual(nums_to_text([2]).lower(), 'a')


class TestTextToNums(unittest.TestCase):
    """Test the text_to_nums function."""

    def test_simple_conversion(self):
        """Sanity test for a single letter."""
        self.assertEqual(text_to_nums('a'), [2])


class TestNumsToAngles(unittest.TestCase):
    """Test the nums_to_angle function."""

    def test_simple_conversion(self):
        """Sanity test for a single number."""
        self.assertEqual(nums_to_angle([1]), 30)


class TestAnglesToNums(unittest.TestCase):
    """Test the angles_to_nums function."""

    def test_simple_conversion(self):
        """Sanity test for a single angle."""
        self.assertEqual(angles_to_nums([30]), [1])


class TestIsPhonetastic(unittest.TestCase):
    """Test the is_phone_tastic function."""

    def test_simple_word(self):
        """Sanity test for a single letter word."""
        self.assertTrue(is_phone_tastic('a'))


if __name__ == '__main__':
    unittest.main()
