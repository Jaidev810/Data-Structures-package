class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None


class LinkedList:
    def takeInput(self) -> Node:
        inputlist = [int(x) for x in input().split()]
        head = None
        temp = None

        for cur in inputlist:
            if cur == -1:
                break
            Newnode = Node(cur)
            if head is None:
                head = Newnode
                temp = head
            else:
                temp.next = Newnode
                temp = temp.next

        return head

    def PrintLL(self, head:Node) -> None:
        temp = head
        while temp is not None:
            print(temp.val, end='->')
            temp = temp.next

        print("None")

    def getLength(self, head:Node) -> int:
        count = 0
        temp = head

        while temp is not None:
            count += 1
            temp = temp.next

        return count

    def getMiddle(self, head:Node) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.val

    def reverseLL(self, head: Node) -> Node:
        if head is None or head.next is None:
            return head
        new_head = self.reverseLL(head.next)
        head.next.next = head
        head.next = None
        
        return new_head




