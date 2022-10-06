class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def sum_of_nodes (root) :
    if root == None :
        return 0

    leftsum = sum_of_nodes (root.left)
    rightsum = sum_of_nodes (root.right)

    return leftsum + rightsum + root.val

if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    print(sum_of_nodes (root))

# Time Complexity = O(N)
