class Node :
    def __init__ (self , data = None , next = None) :
        self.data = data
        self.next = next

a = Node (1)
b = Node (2)
c = Node (3)
d = Node (4)
e = Node (5)
f = Node (6)
g = Node (7)
h = Node (8)
i = Node (9)
j = Node (10)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j
j.next = d

def print_linklist (head) :
    if head == None :
        return
    print(head.data)
    return print_linklist(head.next)

def reverse_linklist (head):
    if head == None : return
    reverse_linklist (head.next)
    print(head.data)

def insert_linklist (head , index ,value) :
    if index == 0 :
        print("inserting at begining")
        new = Node (value)
        new.next = head
        return new
    if head == None :
        new = Node (value)
        head = new
        return head

    curr = head
    count = 0
    while count != index :
        curr = curr.next
        count += 1
    temp = curr.next
    new = Node (value)
    curr.next = new
    new.next = temp
    return head

def searching (head , value) :
    result = recrssive_fun_searching (head , value)
    print(result)
def recrssive_fun_searching (head , value , index = 0) :
    if head == None : return
    if head.data == value : return index
    return recrssive_fun_searching (head.next , value , index+1)

def sorting_linklist (head) :
    if head == None :
        print ("Noting to sort")
        return
    curr1 = head
    while curr1 is not None :
        curr2 = curr1.next
        while curr2 is not None :
            if curr1.data > curr2.data :
                curr1.data , curr2.data = curr2.data , curr1.data
            curr2 = curr2.next
        curr1 = curr1.next

def find_mid(head):
	slow=head
	fast=head
	while fast and fast.next:
		slow=slow.next
		fast=fast.next.next
	print("the middle element is",slow.data)

def cycle(head):
	slow=head
	fast=head
	while slow and  fast and fast.next:
		slow=slow.next
		fast=fast.next.next
		if slow==fast:
			print("cycle",slow.data)
			return
	print("no cycle")
	return

# Floyd Algorithm


# print_linklist (a)
# print()
# reverse_linklist (a)
# print()

# ans = insert_linklist (a , 0 , 40)
# print_linklist (ans)

# searching(a , 'C')

# sorting_linklist (a)
# print_linklist (a)

# find_mid (a)

cycle (a)
