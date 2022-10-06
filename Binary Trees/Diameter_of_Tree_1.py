class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def height_of_tree (root) :
    if root == None :
        return 0

    left = height_of_tree (root.left)
    right = height_of_tree (root.right)

    myheight = max (left , right) + 1
    return myheight

def diameter_of_tree (root) :
    if root == None :
        return 0

    diam1 = diameter_of_tree (root.left)
    diam2 = diameter_of_tree (root.right)
    diam3 = height_of_tree (root.left) + height_of_tree (root.right) + 1

    return max (diam3 , max (diam1 , diam2))

if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    print(diameter_of_tree (root))

# Time Complexity = O(N)
