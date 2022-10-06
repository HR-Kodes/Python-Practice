class Node :
    def __init__ (self , val = None , next = None) :
        self.val = val
        self.next = None

class linkedlist :
    def __init__ (self) :
        self.head = None

def sum_link_list_loop (head) :                         # Using loop to find sum of given linked list node values
    if head == None :
        print('Sum = 0 [ as there is no element in given linked list ] ')
        return
    sum = 0
    cur = head
    while cur != None :
        sum += cur.val
        cur = cur.next
    print ('Sum = ' , sum)


def sum_link_list_recur (head) :                        # Using recurssive way to find sum of given linked list values
    ans = recurssive_function (head)
    print('Sum = ' , ans)
def recurssive_function (head):
    if head == None : return 0
    return head.val + recurssive_function (head.next)

link_list1 = linkedlist ()
link_list2 = linkedlist ()

link_list1.head = Node (10)
b = Node (20)
c = Node (2)
d = Node (3)

link_list1.head.next = b
b.next = c
c.next = d

print ('Finding sum of values in node of linked list using recurssive approach')

sum_link_list_loop (link_list1.head)
sum_link_list_loop (link_list2.head)

print ('Finding sum of values in node of linked list using recurssive approach')

sum_link_list_recur (link_list1.head)
sum_link_list_recur (link_list2.head)
