class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def search_element (root , target) :
    if root == None :
        return

    if root.val == target :
        print('Target @ ' + str(root.val))
    if root.left :
        search_element (root.left , target)
    if root.right :
        search_element (root.right , target)

if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    search_element(root , 3)
