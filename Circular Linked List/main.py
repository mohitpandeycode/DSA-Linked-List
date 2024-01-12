# crating node.
class Node:
    def __init__(self,item = None, next = None):
        self.item = item
        self.next = next

# Creating Circular Linked List...
class CLL:
    def __init__(self,last = None):
        self.last = last
    
# check the list empty or not....
    def is_empty(self):
        return self.last is None

# Print the list...
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item,end = " -> ")
                temp = temp.next
            print(temp.item)

# insert element at first...
    def insert_at_first(self,data):
        n =  Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

# Inserting elemnt at last...
    def Insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

# serching the element...
    def search_item(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None

# inserting element after any element....
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data,temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n
                
# deleteing first element...
    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None

            else:
                self.last.next = self.last.next.next

# deleting element from last...
    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next is not self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

# delete a perticuler item...
    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None  
            else:
                temp = self.last.next
                if temp.item == data:
                    self.last.next = temp.next
                else:
                    temp = self.last.next
                    while temp is not self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                            break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

list = CLL()
list.insert_at_first(30)
list.insert_at_first(20)
list.insert_at_first(10)
# list.Insert_at_last(40)
# list.Insert_at_last(50)
# list.insert_after(list.search_item(50),60)
# list.delete_first()
# list.delete_first()
# list.delete_last()
# list.delete_last()
# list.delete_last()
# list.delete_item(10)
# if list.search_item(30):
#     print("true")
# else: 
#     print("not")
list.print_list()