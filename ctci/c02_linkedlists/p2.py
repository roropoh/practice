'''
P2. Remove duplicates from a linked list
'''

import p1

class Node(p1.Node):
    def remove_dups(self):
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
