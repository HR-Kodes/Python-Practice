class Node :                        # Creating 'Node' class
    def __init__ (self , val=None , next=None):
        self.val = val              # Adding node values
        self.next = None            # Initially specifing next node as None

class linkedlist :                  # Creating linked list class with 'head'
    def __init__ (self) :
        self.head = None            # Initially declaring 'head' of linked list as None

def link_list_values_loop (head) :       # Function to get all linked list Node values in a list
    if (head == None) :             # Checking if 'head' of given linked list is None
        print("Nothing to print")
        return
    arr = []
    curr = head
    while (curr != None) :
        arr.append(curr.val)
        curr = curr.next
    print(arr)

def link_list_values_recur (head , arr = []) :
    if head == None :
        print(arr)
        return
    arr.append(head.val)
    link_list_values_recur (head.next , arr)

link_list1 = linkedlist ()          # Initilizing linked list - 1
link_list2 = linkedlist ()          # Initilizing linked list - 2

link_list1.head = Node ('A')        # Declaring linked list - 1 head as 'A'
b = Node ('B')                      # Creating another node 'B'
c = Node ('C')                      # creating one more node 'C'
d = Node ('D')                      # creating another node 'D'

link_list1.head.next = b            # Defining link between nodes 'A' & 'B'
b.next = c                          # Linking nodes 'B' and 'C'
c.next = d                          # Linking nodes 'C' and 'D'

print('Printing linked list node values using looping approach')

link_list_values_loop (link_list1.head)   # Passing linked list - 1 to get its values as > ['A', 'B', 'C', 'D']
link_list_values_loop (link_list2.head)   # Passing linked list - 2 to get its values as > Nothing to print

print('Printing linked list node values using recusive approach')

link_list_values_recur (link_list1.head)
link_list_values_recur (link_list2.head)
