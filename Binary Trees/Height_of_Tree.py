class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def heigth_of_tree (root) :
    if root == None :
        return 0

    left = heigth_of_tree (root.left)
    right = heigth_of_tree (root.right)

    myheight = max (left , right) + 1
    return myheight


if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    print(heigth_of_tree (root))

# Time Complexity = O(N)
