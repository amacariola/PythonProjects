# Left > Root > Right 
# in order traversal

class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    # Insert the node
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    def preordertraversal(self,root):
        res = []
        if root:
            res.append(root.data)
            res= res + self.preordertraversal(root.left)
            res= res + self.preordertraversal(root.right)
        return res
    def postordertraversal(self,root):
        res = []
        if root:
            res= res + self.postordertraversal(root.left)
            res= res + self.postordertraversal(root.right)
            res.append(root.data)
        return res



root = Node(27)
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(4)
root.insert(5)
root.insert(6)


print(root.inorderTraversal(root))
print(root.preordertraversal(root))
print(root.postordertraversal(root))