class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def inorder (root) :
    if root :
        inorder (root.left)
        print(root.val)
        inorder (root.right)

def preorder (root) :
    if root :
        print(root.val)
        preorder (root.left)
        preorder (root.right)

def postorder (root) :
    if root :
        postorder (root.left)
        postorder (root.right)
        print(root.val)

if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    inorder (root)
    print ()
    preorder (root)
    print ()
    postorder (root)
