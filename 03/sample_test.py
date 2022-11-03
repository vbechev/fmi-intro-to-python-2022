import unittest

from solution import Card, Deck, Player, Game, Belot, Poker


class TestCard(unittest.TestCase):
    """Test the Card class."""

    def test_simple_init(self):
        """Sanity test for the Card class."""
        card = Card('clubs', '2')
        self.assertTrue(hasattr(card, 'get_suit'))
        self.assertTrue(hasattr(card, 'get_face'))


class TestDeck(unittest.TestCase):
    """Test the Deck class."""

    def test_simple_init(self):
        """Sanity test for the Deck class."""
        deck = Deck()
        self.assertTrue(hasattr(deck, 'cut'))
        self.assertTrue(hasattr(deck, 'shuffle'))
        self.assertTrue(hasattr(deck, 'get_cards'))


class TestPlayer(unittest.TestCase):
    """Test the Player class."""

    def test_simple_init(self):
        """Sanity test for the Player class."""
        player = Player()
        self.assertTrue(hasattr(player, 'get_cards'))


class TestGame(unittest.TestCase):
    """Test the Game class."""

    def test_simple_init(self):
        """Sanity test for the Game class."""
        game = Game(2, 'rtl', (1, 2))
        self.assertTrue(hasattr(game, 'get_players'))
        self.assertTrue(hasattr(game, 'prepare_deck'))
        self.assertTrue(hasattr(game, 'deal'))
        self.assertTrue(hasattr(game, 'get_deck'))


class TestBelot(unittest.TestCase):
    """Test the Belot class."""

    def test_simple_init(self):
        """Sanity test for the Belot class."""
        belot = Belot()
        self.assertIsInstance(belot, Game)
        

class TestPoker(unittest.TestCase):
    """Test the Poker class."""

    def test_simple_init(self):
        """Sanity test for the Poker class."""
        poker = Poker()
        self.assertIsInstance(poker, Game)


if __name__ == '__main__':
    unittest.main()
