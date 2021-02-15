class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class CircularLL:
    def takeinputLL(self) -> Node:
        inputLL = [int(x) for x in input().split()]
        head = None
        temp = None

        for curr in inputLL:
            if curr == -1:
                break
            Newnode = Node(curr)
            if head is None:
                head = Newnode
                Newnode.next = head
                temp = head
            else:
                temp.next = Newnode
                Newnode.next = head
                temp = temp.next

        return head


    def printLL(self, head:Node) -> None:
        print(head.val, end='->')
        temp = head.next
        while temp != head:
            print(temp.val, end='->')
            temp = temp.next

        print("None")
        return 


    def reverseLL(self, head:Node) -> Node:
        if head is None:
            return None

        prev = None
        curr = head
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        while curr != head:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head.next = prev
        head = prev
        return head

