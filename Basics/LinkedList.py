# LinkedList do not have indexes like List instead each node points to the next and last one points to none, 
# the first node has Head pointer and last node has Tail pointed.

# Demo Linked List Implementation
class Node:
    #constructor/initializer for Node class
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    #constructor/initializer for LinkedList Class
    def __init__(self,data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.length = 1

# print LinkedList
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

# append to LinkedList
    def append(self,data):
        new_node= Node(data)
        if self.length ==0:
            self.head =  new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

# pop from LinkedList
    def pop(self, data):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail =None
        return temp        
    
# prepend to LinkedList
    def prepend(self,data):
        new_node = Node(data)
        if self.length ==0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


# pop first from LinkedList
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head =self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp    

# get value at index
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp 

# set value at index
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False   
    
# insert value at index
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index ==0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        return temp

# remove value at index
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index ==0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
        pre = self.get(index -1 )
        temp = pre.next
        temp.next = None
        pre.next = temp.next
        self.length -=1
        return temp

  # reverse the LinkedList
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return temp    


# Test the LinkedList implementation
my_linked_list = LinkedList(11)
my_linked_list.append(3)
#my_linked_list.append(23)
my_linked_list.prepend(7)
my_linked_list.insert(2,99)
#my_linked_list.remove(3)
my_linked_list.reverse()

my_linked_list.print_list()
