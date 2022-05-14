class InOrder:

    def __init__(root, key):

        root.left = None
        root.right = None
        root.key = key

    def insert(root, key):

        if root.key:
            if key < root.key:
                if root.left is None:
                    root.left = InOrder(key)
                else:
                    root.left.insert(key)
            elif key > root.key:
                if root.right is None:
                    root.right = InOrder(key)
                else:
                    root.right.insert(key)
        else:
            root.key = key

    def PrintTree(root):
        if root.left:
            root.left.PrintTree()
        print( root.key),
        if root.right:
            root.right.PrintTree()

    def inorderTraversl(root, r):
        res = []
        if r:
            res = root.inorderTraversl(r.left)
            res.append(r.key)
            res = res + root.inorderTraversl(r.right)
        return res

r = InOrder(27)
r.insert(14)
r.insert(35)
r.insert(10)
r.insert(19)
r.insert(31)
r.insert(42)
print(r.inorderTraversal(r))