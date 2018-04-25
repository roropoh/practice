'''
P3. find the nth to last element of a singly linked list.
'''

import p2

class Node(p2.Node):
    def find_nth_element(self):
        arry = []
        node = self
        previous = None
        while node != None:
            if node.val in arry:
                previous.next = node.next
            else:
                arry.append(node.val)
            previous = node
            node = node.next

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.remove_dups()
    node1.traverse()
    node1.find_nth_element()
