# Raum: Einzelzimmer, Doppelzimmer, besetzt/frei, Bezeichnung
# Hotel: Verwaltung der Räume, (Raum buchen, nächstes Frei, stornieren), Methode Anzahl der freien Zimmer
# Main ausprobieren

class Raum:
    def __init__(self, bezeichnung):
        self.bezeichnung = bezeichnung
        self.besetzt = False

    def buchen(self):
        if self.besetzt:
            print(f"Raum {self.bezeichnung} ist bereits belegt.")
        else:
            self.besetzt = True
            print(f"Raum {self.bezeichnung} wurde gebucht.")

    def stornieren(self):
        if self.besetzt:
            self.besetzt = False
            print(f"Raum {self.bezeichnung} wurde storniert.")
        else:
            print(f"Raum {self.bezeichnung} ist nicht belegt.")
            
class Einzelzimmer(Raum):
    def __init__(self, bezeichnung):
        super().__init__(bezeichnung)
        self.bezeichnung = bezeichnung
        
class Doppelzimmer(Raum):
    def __init__(self, bezeichnung):
        super().__init__(bezeichnung)
        self.bezeichnung = bezeichnung
        
class Hotel:
    def __init__(self):
        self.raeume = []
        
    def add_raum(self, raum):
        self.raeume.append(raum)
        
    def buchen(self, raum):
        raum.buchen()
        
    def stornieren(self, raum):
        raum.stornieren()
        
    def naechstes_freies_zimmer(self):
        for raum in self.raeume:
            if not raum.besetzt:
                return raum
        return None
    
    def anzahl_freie_zimmer(self):
        return len([raum for raum in self.raeume if not raum.besetzt])
    
def main():
    h = Hotel()
    
    e1 = Einzelzimmer("EZ1")
    e2 = Einzelzimmer("EZ2")
    d1 = Doppelzimmer("DZ1")
    d2 = Doppelzimmer("DZ2")
    
    h.add_raum(e1)
    h.add_raum(e2)
    h.add_raum(d1)
    h.add_raum(d2)
    
    h.buchen(e1)
    h.buchen(d1)
    h.stornieren(d1)
    
    print(h.anzahl_freie_zimmer())
    
    h.buchen(h.naechstes_freies_zimmer())
    
    print(h.anzahl_freie_zimmer())
    
if __name__ == "__main__":
    main()