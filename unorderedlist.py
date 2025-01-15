"""
My unorderedlist file
"""


from node import Node
from errors import ValueTooBig
from errors import NoValueFound
from errors import NoValueInIndex

class UnorderedList():
    """
    my class
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Min funktion som lägger till värde till min node
        """
        current = self.head
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
        else:
            while current.next != None:
                current = current.next
            current.next = new_node


    def get(self, value):
        """
        Söker efter ett värde
        """
        current = self.head
        while current.next != None:
            if current.data == value:
                print(value)
                return True
            current = current.next
        if current.data == value:
            print(value)
            return True
        # return False
        raise NoValueFound("No value found")

    def remove(self, index):
        """
        Ta bort ett värde
        """
        current = self.head
        previous = None
        counter = 0
        while current is not None:
            if counter == index:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return

            previous = current
            current = current.next
            counter += 1

        raise ValueTooBig("Index out of bounds")

    def print(self):
        """
        printar min node
        """
        current = self.head
        while current.next != None:
            print(current.data)
            current = current.next
        print(current.data)

    def size(self):
        """
        vissar storleken
        """
        current = self.head
        counter = 1
        while current.next != None:
            current = current.next
            counter += 1
        print(counter)

    def set(self, index, newdata):
        """
        lägger till ett värde i en speciel plats

        """
        current = self.head
        previous = None
        for i in range(index):
            previous = current
            current = current.next
        if current != None:
            temp = Node(newdata)
            temp.set_next(current)
            if previous is None:
                self.head = temp
            else:
                previous.set_next(temp)
        else:
            raise NoValueInIndex("index out of range")



    def main_list(self):
        """
        min loop
        """
        while True:
            print("1. Lägg till  värde")
            print("2. Ta bort värde")
            print("3. kolla på värde")
            print("4. kolla på hela lista")
            print("5. Välj ett plats ock värde")
            print("6. Kolla på storleken")
            print("7. quit \n")
            inp = input("vad vill du ha: ")

            if inp == "7":
                break

            if inp == "1":
                value = input("skriv in ditt värde: ")
                self.append(value)
                print(self.head.data)

            if inp == "2":
                index = int(input("tog bort ett värde: "))
                try:
                    self.remove(index)
                except ValueTooBig:
                    print("\nFinns inget värde i den platsen\n")

            if inp == "3":
                value = input("vad vill du söka på: ")
                try:
                    self.get(value)
                except NoValueFound:
                    print("\nDet värde finns inte\n")

            if inp == "4":
                print(self.print())

            if inp == "6":
                self.size()

            if inp == "5":
                index = int(input("Index: "))
                value = input("Värde: ")
                try:
                    self.set(index, value)
                except NoValueInIndex:
                    print("Inget värde i den platsen")





if __name__ == "__main__":


    ll = UnorderedList()
    ll.main_list()
    # ll.append(9)
    # ll.append(5)
    # print(ll)
    # ll.append(7)
    # ll.print()
    # print("hej")
    # try:
    #     ll.remove(value)
    # except ValueTooBig:
    #     print("Gick inte")
    # ll.print()
    # print("hej")
    # try:
    #     ll.search(9)
    # except NoValueFound:
    #     print("hitade inte")
