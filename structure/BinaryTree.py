import queue

class Node:
    def __init(self, val: int):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def takeinput(self) -> Node:
        print("enter root's data: ")
        rootData = int(input())
        if rootData == -1:
            return None

        root = BinaryTree(rootData)
        q = queue.Queue()
        q.put(root)

        while not q.empty():
            cur = q.get()
            print("enter the left child of : ", cur)
            leftData = int(input())
            if leftData != -1:
                leftChild = Node(leftData)
                cur.left = leftChild
                q.put(cur.left)
            print("enter the right child of : ", cur)
            rightData = int(input())
            if rightData != -1:
                rightchild = Node(rightData)
                cur.right = rightchild
                q.put(cur.right)
        return root

    def printLevelWise(self, root: Node) -> None:
        if root is None:
            return None
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            curr = q.get()
            print(curr, end=':')
            if curr.left is not None:
                print(curr.left.val, end=',')
                q.put(curr.left)
            if curr.right is not None:
                print(curr.right.val, end='')
                q.put(curr.right)
            print()


    ## Traversal ##
    def levelorder(self, root: Node) -> list:
        arr = []
        q = []
        if root is None:
            return root
        q.append(root)
        q.append(None)
        temp = []
        while len(q) != 0:
            curr_node = q.pop(0)
            if curr_node is None:
                if len(q) == 0 and len(temp) == 0:
                    break
                else:
                    arr.append(temp)
                    temp = []
                    q.append(None)
            else:
                if curr_node.left is not None:
                    q.append(curr_node.left)

                if curr_node.right is not None:
                    q.append(curr_node.right)

                temp.append(curr_node.val)
        return arr


    def preorder(self, root: Node) -> None:
        if root is not None:
            print(root.val, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)
        return
    
    def inorder(self, root: Node) -> None:
        if root is not None:
            self.inorder(root.left)
            print(root.val, end=' ')
            self.inorder(root.right)
        return

    def postorder(self, root:Node) -> None:
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=' ')
        return 