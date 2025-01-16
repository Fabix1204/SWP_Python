class Person:
    def __init__(self, name, gender):
        if gender not in ["male", "female"]:
            # c) Neuer Fehler und NICHT behebar
            raise ValueError("Gender must be 'male' or 'female'")
        self.name = name
        self.gender = gender


class Mitarbeiter(Person):
    def __init__(self, name, gender, abteilung):
        super().__init__(name, gender)
        self.abteilung = abteilung
        try:
            # b) Hochblubber-Fehler und behebar
            abteilung.add_mitarbeiter(self)
        except AttributeError:
            raise ValueError("Invalid Abteilung object")


class Abteilungsleiter(Mitarbeiter):
    def __init__(self, name, gender, abteilung):
        if abteilung.leiter is not None:
            # c) Neuer Fehler und NICHT behebar
            raise ValueError(f"Abteilung {abteilung.name} already has a leader")
        super().__init__(name, gender, abteilung)
        abteilung.set_leiter(self)


class Abteilung:
    def __init__(self, name: str):
        self.name = name
        self.mitarbeiter = []
        self.leiter = None

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)

    def set_leiter(self, leiter: Abteilungsleiter):
        self.leiter = leiter

    def mitarbeiter_anzahl(self):
        return len(self.mitarbeiter)


class Firma:
    def __init__(self, name: str):
        self.name = name
        self.abteilungen = []

    def add_abteilung(self, abteilung: Abteilung):
        # a) Neuer Fehler und behebar
        if not isinstance(abteilung, Abteilung):
            raise ValueError("Only Abteilung instances can be added")
        self.abteilungen.append(abteilung)

    def gesamt_mitarbeiter(self):
        return sum(abt.mitarbeiter_anzahl() for abt in self.abteilungen)

    def gesamt_abteilungsleiter(self):
        return sum(1 for abt in self.abteilungen if abt.leiter is not None)

    def gesamt_abteilungen(self):
        return len(self.abteilungen)

    def groesste_abteilung(self):
        try:
            # b) Hochblubber-Fehler und behebar
            return max(self.abteilungen, key=lambda abt: abt.mitarbeiter_anzahl())
        except ValueError:
            return None

    def gender_verteilung(self):
        total_male = total_female = 0
        for abteilung in self.abteilungen:
            for mitarbeiter in abteilung.mitarbeiter:
                if mitarbeiter.gender == "male":
                    total_male += 1
                elif mitarbeiter.gender == "female":
                    total_female += 1
        total = total_male + total_female
        male_percent = (total_male / total * 100) if total > 0 else 0
        female_percent = (total_female / total * 100) if total > 0 else 0
        return male_percent, female_percent


def main():
    try:
        # Erstellung der Firmenstruktur
        firma = Firma("Apple Inc.")

        # Abteilungen erstellen
        it = Abteilung("IT")
        hr = Abteilung("HR")
        firma.add_abteilung(it)
        firma.add_abteilung(hr)

        # Mitarbeiter und Abteilungsleiter instanzieren
        leiter_it = Abteilungsleiter("Alice", "female", it)
        m1_it = Mitarbeiter("Bob", "male", it)
        m2_it = Mitarbeiter("Charlie", "male", it)
        leiter_hr = Abteilungsleiter("Diana", "female", hr)
        m1_hr = Mitarbeiter("Eve", "female", hr)

        # Methoden testen
        print("Firma:", firma.name)
        print("Gesamtmitarbeiter:", firma.gesamt_mitarbeiter())
        print("Gesamtabteilungsleiter:", firma.gesamt_abteilungsleiter())
        print("Gesamtabteilungen:", firma.gesamt_abteilungen())
        groesste = firma.groesste_abteilung()
        if groesste:
            print("Größte Abteilung:", groesste.name)
        else:
            print("Keine Abteilungen vorhanden")
        male_percent, female_percent = firma.gender_verteilung()
        print(f"Geschlechterverteilung: {male_percent:.2f}% Männer, {female_percent:.2f}% Frauen")
    except Exception as error:
        # d) Hochblubber-Fehler und NICHT behebar
        print(f"Unexpected error: {error}")
        import sys
        sys.exit(1)


if __name__ == "__main__":
    main()
