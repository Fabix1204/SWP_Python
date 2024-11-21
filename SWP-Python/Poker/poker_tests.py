import unittest

# Importiere die zu testenden Klassen und Funktionen
from poker_main import Card, create_deck, shuffle_deck, deal_cards, check_hand, simulate_poker_hands

class TestPokerSimulation(unittest.TestCase):

    def test_card_creation(self):
        # Test der Card-Klasse
        card = Card('A', 'Hearts')
        self.assertEqual(card.value, 'A')
        self.assertEqual(card.color, 'Hearts')
        self.assertEqual(str(card), 'A of Hearts')

    def test_create_deck(self):
        # Test der create_deck-Funktion
        deck = create_deck()
        self.assertEqual(len(deck), 52)  # Ein vollständiges Deck sollte 52 Karten haben
        # Prüfen, ob jede Kombination aus Wert und Farbe enthalten ist
        self.assertIn(Card('A', 'Hearts'), deck)
        self.assertIn(Card('2', 'Spades'), deck)

    def test_shuffle_deck(self):
        # Test der shuffle_deck-Funktion
        deck = create_deck()
        shuffled_deck = shuffle_deck(deck[:])  # Kopie erstellen, um Seiteneffekte zu vermeiden
        self.assertEqual(len(shuffled_deck), 52)  # Die Anzahl der Karten sollte gleich bleiben
        self.assertNotEqual(deck, shuffled_deck)  # Nach dem Mischen sollte das Deck anders sein

    def test_deal_cards(self):
        # Test der deal_cards-Funktion
        deck = create_deck()
        hand = deal_cards(deck, 5)
        self.assertEqual(len(hand), 5)  # Die Hand sollte 5 Karten haben
        self.assertEqual(len(deck), 47)  # Das Deck sollte um 5 Karten reduziert sein
        # Test mit zu kleiner Deckgröße
        with self.assertRaises(ValueError):
            deal_cards([], 1)

    def test_check_hand(self):
        # Test der check_hand-Funktion
        flush_hand = [
            Card('A', 'Hearts'),
            Card('10', 'Hearts'),
            Card('J', 'Hearts'),
            Card('Q', 'Hearts'),
            Card('K', 'Hearts'),
        ]
        self.assertEqual(check_hand(flush_hand), "Royal Flush")

        straight_flush_hand = [
            Card('9', 'Diamonds'),
            Card('10', 'Diamonds'),
            Card('J', 'Diamonds'),
            Card('Q', 'Diamonds'),
            Card('K', 'Diamonds'),
        ]
        self.assertEqual(check_hand(straight_flush_hand), "Straight Flush")

        four_of_a_kind_hand = [
            Card('A', 'Hearts'),
            Card('A', 'Diamonds'),
            Card('A', 'Clubs'),
            Card('A', 'Spades'),
            Card('K', 'Hearts'),
        ]
        self.assertEqual(check_hand(four_of_a_kind_hand), "Four of a Kind")

        high_card_hand = [
            Card('2', 'Hearts'),
            Card('5', 'Diamonds'),
            Card('7', 'Clubs'),
            Card('J', 'Spades'),
            Card('K', 'Hearts'),
        ]
        self.assertEqual(check_hand(high_card_hand), "High Card")

    def test_simulate_poker_hands(self):
        # Test der simulate_poker_hands-Funktion
        hand_statistics = simulate_poker_hands(100, 5)
        # Sicherstellen, dass die Wahrscheinlichkeiten sinnvoll sind
        total_percentage = sum(hand_statistics.values())
        self.assertAlmostEqual(total_percentage, 100, places=1)  # Gesamtprozentsatz sollte 100% sein
        self.assertIn("High Card", hand_statistics)  # 'High Card' sollte vorkommen
        self.assertIn("Pair", hand_statistics)  # 'Pair' sollte ebenfalls vorkommen

def main():
    unittest.main()

if __name__ == '__main__':
    main()
