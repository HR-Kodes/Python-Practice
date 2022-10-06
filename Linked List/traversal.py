class Node :
    def __init__ (self , val=None , next=None) :
        self.val = val
        self.next = None

class linkedlist:
    def __init__ (self) :
        self.head = None

        # Printing linked list elements uing loops

    def traversal_loop (self , head):
        temp = self.head
        while temp is not None :
            print(temp.val)
            temp = temp.next

# Print linked list elements recursively

def traversal_recur (head):
        if head is None :
            return
        print (head.val)
        traversal_recur (head.next)

link_list = linkedlist ()
link_list.head = Node ('A')
b = Node ('B')
c = Node ('C')
d = Node ('D')

link_list.head.next = b
b.next = c
c.next = d

print('Looping way')
link_list.traversal_loop(link_list.head)
print('Using recursive way')
traversal_recur(link_list.head)
