class Node:
    # creating a Node
    def __init__(self,prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL: # making doubly linked list..
#creating start
    def __init__(self,start=None):
        self.start = start

#creating print linked list function..
    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp = temp.next

# checking if the linked list empty or not..
    def is_empty(self):
        return self.start is None

# A data inserting at first.....
    def insert_at_first(self,data):
        new_Node = Node(None,data,self.start)
        if not self.is_empty:
            self.start.prev= new_Node
        self.start = new_Node

# A data inserting at last...
    def insert_at_last(self,data):
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            new_Node = Node(temp,data)
            temp.next = new_Node
        else:
            new_Node = Node(None,data,self.start)
            self.start = new_Node

# Making search method...
    def search_item(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None

# Inserting data at last..
    def insert_after(self,temp,data):
        if temp is not None:
            new_Node = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = new_Node
            temp.next = new_Node

# deleting data from first....
    def delete_first(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            self.start = self.start.next

# deleting element from last...
    def delete_last(self):
        if self.start.next is None:
            self.start = None
        else:
            temp = self.start
            if temp.next is None:
                self.start = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None

# delete element after any element...
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next 

# print item by itrater...
    def __iter__(self):
        return DLLItrator(self.start)

class DLLItrator:
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

# Test the Code
list = DLL()
list.insert_at_first(20)
list.insert_at_first(15)
list.insert_at_last(155)
list.insert_at_last(255)
list.insert_after(list.search_item(50),800)
if list.search_item(255):
    print("serched")
else:
    print("not searched")
# list.delete_first()
list.delete_item(255)
# list.delete_last()
list.print_list()

