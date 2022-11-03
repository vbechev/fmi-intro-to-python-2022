import unittest

from solution import *


class TestNumsToText(unittest.TestCase):
    """Test the nums_to_text function."""

    def test_empty_input(self):
        """Test with empty input."""
        self.assertEqual(nums_to_text([]), '')

    def test_simple_word(self):
        """Test with a simple word that doesn't require -1."""
        self.assertEqual(nums_to_text([2, 3, 4]).lower(), 'adg')

    def test_complex_word(self):
        """Test with a complex word that requires -1."""
        self.assertEqual(nums_to_text([2, 2, -1, 2]).lower(), 'ba')

    def test_overflow_input(self):
        """Test with oveflowing number of presses."""
        self.assertEqual(nums_to_text([9, 9, 9, 9, 9, 9]).lower(), 'x')

    def test_multiple_timeouts(self):
        """Test with multiple '-1's next to each other."""
        input = [5, -1, -1, -1, 6, -1, 7, -1, -1, 8]
        self.assertEqual(nums_to_text(input).lower(), 'jmpt')

    def test_starting_with_timeout(self):
        """Test with a sequence starting with a -1."""
        self.assertEqual(nums_to_text([-1, -1, 6, 6, 6]).lower(), 'o')

    def test_ending_with_timeout(self):
        """Test with a sequence ending with a -1."""
        self.assertEqual(nums_to_text([6, 6, 6, -1]).lower(), 'o')

    def test_all_chars(self):
        """Test for correct mapping of all chars."""
        input = [1,
                 2, -1, 2, 2, -1, 2, 2, 2,
                 3, -1, 3, 3, -1, 3, 3, 3,
                 4, -1, 4, 4, -1, 4, 4, 4,
                 5, -1, 5, 5, -1, 5, 5, 5,
                 6, -1, 6, 6, -1, 6, 6, 6,
                 7, -1, 7, 7, -1, 7, 7, 7, -1, 7, 7, 7, 7,
                 8, -1, 8, 8, -1, 8, 8, 8,
                 9, -1, 9, 9, -1, 9, 9, 9, -1, 9, 9, 9, 9,
                 0]
        self.assertEqual(nums_to_text(input).lower(),
                         'abcdefghijklmnopqrstuvwxyz ')

    def test_spaces_only(self):
        """Test for input of only whitespaces with or without -1."""
        self.assertIn(nums_to_text([0, 0, 0, 0, -1, 0, -1, 0]),
                                   (' ' * 3, ' ' * 6))

    def test_random_mixed_case(self):
        """Test for a random mixed case."""
        input = [1, 3, 3, 3, 6, 4, 4, 4, 0, 7, 7, 7, 8, 8, 5, 5, 5, 5, 5, 5,
                 9, 9, 9, 9, -1, 9, 9, 9, 9, -1, 9, 9, 9, 9,
                 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        self.assertEqual(nums_to_text(input).lower(),
                         'fmi rulzzz')


class TestTextToNums(unittest.TestCase):
    """Test the text_to_nums function."""

    def test_empty_input(self):
        """Test with empty input."""
        self.assertEqual(text_to_nums(''), [])

    def test_simple_word(self):
        """Test with a simple word that doesn't require -1."""
        self.assertEqual(text_to_nums('wtm'), [9, 8, 6])

    def test_complex_word(self):
        """Test with a complex word that requires -1."""
        self.assertEqual(text_to_nums('gmm'), [4, 6, -1, 6])

    def test_all_chars(self):
        """Test for correct mapping of all chars."""
        output = [2, -1, 2, 2, -1, 2, 2, 2,
                  3, -1, 3, 3, -1, 3, 3, 3,
                  4, -1, 4, 4, -1, 4, 4, 4,
                  5, -1, 5, 5, -1, 5, 5, 5,
                  6, -1, 6, 6, -1, 6, 6, 6,
                  7, -1, 7, 7, -1, 7, 7, 7, -1, 7, 7, 7, 7,
                  8, -1, 8, 8, -1, 8, 8, 8,
                  9, -1, 9, 9, -1, 9, 9, 9, -1, 9, 9, 9, 9,
                  0]
        self.assertEqual(text_to_nums('abcdefghijklmnopqrstuvwxyz '), output)

    def test_mixed_casing(self):
        """Test for both lower and capital case."""
        self.assertEqual(text_to_nums('aBDd'), [2, -1, 2, 2, 3, -1, 3])

    def test_spaces_only(self):
        """Test for input of only whitespaces."""
        self.assertIn(text_to_nums(' ' * 4),
                      ([0, -1, 0, -1, 0, -1, 0], [0, 0, 0, 0]))

    def test_random_mixed_case(self):
        """Test for a random mixed case."""
        output1 = [8, 8, 8, 2, 7, 7, 7, 7, 5, 5, 6, 6, 6, 0, -1, 0, -1, 0,
                  5, 2, -1, 2, 2, -1, 2, 8, 2]
        output2 = [8, 8, 8, 2, 7, 7, 7, 7, 5, 5, 6, 6, 6, 0, 0, 0,
                  5, 2, -1, 2, 2, -1, 2, 8, 2]
        self.assertIn(text_to_nums('Vasko   JaBaTa'), (output1, output2))


class TestNumsToAngles(unittest.TestCase):
    """Test the nums_to_angle function."""

    def test_empty_input(self):
        """Test with empty input."""
        self.assertEqual(nums_to_angle([]), 0)

    def test_single_number(self):
        """Test with single number."""
        self.assertEqual(nums_to_angle([5]), 150)

    def test_for_sum(self):
        """Test with multiple numbers that should result in a sum."""
        self.assertEqual(nums_to_angle([1, 2]), 90)

    def test_normalizing_for_top_boundary(self):
        """Test normalizing when the sum is full circle."""
        self.assertEqual(nums_to_angle([6, 6]), 0)

    def test_for_overflowing_numbers(self):
        """Test normalizing when sum overflows."""
        self.assertEqual(nums_to_angle([9, 9]), 180)

    def test_correct_mapping(self):
        """Test correct mapping for all numbers."""
        self.assertEqual(nums_to_angle([1]), 30)
        self.assertEqual(nums_to_angle([2]), 60)
        self.assertEqual(nums_to_angle([3]), 90)
        self.assertEqual(nums_to_angle([4]), 120)
        self.assertEqual(nums_to_angle([5]), 150)
        self.assertEqual(nums_to_angle([6]), 180)
        self.assertEqual(nums_to_angle([7]), 210)
        self.assertEqual(nums_to_angle([8]), 240)
        self.assertEqual(nums_to_angle([9]), 270)
        self.assertEqual(nums_to_angle([0]), 300)

    def test_random_mixed_case(self):
        """Test with a random mixed input."""
        # ОК, не е рандом - това е телефонът на МАГ РАЯ ЕЗО ТВ :)
        self.assertEqual(nums_to_angle([0, 9, 0, 0, 6, 3, 9, 0, 0]), 150)


class TestAnglesToNums(unittest.TestCase):
    """Test the angles_to_nums function."""

    def test_empty_input(self):
        """Test with empty input."""
        self.assertEqual(angles_to_nums([]), [])

    def test_exact_angle(self):
        """Test with an exact angle."""
        self.assertEqual(angles_to_nums([60]), [2])

    def test_round_angle_easy_case(self):
        """Test with an angle requiring rounding - easy case."""
        self.assertEqual(angles_to_nums([85]), [3])

    def test_round_angle_direction(self):
        """Test with an angle requiring explicit rounding to floor."""
        """
            round() rounds halfs to an even number:
                round(0.5) -> 0
                round(1.5) -> 2
            So many algorithms that might be implemented for this will
            act differently depending on the angle, thus two adjacent
            30-degree steps are required to verify that it really works.
        """
        self.assertEqual(angles_to_nums([45]), [1])
        self.assertEqual(angles_to_nums([75]), [2])

    def test_ignoring_under_30(self):
        """Test that angles rounded under 30 are ignored."""
        self.assertEqual(angles_to_nums([14]), [])

    def test_ignoring_over_330(self):
        """Test that angles rounded over 330 are ignored."""
        self.assertEqual(angles_to_nums([320]), [])

    def test_multiple_angles(self):
        """Test with a couple of angles as input."""
        self.assertEqual(angles_to_nums([20, 180, 56, 60, 61]),
                         [1, 6, 2, 2, 2])

    def test_negative_angles(self):
        """Test with a negative input."""
        self.assertEqual(angles_to_nums([-150]), [7])

    def test_overflowing_angles(self):
        """Test with an overflowed input."""
        self.assertEqual(angles_to_nums([2940]), [2])

    def test_random_mixed_case(self):
        """Test with a random mixed input."""
        # 2925 - височината на в. Мусала (м)
        # 11034 - дълбочината на Марианската падина (м)
        # 299792458 - скоросста на светлината (м/с)
        # 384400 - разстоянието до луната (км)
        input = [-210, 0, 5, 15, 30, 60, 135, 270, 330, 340, 720, 2925, 11034,
                 299792458, 384400]
        self.assertEqual(angles_to_nums(input), [5, 1, 2, 4, 9, 1, 8, 0, 9])


class TestIsPhonetastic(unittest.TestCase):
    """Test the is_phone_tastic function."""

    def test_empty_input(self):
        """Test with empty input."""
        self.assertFalse(is_phone_tastic(''))

    def test_random_trues(self):
        """Test with a random input resulting in True."""
        self.assertTrue(is_phone_tastic('Viktor'))
        self.assertTrue(is_phone_tastic('Georgi'))

    def test_random_falses(self):
        """Test with a random input resulting in False."""
        self.assertFalse(is_phone_tastic('yomaama'))
        self.assertFalse(is_phone_tastic('JAVA'))


if __name__ == '__main__':
    unittest.main()
