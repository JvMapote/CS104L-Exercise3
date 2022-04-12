class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
class doubly_linked_list(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def append_item(self, data):
        new_item = Node(data, None, None)
        if self.head is None:
            self.head = new_item
            self.tail = self.head
        else:
            new_item.prev = self.tail
            self.tail.next = new_item
            self.tail = new_item
        self.count += 1
    def print_foward(self):
        for node in self.iter():
            if(node=="Exit"):
                break
            print(node)
    def iter(self):
        current = self.head
        while current:
            item_val = current.data
            current = current.next
            yield item_val

items = doubly_linked_list()
count = 0
print("Note: Write [Exit] if you want to search\n")
while (count < 1): 
    value = input("Enter Node:")
    items.append_item(value);
    if(value == "Exit"):
        count = count + 1

print("\nItems in the Doubly linked list: ")
items.print_foward()
