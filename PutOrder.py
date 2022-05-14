class PutOrder:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 

def insert(root, key):
    if root is None:
        return PutOrder(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root
 
def putorder(root):
    if root:
        putorder(root.left)
        print(root.val)
        putorder(root.right)
 
 
r = PutOrder(100)
r = insert(r, 50)
r = insert(r, 150)
r = insert(r, 200)

 
putorder(r)