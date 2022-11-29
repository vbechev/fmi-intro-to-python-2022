import unittest

from solution import *


"""
Some FENs are taken from a database that can be found here:
https://docs.google.com/spreadsheets/d/1fWA-9QW-C8Dc-8LDrEemSligWcprkpKif6cNDs4V_mg/edit#gid=0
"""

class TestChessException(unittest.TestCase):
    """Test the ChessException class."""

    def test_correct_parent(self):
        """Ensure ChessException is a child of Exception."""
        """
            People might inherit from BaseException which would work...
            ...but is wrong.
        """
        exception = ChessException('Paul Morphy')
        self.assertIsInstance(exception, Exception)


class TestChessScore(unittest.TestCase):
    """Test the ChessScore class."""

    def test_correct_mapping_of_pieces(self):
        """Test correct mapping for each piece."""
        self.assertEqual(int(ChessScore(['p'])), 1)
        self.assertEqual(int(ChessScore(['b'])), 3)
        self.assertEqual(int(ChessScore(['n'])), 3)
        self.assertEqual(int(ChessScore(['k'])), 4)
        self.assertEqual(int(ChessScore(['r'])), 5)
        self.assertEqual(int(ChessScore(['q'])), 9)

    def test_correct_sum_of_pieces(self):
        """Test correct sum for random pieces."""
        # All pieces met once
        self.assertEqual(int(ChessScore(['p', 'b', 'n', 'k', 'r', 'q'])), 25)
        # No king
        self.assertEqual(int(ChessScore(['q'] * 3)), 27)
        # Many kings
        self.assertEqual(int(ChessScore(['k'] * 5)), 20)
        # Random long combination (well, not trully random - digits of Pi)
        self.assertEqual(int(ChessScore(['p']*3 + ['b']*1 + ['n']*4 + ['k']*1 +
                                        ['r']*5 + ['q']*9 + ['q']*200)), 1928)

    def test_comparison(self):
        """Test correct comparison on a pair of scores."""
        self.assertLess(ChessScore(['b']), ChessScore(['k']))
        self.assertGreater(ChessScore(['k']), ChessScore(['p']))
        self.assertEqual(ChessScore(['b']), ChessScore(['n']))
        self.assertLessEqual(ChessScore(['b']), ChessScore(['q']))
        self.assertLessEqual(ChessScore(['b']), ChessScore(['n']))
        self.assertGreaterEqual(ChessScore(['b']), ChessScore(['p']))
        self.assertGreaterEqual(ChessScore(['b']), ChessScore(['n']))
        self.assertNotEqual(ChessScore(['b']), ChessScore(['p']))

    def test_basic_arithmetic(self):
        """Test additiona and subtraction of ChessScores."""
        self.assertEqual(ChessScore(['b']) + ChessScore(['k']), 7)
        self.assertEqual(ChessScore(['q']) - ChessScore(['p']), 8)
        self.assertEqual(ChessScore(['p']) - ChessScore(['p']), 0)
        self.assertEqual(ChessScore(['n']) - ChessScore(['k']), -1)


class TestChessPosition(unittest.TestCase):
    """Test the ChessPosition class."""

    def test_against_touching_kings(self):
        """Test for kings next to each other."""
        positions = ['k7/K7/8/8/8/8/8/8', # Vertical
                     '8/8/8/3kK3/8/8/8/8', # Horizonal
                     '8/8/8/3k4/2K5/8/8/8', # Diagonal A1-H8
                     '8/8/8/K7/1k6/8/8/8'] # Diagonal A8-H1
        for position in positions:
            try:
                ChessPosition(position)
            except ChessException as e:
                self.assertEqual(str(e), 'kings')
            else:
                raise Exception(f"No exception raised on: {position}")

    def test_validation_conflict(self):
        """Test for correct Exception on multiple validation fails."""
        position = 'P7/K7/k7/8/8/8/8/8'
        try:
            ChessPosition(position)
        except ChessException as e:
            self.assertEqual(str(e), 'kings')
        else:
            raise Exception(f"No exception raised on: {position}")

    def test_king_count(self):
        """Test for missing or multiple kings."""
        positions = ['8/8/8/8/8/8/8/8',
                     'k7/8/2K5/8/8/4k3/8/8',
                     '4k3/8/1K6/8/8/pppppppK/8/8',
                     'rnbqkbnr/pppppppK/8/8/8/8/PPPPPPPP/RNBQKBNR',
                     'rnbqkbnr/pppppppp/8/8/8/8/kPPPPPPP/RNBQKBNR']
        for position in positions:
            try:
                ChessPosition(position)
            except ChessException as e:
                self.assertEqual(str(e), 'kings')
            else:
                raise Exception(f"No exception raised on: {position}")

    def test_pawns_position(self):
        """Test for incorrect pawns."""
        positions = ['p7/8/k7/8/7K/8/8/8',
                     '7p/8/k7/8/7K/8/8/8',
                     '3pp3/8/k7/8/7K/8/8/8',
                     '8/8/k7/8/7K/8/8/p7',
                     '8/8/k7/8/7K/8/8/p5pp']
        for position in positions:
            try:
                ChessPosition(position)
            except ChessException as e:
                self.assertEqual(str(e), 'pawns')
            else:
                raise Exception(f"No exception raised on: {position}")

    def test_get_black_score(self):
        """Test get_black_score."""
        scores = {
            '8/8/8/k7/7K/8/8/8': 4,
            'rrrrrrrr/rrrrrrrr/krrrrrrr/rrrrrrrr/'
            'rrrrrrrr/rrrrrrrK/rrrrrrrr/rrrrrrrr': 314,
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': 43
        }
        for fen, score in scores.items():
            self.assertEqual(int(ChessPosition(fen).get_black_score()), score)

    def test_get_white_score(self):
        """Test get_white_score."""
        scores = {
            '8/8/8/k7/7K/8/8/8': 4,
            'QQQQQQQQ/QQQQQQQQ/QQkQQQQQ/QQQQQQQQ/'
            'QQQQQQQQ/QQKQQQQQ/QQQQQQQQ/QQQQQQQQ': 562,
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': 43
        }
        for fen, score in scores.items():
            self.assertIsInstance(ChessPosition(fen).get_white_score(),
                                  ChessScore)
            self.assertEqual(int(ChessPosition(fen).get_white_score()), score)

    def test_white_is_winning(self):
        """Test white_is_winning."""
        results = {
            '8/8/8/k7/7K/8/8/8': False,
            'qqqqqqqq/qqqqqqqq/QQkQQQQQ/QQQQQQQQ/'
            'qqqqqqqq/qqKqqqqq/QQQQQQQQ/QQQQQQQQ': False,
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': False,
            '8/P7/8/k7/7K/8/8/8': True,
            '8/3p4/8/k7/7K/8/8/8': False
        }
        for fen, result in results.items():
            self.assertIsInstance(ChessPosition(fen).get_white_score(),
                                  ChessScore)
            if ChessPosition(fen).white_is_winning() is not result:
                raise Exception(f'Incorrect result for {fen}')

    def test_black_is_winning(self):
        """Test black_is_winning."""
        results = {
            '8/8/8/k7/7K/8/8/8': False,
            'qqqqqqqq/qqqqqqqq/QQkQQQQQ/QQQQQQQQ/'
            'qqqqqqqq/qqKqqqqq/QQQQQQQQ/QQQQQQQQ': False,
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': False,
            '8/P7/8/k7/7K/8/8/8': False,
            '8/3p4/8/k7/7K/8/8/8': True
        }
        for fen, result in results.items():
            if ChessPosition(fen).black_is_winning() is not result:
                raise Exception(f'Incorrect result for {fen}')

    def test_is_equal(self):
        """Test is_equal."""
        results = {
            '8/8/8/k7/7K/8/8/8': True,
            'qqqqqqqq/qqqqqqqq/QQkQQQQQ/QQQQQQQQ/'
            'qqqqqqqq/qqKqqqqq/QQQQQQQQ/QQQQQQQQ': True,
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': True,
            '8/P7/8/k7/7K/8/8/8': False,
            '8/3p4/8/k7/7K/8/8/8': False
        }
        for fen, result in results.items():
            if ChessPosition(fen).is_equal() is not result:
                raise Exception(f'Incorrect result for {fen}')

    def test_str(self):
        """Test string representation of the instance."""
        fen = '6k1/5p2/6p1/8/7p/8/6PP/6K1'
        self.assertEqual(str(ChessPosition(fen)), fen)

    def test_len(self):
        """Test number of pieces for a position."""
        counts = {
            '5k2/8/p7/4K1P1/P4R2/6r1/8/8': 7,
            'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR': 32,
            'rrrrrrrk/qbnQQbnr/pppppppp/pppppppp/'
            'pppppppp/pppppppp/QBNqqBNR/Kbnbnbnb': 64,
            '7k/8/8/8/8/8/8/3K4': 2,
        }
        for fen, count in counts.items():
            self.assertEqual(len(ChessPosition(fen)), count)

    def test_getitem(self):
        """Test getitem functionality."""
        pos = ChessPosition('3b1N2/8/3k4/5pp1/8/5K1P/8/8')
        self.assertEqual(pos['F3'], 'K')
        self.assertEqual(pos['D6'], 'k')
        self.assertEqual(pos['D8'], 'b')
        self.assertEqual(pos['F8'], 'N')
        self.assertEqual(pos['F5'], 'p')
        self.assertEqual(pos['H3'], 'P')
        self.assertEqual(pos['A1'], None)
        self.assertEqual(pos['H8'], None)


if __name__ == '__main__':
    unittest.main()