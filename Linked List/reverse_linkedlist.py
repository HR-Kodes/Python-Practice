class Node :
    def __init__ (self , val = None , next = None) :
        self.val = val
        self.next = None

class linkedlist :
    def __init__ (self) :
        self.head = None

# Looping way of reversing given linked list

def reverse_link_list_loop (head) :
    prev = None
    curr = head
    while (curr != None) :
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    printing_link_list(prev)

def printing_link_list (head) :
    curr = head
    while (curr != None) :
        print(curr.val,end = ' ')
        curr = curr.next
    print()

# Recurssive approach to reverse a linked list NOTE : NOT WORKING RECURSSIVE WAY

def reverse_link_list_recurr (head) :
    ans = recurssive_function (head)
    print(ans)
def recurssive_function (head , prev = None) :
    if (head == None) : return prev
    next = head.next
    head.next = prev
    return recurssive_function (next , head)



link_list = linkedlist ()
link_list.head = Node ('A')        # Declaring linked list - 1 head as 'A'
b = Node ('B')                      # Creating another node 'B'
c = Node ('C')                      # creating one more node 'C'
d = Node ('D')                      # creating another node 'D'

link_list.head.next = b            # Defining link between nodes 'A' & 'B'
b.next = c                          # Linking nodes 'B' and 'C'
c.next = d                          # Linking nodes 'C' and 'D'


printing_link_list (link_list.head)
reverse_link_list_loop (link_list.head)
reverse_link_list_recurr(link_list.head)
