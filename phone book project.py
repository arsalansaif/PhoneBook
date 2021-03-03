import re
import sys

class Node(object):

    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def get_prev(self):
        return self.prev_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_prev(self, new_prev):
        self.prev_node = new_prev

class DoublyLinkedList(object):

    def __init__(self, head=None, end=None):
        self.head = head
#O(1)
    def list_insert(self, data):
        n = Node(data)
        n.next_node = self.head
        n.prev_node = None
        if self.head is not None:
            self.head.set_prev(n)
        self.head = n
        self.list_sort()
#O(n^2)
    def list_sort(self):
        if self.head is None:
            return;
        else:
            current = self.head
            while current.next_node is not None:
                index = current.next_node;
                while index is not None:
                    if current.data > index.data:
                        temp = current.data;
                        current.data = index.data;
                        index.data = temp;
                    index = index.next_node
                current = current.next_node
#O(n)
    def list_print(self):
        self.list_sort()
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next_node
# search time + O(1)
    def list_remove(self, element):
        if self.head is None:
            print("The list is empty!")
            return

        if self.head.next_node is None:
            if self.head.data == element:
                self.head = None
            else:
                print("The desired item was not found!")
            return

        if self.head.data == element:
            self.head = self.head.next_node
            self.head.prev_node = None
            return

        n = self.head
        while n.next_node is not None:
            if n.data == element:
                break
            n = n.next_node

        if n.next_node is not None:
            n.prev_node.next_node = n.next_node
            n.next_node.prev_node = n.prev_node
        else:
            if n.data == element:
                n.prev_node.next_node = None
            else:
                print("The desired item was not found!")
#O(n)
    def list_search(self, substring):
        current_node = self.head
        chosen_contacts = []
        while current_node is not None:
            subs = substring.lower()
            curr = current_node.data.lower()
            if subs in curr:
                chosen_contacts.append(current_node.data)
            current_node = current_node.next_node
        if len(chosen_contacts) > 0:
            for item in chosen_contacts:
                print(item)
        else:
            print("The desired item was not found!")
        print()
#search time + O(1)
    def list_search_remove(self, substring):
        current_node = self.head
        chosen_contacts = []
        while current_node is not None:
            subs = substring.lower()
            curr = current_node.data.lower()
            if subs in curr:
                chosen_contacts.append(current_node.data)
            current_node = current_node.next_node
        counter = 1
        if len(chosen_contacts) > 0:
            for item in chosen_contacts:
                print(str(counter) + ". " + item)
                counter += 1
            print("Choose the number of element that you'd like to remove: ")
            num = int(input())
            if (num-1) >= len(chosen_contacts):
                print("Incorrect input!")
            else:
                self.list_remove(chosen_contacts[num-1])
                print("\nThe updated list is: ", end="")
                self.list_print()
        else:
            print("The desired item was not found!")
        print()

DLL = DoublyLinkedList()
path = 'contacts.txt'
with open(path) as f:
    line = f.readline()
    while line:
        line = f.readline()
        element = re.split('\n', line)
        DLL.list_insert(element[0])

k = True
print("<<< WELCOME TO THE PHONE DIRECTORY APPLICATION! >>>")
while k:
    print("\nMain Menu")
    print("1. Add Contact")
    print("2. Print Contacts")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")
    print("Your choice is: ")
    choice = int(input())
    if choice == 5:
        k = False
        print("<<< THANK YOU FOR USING THE PHONE DIRECTORY APPLICATION! >>>")
        sys.exit()
    if choice <= 0 or choice >= 6:
        print("Invalid input!")
    if choice == 1:
        print("\nEnter the name: ")
        name = input()
        print("Enter the number: ")
        number = input()
        entry = name + ":" + number
        DLL.list_insert(entry)
    if choice == 2:
        DLL.list_print()
    if choice == 4:
        t = True
        str = ""
        print("\nEnter the characters for searching or Enter / to stop: ")
        while t:
            print("Look for: ", end="")
            char = input(str)
            if char == "/":
                t = False
            else:
                str += char
                DLL.list_search(str)
    if choice == 3:
        print("\nEnter the info about the element you'd like to remove: ")
        info = input()
        DLL.list_search_remove(info)
