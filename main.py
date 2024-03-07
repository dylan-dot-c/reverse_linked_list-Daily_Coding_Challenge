class Node:
    "class for a node in a link list"
    def __init__(self, val: str):
        self.val = val
        self.next = None

class LinkedList:
    "class for managing nodes"
    def __init__(self):
        self.head = None

    def add_to_start(self, val: str):
        "add new node to the start of the linkedList"
        newNode = Node(val)
        # the new node will now reference the old head node
        newNode.next = self.head
        # head now points to the new node
        self.head = newNode

    def add_to_end(self, val:str):
        "add new node to the end of the linkedList"
        newNode = Node(val)
        # if linkedList is empty
        # assign head as the newNode
        if not self.head:
            self.head = newNode
        else:
            # get a copy of the head, so it wont affect
            # it when we leave this scope
            current_node = self.head

            # while there is a next node in the linkedList
            # going to the end of the Linkedlist to add new node
            while(current_node.next):
                current_node = current_node.next

            current_node.next = newNode

    def __repr__(self):
        "function to print all values in the linked_list"
        # making a copy
        head = self.head
        if not head:
            return "*Linked List is Empty*"
        words = []
        # looping through nodes and printing values
        while(head):
            words.append(head.val)
            head = head.next

        return " ".join(words)
        

    def reverse_list(self):
        "function to return a reversed LinkedList of the current one"
        current_node = self.head
        # new instance
        new_list = LinkedList()
        while(current_node):
            # looping through each node and add it to the end
            # basically enqueue the node to the list
            # so last will be first and first be last
            new_list.add_to_start(current_node.val)
            current_node = current_node.next
        
        # return new linkedList
        return new_list        

linked_list = LinkedList()
linked_list.add_to_end("I")
linked_list.add_to_end("Like")
linked_list.add_to_end("To")
linked_list.add_to_end("Write")
linked_list.add_to_end("Code")

print("ORIGINAL")
print(linked_list)

print("REVERSED")
reversed_list = linked_list.reverse_list()
print(reversed_list)