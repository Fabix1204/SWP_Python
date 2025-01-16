class Auto:
    def __init__(self, ps):
        if not isinstance(ps, (int, float)) or ps <= 0:
            raise ValueError("PS (horsepower) must be a positive number.")
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Auto):
            return self.ps + other.ps
        raise TypeError("Addition is only supported between Auto instances.")

    def __sub__(self, other):
        if isinstance(other, Auto):
            return self.ps - other.ps
        raise TypeError("Subtraction is only supported between Auto instances.")

    def __mul__(self, other):
        if isinstance(other, Auto):
            return self.ps * other.ps
        raise TypeError("Multiplication is only supported between Auto instances.")

    def __eq__(self, other):
        if isinstance(other, Auto):
            return self.ps == other.ps
        raise TypeError("Equality comparison is only supported between Auto instances.")

    def __lt__(self, other):
        if isinstance(other, Auto):
            return self.ps < other.ps
        raise TypeError("Less-than comparison is only supported between Auto instances.")

    def __gt__(self, other):
        if isinstance(other, Auto):
            return self.ps > other.ps
        raise TypeError("Greater-than comparison is only supported between Auto instances.")

    def __len__(self):
        return self.ps

    def __repr__(self):
        return f"Auto({self.ps} PS)"

# Testzeilen
def test_auto():
    a1 = Auto(50)
    a2 = Auto(60)

    # Addition
    print(a1 + a2)  # 110

    # Subtraktion
    print(a2 - a1)  # 10

    # Multiplikation
    print(a1 * a2)  # 3000

    # Vergleiche
    print(a1 == a2)  # False
    print(a1 < a2)   # True
    print(a1 > a2)   # False

    # len()
    print(len(a1))  # 50

    # Repräsentation
    print(a1)  # Auto(50 PS)

    # Fehlerbehandlungen
    try:
        print(a1 + 10)  # TypeError
    except TypeError as e:
        print(e)

    try:
        print(a1 - "test")  # TypeError
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    test_auto()
