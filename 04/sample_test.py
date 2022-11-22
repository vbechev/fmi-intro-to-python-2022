import unittest

from solution import *


class TestChessException(unittest.TestCase):
    """Test the ChessException class."""

    def test_existence(self):
        """Sanity test for the ChessException class."""
        exception = ChessException('Paul Morphy')


class TestChessScore(unittest.TestCase):
    """Test the ChessScore class."""

    def test_simple_init(self):
        """Sanity test for the ChessScore class."""
        score = ChessScore(['p'])


class TestChessPosition(unittest.TestCase):
    """Test the ChessPosition class."""

    def test_simple_init(self):
        """Sanity test for the ChessPosition class."""
        init_pos = ChessPosition('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR')
        self.assertTrue(hasattr(init_pos, 'get_white_score'))
        self.assertTrue(hasattr(init_pos, 'get_black_score'))
        self.assertTrue(hasattr(init_pos, 'white_is_winning'))
        self.assertTrue(hasattr(init_pos, 'black_is_winning'))
        self.assertTrue(hasattr(init_pos, 'is_equal'))


if __name__ == '__main__':
    unittest.main()
