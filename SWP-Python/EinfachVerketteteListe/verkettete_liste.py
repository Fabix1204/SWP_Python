class ListElement:
    def __init__(self, obj):
        self.obj = obj
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListElement("Head")
        
    def add_last(self, obj):
        new_element = ListElement(obj)
        last_element = self.get_last_element()
        last_element.next = new_element
        
    def insert_after(self, prev_obj, new_obj):
        pointer_elem = self.head.next
        while pointer_elem and pointer_elem.obj != prev_obj:
            pointer_elem = pointer_elem.next
        if pointer_elem:
            new_elem = ListElement(new_obj)
            new_elem.next = pointer_elem.next
            pointer_elem.next = new_elem
            
    def delete(self, obj):
        le = self.head
        while le.next and le.next.obj != obj:
            le = le.next
        if le.next:
            le.next = le.next.next
    
    def find(self, obj):
        le = self.head
        while le:
            if le.obj == obj:
                return True
            le = le.next
        return False
    
    def get_first_elem(self):
        return self.head.next
    
    def get_last_element(self):
        le = self.head
        while le.next:
            le = le.next
        return le
    
    def write_list(self):
        le = self.head.next
        while le:
            print(le.obj)
            le = le.next
            
def main():
    try:
        l = LinkedList()
        l.add_last("1")
        l.add_last("2")
        l.add_last("3")
        l.add_last("4")
        l.add_last("5")
        l.write_list()
        print()
        l.insert_after("3", "3.5")
        l.write_list()
        print()
        l.delete("3")
        l.write_list()
    except Exception as error:
        print(f"Unexpected error: {error}")
        import sys
        sys.exit(1)

if __name__ == '__main__':
    main()