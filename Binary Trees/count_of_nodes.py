class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def count_of_nodes (root) :
    if root == None :
        return 0

    leftnodes = count_of_nodes (root.left)
    rightnodes = count_of_nodes (root.right)

    return leftnodes + rightnodes + 1

if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    print(count_of_nodes (root))

# Time Complexity = O(N)
