import random
from collections import Counter

# Klasse, die eine einzelne Karte mit einem Wert und einer Farbe darstellt
class Card():
    def __init__(self, value, color):
        # Initialisiert eine Karte mit einem Wert (z.B. 'A', 'K', '10') und einer Farbe (z.B. 'Hearts')
        self.value = value
        self.color = color

    # Gibt die Karte als lesbaren String aus (z.B. 'A of Hearts')
    def __str__(self):
        return f'{self.value} of {self.color}'

    # Für die konsistente Darstellung der Karte, z.B. in Listen
    def __repr__(self):
        return self.__str__()
    
    # Vergleichsmethode, um zwei Karten auf Gleichheit zu prüfen (gleicher Wert und gleiche Farbe)
    def __eq__(self, other):
        return self.value == other.value and self.color == other.color

# Funktion, die ein Kartendeck mit 52 Karten erstellt
def create_deck():
    # Liste der Werte (2-10, J, Q, K, A)
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    # Liste der Farben (Hearts, Diamonds, Clubs, Spades)
    colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    # Erstellt das Kartendeck durch Kombination von Werten und Farben
    deck = [Card(value, color) for value in values for color in colors]
    return deck

# Funktion, die das Deck mischt
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Funktion, die eine bestimmte Anzahl an Karten aus dem Deck zieht
def deal_cards(deck, size):
    # pop entfernt das letzte Element aus der Liste des Decks und gibt es zurück
    return [deck.pop() for _ in range(size)]

# Funktion zur Überprüfung der Kartenhand, um die beste Pokerhand zu ermitteln
def check_hand(hand):
    # Extrahiert die Werte und Farben der Karten in der Hand
    values = [card.value for card in hand]
    colors = [card.color for card in hand]
    
    # Kartewerte in Zahlen umwandeln, um auf eine Reihenfolge (Straight) zu prüfen
    value_map = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                 '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    num_values = sorted([value_map[v] for v in values])

    # Zählt, wie oft jede Karte in der Hand vorkommt
    value_counts = Counter(values)
    # Gibt die häufigsten Karten und ihre Häufigkeit zurück
    # Bsp: most_common_values = [('A', 2), ('K', 2), ('10', 1)]
    most_common_values = value_counts.most_common()

    # Überprüft, ob alle Karten die gleiche Farbe haben (Flush)
    is_flush = len(set(colors)) == 1

    # Überprüft, ob die Kartenwerte aufeinanderfolgend sind (Straight)
    is_straight = all(num_values[i] - num_values[i - 1] == 1 for i in range(1, 5))

    # Überprüft, ob die Hand ein Royal Flush ist (Spezialfall von Straight Flush)
    is_royal_flush = is_flush and is_straight and num_values == [10, 11, 12, 13, 14]

    # Bestimme die Pokerhand basierend auf den Kartenmustern
    if is_royal_flush:
        return "Royal Flush"
    if is_flush and is_straight:
        return "Straight Flush"
    if most_common_values[0][1] == 4:
        return "Four of a Kind"
    if most_common_values[0][1] == 3 and most_common_values[1][1] == 2:
        return "Full House"
    if is_flush:
        return "Flush"
    if is_straight:
        return "Straight"
    if most_common_values[0][1] == 3:
        return "Three of a Kind"
    if most_common_values[0][1] == 2 and most_common_values[1][1] == 2:
        return "Two Pair"
    if most_common_values[0][1] == 2:
        return "Pair"
    
    return "High Card"

# Simulationsfunktion, um Pokerhände n-mal zu simulieren und ihre Häufigkeit zu zählen
def simulate_poker_hands(n, hand_size):
    # Zähle die Anzahl jeder Pokerhand, die während der Simulation vorkommt
    hand_statistics = Counter()

    # Führe die Simulation n-mal aus
    for _ in range(n):
        # Erstelle und mische ein neues Deck für jede Simulation
        deck = shuffle_deck(create_deck())
        # Ziehe eine Hand mit der angegebenen Größe (z.B. 5 Karten)
        hand = deal_cards(deck, hand_size)
        # Überprüfe die Hand, um die Pokerhand zu ermitteln
        hand_type = check_hand(hand)
        # Zähle die erkannte Pokerhand
        hand_statistics[hand_type] += 1
    
    # Berechne den prozentualen Anteil jeder Hand am Gesamtergebnis
    for hand_type in hand_statistics:
        hand_statistics[hand_type] = (hand_statistics[hand_type] / n) * 100

    return hand_statistics

def main():
    # Anzahl der Simulationsdurchläufe
    n = 1_000_000
    # Simuliere Pokerhände mit 5 Karten
    hand_statistics = simulate_poker_hands(n, 5)
    # Gib die Wahrscheinlichkeiten jeder Pokerhand aus
    for hand_type, percentage in hand_statistics.items():
        print(f'{hand_type}: {percentage:.5f}%')

if __name__ == '__main__':
    main()
