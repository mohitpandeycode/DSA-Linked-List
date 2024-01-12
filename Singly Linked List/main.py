#creating Node class for node
class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

#creating singly linked list..  
class SLL:
    def __init__(self,start=None):
        self.start = start

# checking the linked list empty or not...
    def is_empty(self):
        return self.start == None
    
# for inserting a element in the first position of the linked list 
    def insert_at_start(self,data):
        new_Node = Node(data,self.start) # creating new node with data value and in next section we put self.start
        self.start = new_Node  # and then self.start = n

 # for inserting a element in the last position of the linked list   
    def insert_at_last(self,data):
       new_Node = Node(data)
       if not self.is_empty():
           temp = self.start
           while temp.next is not None:
               temp = temp.next
           temp.next = new_Node
       else:
           self.start=new_Node

# search function
    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
# inesert_after elment 
    def insert_after(self,temp,data):
        if temp is not None:
            new_Node = Node(data,temp.next)
            temp.next = new_Node

#print linked list
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next

# delete item from first
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next

# delete item from last
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None

#delete item from any place
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is None:
            if self.start.item == data:
                 self.start = None
        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

# adding the itretor class to the linked list..                 
    def __iter__(self):
        return SLLItretor(self.start)
    
# making our Sll class itrable..
class SLLItretor: 
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

            

#performing operations in linked list
my_list = SLL()
my_list.insert_at_start(20)
my_list.insert_at_start(10)
my_list.insert_at_last(30)
my_list.insert_after(my_list.search(20),25)
my_list.delete_item(30)
my_list.print_list()
