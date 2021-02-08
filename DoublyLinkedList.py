class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def takeinput(self) -> Node:
        inputlist = [int(x) for x in input().split()]
        head = None
        temp = None

        for curr in inputlist:
            if curr == -1:
                break
            Newnode = Node(curr)
            if head is None:
                head = Newnode
                temp = head
            else:
                temp.next = Newnode
                Newnode.prev = temp
                temp = temp.next
        return head


    def printLL(self, head: Node) -> None:
        temp = head
        while temp is not None:
            print(temp.val, end='->')
            temp = temp.next
        print("None")

    def getLength(self, head: Node) -> int:
        count = 0
        temp = head
        while temp is not None:
            count += 1
            temp = temp.next
        return temp

    def getMiddle(self, head: Node) -> int:
        slow = head
        fast = head

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.val

    def reverseLL(self, head: Node) -> Node:
        pass