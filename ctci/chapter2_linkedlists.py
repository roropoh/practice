class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing
    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node = node.next
    def remove_duplicates(self):
        els = []
        node = self
        previous = None
        while node != None:
            if node.val in els:
                previous.next = node.next
            else:
                els.append(node.val)
            previous = node
            node = node.next

def question2_1():
    print("2.1 - remove duplicates from an unsorted linked list")
    node1 = Node(10)
    node2 = Node(6)
    node3 = Node(23)
    node4 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.remove_duplicates()
    node1.traverse()

def main():
    question2_1()

if __name__== "__main__":
    main()
