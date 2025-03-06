import random
from collections import Counter
import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Die Funktion '{func.__name__}' dauerte {execution_time:.6f} Sekunden.")
        return result
    return wrapper_timer

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        print(f"Aufruf: {func.__name__} mit args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} gab {result} zurück")
        return result
    return wrapper_debug

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

def user_input():
    try:
        n = int(input("Enter the number of simulations to run: "))
        hand_size = int(input("Enter the size of the poker hand to simulate: "))
        return n, hand_size
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return user_input()

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
    try:
        random.shuffle(deck)
        return deck
    except Exception as e:
        print(f"Error while shuffling deck: {e}")
        return deck  # Falls ein Fehler auftritt, geben wir das Deck unverändert zurück

# Funktion, die eine bestimmte Anzahl an Karten aus dem Deck zieht
def deal_cards(deck, size):
    # Überprüfen, ob genügend Karten im Deck sind
    if len(deck) < size:
        raise ValueError("Not enough cards left in the deck to deal.")
    # Entferne und gib die Karten zurück
    return [deck.pop() for _ in range(size)]


# Funktion zur Überprüfung der Kartenhand, um die beste Pokerhand zu ermitteln
def check_hand(hand):
    try:
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
    except Exception as e:
        print(f"Error in checking hand: {e}")
        return "Error"

# Simulationsfunktion, um Pokerhände n-mal zu simulieren und ihre Häufigkeit zu zählen
def simulate_poker_hands(n, hand_size):
    hand_statistics = Counter()

    # Führe die Simulation n-mal aus
    for _ in range(n):
        try:
            # Erstelle und mische ein neues Deck für jede Simulation
            deck = shuffle_deck(create_deck())
            # Ziehe eine Hand mit der angegebenen Größe (z.B. 5 Karten)
            hand = deal_cards(deck, hand_size)
            if not hand:
                continue  # Wenn keine Hand gezogen werden konnte, überspringe die Iteration
            # Überprüfe die Hand, um die Pokerhand zu ermitteln
            hand_type = check_hand(hand)
            hand_statistics[hand_type] += 1
        except Exception as e:
            print(f"Error during simulation: {e}")
            continue  # Fahre mit der nächsten Simulation fort, falls ein Fehler auftritt
    
    # Berechne den prozentualen Anteil jeder Hand am Gesamtergebnis
    for hand_type in hand_statistics:
        hand_statistics[hand_type] = (hand_statistics[hand_type] / n) * 100

    return hand_statistics

@timer
@debug
def main():
    n, hand_size = user_input()
    hand_statistics = simulate_poker_hands(n, hand_size)  # Simuliere Pokerhände mit 5 Karten
    for hand_type, percentage in hand_statistics.items():
        print(f'{hand_type}: {percentage:.5f}%')

if __name__ == '__main__':
    main()
