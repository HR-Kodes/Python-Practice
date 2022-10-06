class Node :
    def __init__ (self , val = None , next = None) :
        self.val = val
        self.next = None

class linkedlist :
    def __init__ (self) :
        self.head = None

# Looping way of finding value at given index

def val_at_index_loop (index , head) :
    if (head == None) : print("Head of given linked list is empty")
    curr = head
    count = 0
    while (curr != None) :
        if (count == index) :
            print(curr.val)
            exit()
        count += 1
        curr = curr.next
    print('Index out of range')



# Recurssive approach

def val_at_index_recur (index , head) :
    ans = recurrsive_function (index , head)
    if ans : print(ans)
    else : print("NOT FOUND")
def recurrsive_function (index , head) :
    if (head == None) : return None
    if (index == 0) : return head.val
    return recurrsive_function (index-1 , head.next)


link_list = linkedlist ()
link_list.head = Node ('A')
b = Node ('B')
c = Node ('C')
d = Node ('D')


link_list.head.next = b
b.next = c
c.next = d

val_at_index_recur (3 , link_list.head)
val_at_index_loop (3 , link_list.head)
