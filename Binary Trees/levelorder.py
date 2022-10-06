class Node :
    def __init__ (self , val) :
        self.left = None
        self.right = None
        self.val = val

def levelorder (root) :
    if root == None :
        return

    queue = []
    queue.append(root)
    queue.append(None)

    while queue != [] :
        currNode = queue.pop(0)
        if (currNode == None) :
            print()
            if (queue == []) :
                break
            else :
                queue.append(None)
        else :
            print(currNode.val,end = ' ')
            if (currNode.left != None) :
                queue.append (currNode.left)
            if (currNode.right != None) :
                queue.append (currNode.right)

if __name__ == "__main__" :
    root = Node (1)
    root.left = Node (2)
    root.right = Node (3)
    root.left.right = Node (4)

    levelorder (root)
