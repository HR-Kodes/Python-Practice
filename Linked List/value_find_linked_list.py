class Node :
    def __init__ (self , val = None , next = None) :
        self.val = val
        self.next = next
class linkedlist :
    def __init__ (self) :
        self.head = None

def find_value_loop (target , head) :
    if head == None :
        print("Given linked list is empty so target can't be found")
        return
    if head.val == target :
        print ('Target Found')
        return
    cur = head
    while cur != None :
        if cur.val == target :
            print('Target Found')
            return
        cur = cur.next
    print('Target Not Found')


def find_value_recur (target , head) :
    ans = recurssive_function (target , head)
    if ans :
        print('Target Found')
    else :
        print ('Target Not found')
def recurssive_function (target , head) :
    if head == None :
        return False
    if head.val == target :
        return True
    return recurssive_function (target , head.next)


link_list1 = linkedlist ()
link_list2 = linkedlist ()

link_list1.head = Node (1)
b = Node (2)
c = Node (3)
d = Node (4)

link_list1.head.next = b
b.next = c
c.next = d

print("Finding given target inside a linked list in 'LOOPING APPROACH'")
find_value_loop (3 , link_list1.head)
find_value_loop (10 , link_list1.head)
find_value_loop (1 , link_list2.head)

print("Finding given target inside linked list using 'RECURSSIVE APPROACH'")
find_value_recur (3 , link_list1.head)
find_value_recur (10 , link_list1.head)
find_value_recur (1 , link_list2.head)
