class Node :                        # Creating 'Node' class
    def __init__ (self , val=None , next=None):
        self.val = val              # Adding node values
        self.next = None            # Initially specifing next node as None

class linkedlist :                  # Creating linked list class with 'head'
    def __init__ (self) :
        self.head = None            # Initially declaring 'head' of linked list as None

def zipper_list_loop (head1 , head2) :
    tail = head1
    curr1 = head1.next
    curr2 = head2
    count = 0

    while (curr1 != None and curr2 != None) :
        if (count % 2 == 0) :
            tail.next = curr2
            curr2 = curr2.next
        else :
            tail.next = curr1
            curr1 = curr1.next
        tail = tail.next
        count += 1

    if (curr1 != None) : tail.next = curr1
    if (curr2 != None) : tail.next = curr2

    # Printing linked list after merging
    if head1 :
        curr = head1
        while curr != None :
            print (curr.val,end = ' ')
            curr = curr.next


# Recurssive approach to merge to list (Zipper lists)
def zipper_list_recur (head1 , head2) :
    ans = recurssive_function (head1 , head2)
    if ans:
        curr = ans
        while (curr != None) :
            print(curr.val,end=" ")
            curr = curr.next
def recurssive_function (head1 , head2) :
    if (head1 == None and head2 == None) : return None
    if (head1 == None) : return head2
    if (head2 == None) : return head1

    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = recurssive_function (next1 , next2)

    return head1



link_list1 = linkedlist ()          # Initilizing linked list - 1
link_list2 = linkedlist ()          # Initilizing linked list - 2

link_list1.head = Node ('A')        # Declaring linked list - 1 head as 'A'
b = Node ('B')                      # Creating another node 'B'
c = Node ('C')                      # creating one more node 'C'
d = Node ('D')                      # creating another node 'D'

link_list1.head.next = b            # Defining link between nodes 'A' & 'B'
b.next = c                          # Linking nodes 'B' and 'C'
c.next = d                          # Linking nodes 'C' and 'D'

link_list2.head = Node (1)
x = Node (2)
#y = Node (3)

link_list2.head.next = x
#x.next = y
# Remove '#' for x and y to see different results

zipper_list_loop (link_list1.head , link_list2.head)
zipper_list_recur (link_list1.head , link_list2.head)

# Comment either one of approach (loop or recurssive) if try to run both it will crash -> GG
