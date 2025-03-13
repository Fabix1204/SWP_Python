# Klasse für ein Listenelement
class ListElement:
    def __init__(self, obj):
        self.obj = obj  # Das Objekt, das im Listenelement gespeichert wird
        self.next = None  # Zeiger auf das nächste Listenelement

# Klasse für die verkettete Liste
class LinkedList:
    def __init__(self):
        self.head = ListElement("Head")  # Kopf der Liste, enthält kein nützliches Objekt
        
    # Methode zum Hinzufügen eines Elements am Ende der Liste
    def add_last(self, obj):
        new_element = ListElement(obj)  # Neues Listenelement erstellen
        last_element = self.get_last_element()  # Letztes Element der Liste finden
        last_element.next = new_element  # Neues Element als nächstes Element des letzten Elements setzen
        
    # Methode zum Einfügen eines Elements nach einem bestimmten Element
    def insert_after(self, prev_obj, new_obj):
        pointer_elem = self.head.next  # Start bei dem ersten echten Element
        while pointer_elem and pointer_elem.obj != prev_obj:
            pointer_elem = pointer_elem.next  # Weiter zum nächsten Element, bis das vorherige Element gefunden wird
        if pointer_elem:
            new_elem = ListElement(new_obj)  # Neues Listenelement erstellen
            new_elem.next = pointer_elem.next  # Zeiger des neuen Elements auf das nächste Element setzen
            pointer_elem.next = new_elem  # Zeiger des vorherigen Elements auf das neue Element setzen
            
    # Methode zum Löschen eines Elements
    def delete(self, obj):
        le = self.head  # Start bei dem Kopf der Liste
        while le.next and le.next.obj != obj:
            le = le.next  # Weiter zum nächsten Element, bis das zu löschende Element gefunden wird
        if le.next:
            le.next = le.next.next  # Zeiger des vorherigen Elements auf das übernächste Element setzen
    
    # Methode zum Finden eines Elements
    def find(self, obj):
        le = self.head  # Start bei dem Kopf der Liste
        while le:
            if le.obj == obj:
                return True  # Element gefunden
            le = le.next  # Weiter zum nächsten Element
        return False  # Element nicht gefunden
    
    # Methode zum Abrufen des ersten Elements
    def get_first_elem(self):
        return self.head.next  # Das erste echte Element zurückgeben
    
    # Methode zum Abrufen des letzten Elements
    def get_last_element(self):
        le = self.head  # Start bei dem Kopf der Liste
        while le.next:
            le = le.next  # Weiter zum nächsten Element, bis das letzte Element gefunden wird
        return le  # Letztes Element zurückgeben
    
    # Methode zum Ausgeben der gesamten Liste
    def write_list(self):
        le = self.head.next  # Start bei dem ersten echten Element
        while le:
            print(le.obj)  # Objekt des aktuellen Elements ausgeben
            le = le.next  # Weiter zum nächsten Element
            
# Hauptfunktion zum Testen der verketteten Liste
def main():
    try:
        l = LinkedList()  # Neue verkettete Liste erstellen
        l.add_last("1")
        l.add_last("2")
        l.add_last("3")
        l.add_last("4")
        l.add_last("5")
        l.write_list()  # Liste ausgeben
        print()
        l.insert_after("3", "3.5")  # Element nach "3" einfügen
        l.write_list()  # Liste ausgeben
        print()
        l.delete("3")  # Element "3" löschen
        l.write_list()  # Liste ausgeben
    except Exception as error:
        print(f"Unexpected error: {error}")  # Fehler ausgeben
        import sys
        sys.exit(1)  # Programm beenden

# Wenn dieses Skript direkt ausgeführt wird, die Hauptfunktion aufrufen
if __name__ == '__main__':
    main()