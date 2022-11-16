import unittest
from unittest.mock import patch

from solution import Card, Deck, Player, Game, Belot, Poker


def identify(card):
    """Represent a Card as a tuple to disregard identity."""
    return card.get_suit(), card.get_face()


class TestCard(unittest.TestCase):
    """Test the Card class."""

    def setUp(self):
        """Setup Card instances."""
        self._ace_spades = Card('spades', 'A')
        self._ten_clubs = Card('clubs', '10')

    def test_get_face(self):
        """Test the get_face method."""
        self.assertEqual(self._ace_spades.get_face(), 'A')
        self.assertEqual(self._ten_clubs.get_face(), '10')

    def test_get_suit(self):
        """Test the get_suit method."""
        self.assertEqual(self._ace_spades.get_suit(), 'spades')
        self.assertEqual(self._ten_clubs.get_suit(), 'clubs')


class TestDeck(unittest.TestCase):
    """Test the Deck class."""

    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')
    FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def test_init_regular(self):
        """Test initialized cards without filter."""
        # Construct expected cards
        expected_cards = set()
        for suit in self.SUITS:
            for face in self.FACES:
                expected_cards.add((suit, face))
        # Construct actual_cards
        actual_cards = set()
        deck = Deck()
        for card in deck.get_cards():
            actual_cards.add(identify(card))
        # Compare
        self.assertEqual(expected_cards, actual_cards)
        # Ensure that set is not hiding some duplicates
        self.assertEqual(len(deck.get_cards()), len(self.FACES) * 4)

    def test_init_filtered(self):
        """Test initialized cards with filter."""
        face_filter = ['2', '5', '10', 'J', 'A']
        # Construct expected cards
        expected_cards = set()
        for suit in self.SUITS:
            for face in face_filter:
                expected_cards.add((suit, face))
        # Construct actual_cards
        deck = Deck(face_filter)
        actual_cards = set()
        for card in deck.get_cards():
            actual_cards.add(identify(card))
        # Compare
        self.assertEqual(expected_cards, actual_cards)
        # Ensure that set is not hiding some duplicates
        self.assertEqual(len(deck.get_cards()), len(face_filter) * 4)

    def test_cutting_deck(self):
        """Test cutting a deck."""
        face_filter = ['2', '5', '10', 'J', 'A']
        deck = Deck(face_filter)
        cards_before = deck.get_cards()[:]
        deck.cut()
        cards_after = deck.get_cards()[:]
        # Ensure that there is actually a change
        self.assertNotEqual(cards_before, cards_after)
        # Pick the first card from the new order and 
        # find its place in the old order
        index = cards_before.index(cards_after[0])
        # Simulate a cut with the card before the first one
        simulated_cards = cards_before[index:] + cards_before[:index]
        # Ensure the result is the same
        self.assertEqual(simulated_cards, cards_after)

    def test_shuffling_deck(self):
        """Test shuffling a deck."""
        deck = Deck()
        cards_before = deck.get_cards()[:]
        deck.shuffle()
        cards_after = deck.get_cards()[:]
        # Ensure that there is actually a change
        self.assertNotEqual(cards_before, cards_after)
        # Ensure that the set is still the same (no cards were lost or added)
        self.assertEqual(set(cards_before), set(cards_after))


class TestPlayer(unittest.TestCase):
    pass # Nothing really to test with this class


class TestGame(unittest.TestCase):
    """Test the Game class."""

    def test_players_creation(self):
        """Test creation and retrieval of players."""
        game_of_2 = Game(2, 'ltr', (1, 2))
        game_of_5 = Game(5, 'ltr', (1, 2))
        game_of_2_players = game_of_2.get_players()[:]
        game_of_5_players = game_of_5.get_players()[:]
        self.assertEqual(len(game_of_2_players), 2)
        self.assertEqual(len(game_of_5_players), 5)
        for player in game_of_2_players + game_of_5_players:
            self.assertIsInstance(player, Player)

    @patch('solution.Deck.shuffle')
    @patch('solution.Deck.cut')
    def test_prepare_deck(self, cut_mock, shuffle_mock):
        """Test preparing the deck for dealing."""
        game = Game(2, 'ltr', (1, 2))
        game.prepare_deck()
        cut_mock.assert_called_once_with
        shuffle_mock.assert_called_once_with

    def test_dealing_ltr(self):
        """Test dealing the cards left to right."""
        game = Game(3, 'ltr', (1, 1, 1))
        players = game.get_players()[:]
        cards = list(map(identify, game.get_deck().get_cards()))
        game.deal(players[2])
        for player_index, cards_indexes in ((2, (0, 3, 6)),
                                            (0, (1, 4, 7)),
                                            (1, (2, 5, 8))):
            actual = set(map(identify, players[player_index].get_cards()))
            # Allow dealing from top or bottom, becaues different people
            # might consider index=0 - top OR index=0 - bottom
            expected_from_top = set(map(cards.__getitem__, cards_indexes))
            expected_from_bottom = set(map(cards[::-1].__getitem__, cards_indexes))
            self.assertIn(actual, (expected_from_top, expected_from_bottom))

    def test_dealing_rtl(self):
        """Test dealing the cards right to left."""
        game = Game(4, 'rtl', (2, 1))
        players = game.get_players()[:]
        cards = list(map(identify, game.get_deck().get_cards()))
        game.deal(players[1])
        for player_index, cards_indexes in ((1, (0, 1, 8)),
                                            (0, (2, 3, 9)),
                                            (3, (4, 5, 10)),
                                            (2, (6, 7, 11))):
            actual = set(map(identify, players[player_index].get_cards()))
            # Allow dealing from top or bottom, becaues different people
            # might consider index=0 - top OR index=0 - bottom
            expected_from_top = set(map(cards.__getitem__, cards_indexes))
            expected_from_bottom = set(map(cards[::-1].__getitem__, cards_indexes))
            self.assertIn(actual, (expected_from_top, expected_from_bottom))

    def test_collecting_cards_before_dealing(self):
        """Test collecting the cards before a new deal."""
        game = Game(4, 'ltr', (1, 1, 1))
        players = game.get_players()[:]
        game.prepare_deck()
        game.deal(players[0])
        game.prepare_deck()
        for player in players:
            self.assertEqual(player.get_cards(), [])
        self.assertEqual(len(game.get_deck().get_cards()), 52)


class TestBelot(unittest.TestCase):
    """Test the Belot class."""

    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')
    FACES = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def test_correct_deck_init(self):
        """Test initialization with correct deck."""
        belot = Belot()
        expected_cards = set()
        for suit in self.SUITS:
            for face in self.FACES:
                expected_cards.add((suit, face))
        actual_cards = set()
        for card in belot.get_deck().get_cards():
            actual_cards.add(identify(card))
        self.assertEqual(expected_cards, actual_cards)
        # Ensure that set is not hiding some duplicates
        self.assertEqual(len(belot.get_deck().get_cards()),
                         len(self.FACES) * 4)

    def test_correct_direction_and_players_deal(self):
        """Test dealing with correct direction and players."""
        belot = Belot()
        cards = list(map(identify, belot.get_deck().get_cards()))
        players = belot.get_players()[:]
        belot.deal(players[0])
        self.assertEqual(len(players), 4)
        for player_index, cards_indexes in ((0, (0, 1, 8, 9, 10, 20, 21, 22)),
                                            (1, (2, 3, 11, 12, 13, 23, 24, 25)),
                                            (2, (4, 5, 14, 15, 16, 26, 27, 28)),
                                            (3, (6, 7, 17, 18, 19, 29, 30, 31))):
            actual = set(map(identify, players[player_index].get_cards()))
            # Allow dealing from top or bottom, becaues different people
            # might consider index=0 - top OR index=0 - bottom
            expected_from_top = set(map(cards.__getitem__, cards_indexes))
            expected_from_bottom = set(map(cards[::-1].__getitem__, cards_indexes))
            self.assertIn(actual, (expected_from_top, expected_from_bottom))


class TestPoker(unittest.TestCase):
    """Test the Poker class."""

    SUITS = ('clubs', 'diamonds', 'hearts', 'spades')
    FACES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def test_correct_deck_init(self):
        """Test initialization with correct deck."""
        poker = Poker()
        expected_cards = set()
        for suit in self.SUITS:
            for face in self.FACES:
                expected_cards.add((suit, face))
        actual_cards = set()
        for card in poker.get_deck().get_cards():
            actual_cards.add(identify(card))
        self.assertEqual(expected_cards, actual_cards)
        # Ensure that set is not hiding some duplicates
        self.assertEqual(len(poker.get_deck().get_cards()),
                         len(self.FACES) * 4)

    def test_correct_direction_and_players_deal(self):
        """Test dealing with correct direction and players."""
        poker = Poker()
        cards = list(map(identify, poker.get_deck().get_cards()))
        players = poker.get_players()[:]
        poker.deal(players[3])
        self.assertEqual(len(players), 9)
        for player_index, cards_indexes in ((3, (0, 9, 18, 27, 36)),
                                            (2, (1, 10, 19, 28, 37)),
                                            (1, (2, 11, 20, 29, 38)),
                                            (0, (3, 12, 21, 30, 39)),
                                            (8, (4, 13, 22, 31, 40)),
                                            (7, (5, 14, 23, 32, 41)),
                                            (6, (6, 15, 24, 33, 42)),
                                            (5, (7, 16, 25, 34, 43)),
                                            (4, (8, 17, 26, 35, 44))):
            actual = set(map(identify, players[player_index].get_cards()))
            # Allow dealing from top or bottom, becaues different people
            # might consider index=0 - top OR index=0 - bottom
            expected_from_top = set(map(cards.__getitem__, cards_indexes))
            expected_from_bottom = set(map(cards[::-1].__getitem__, cards_indexes))
            self.assertIn(actual, (expected_from_top, expected_from_bottom))


if __name__ == '__main__':
    unittest.main()
