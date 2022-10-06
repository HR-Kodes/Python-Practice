class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def max_element (root) :
    if root == None :
        return float('-inf')
    max = root.val

    leftmax = max_element (root.left)
    rightmax = max_element (root.right)

    if leftmax > max :
        max = leftmax
    if rightmax > max :
        max = rightmax

    return max

def min_element (root) :
    if root == None :
        return float('inf')

    min = root.val

    leftmin = min_element (root.left)
    rightmin = min_element (root.right)
    if leftmin < min :
        min = leftmin
    if rightmin < min :
        min = rightmin

    return min

if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    print(max_element (root))
    print()
    print(min_element (root))
