#creating a class for Node...
class Node():
    def __init__(self,prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

#creating a class for doubly circuler linked list....        
class DCLL():
    def __init__(self,start=None):
        self.start = start

# create a function for check the list is empty or not....
    def is_empty(self):
        return self.start is None

# print the list....    
    def print_list(self):
        temp = self.start
        if self.start is None:
            print(self.start)
        elif temp.next == temp:
            print(temp.item,end=" -> ")
        else:
            while temp.next is not self.start:
                print(temp.item,end=" -> ")
                temp = temp.next
            print(temp.item)

# inserting element at first...
    def insert_at_first(self,data):
        n = Node(None,data,None)
        if self.start is None:      
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n
            self.start = n

# inserting element at last....
    def inser_at_last(self,data):
        n = Node(None,data,None)
        if self.start is None:
            n.prev = n
            n.next = n
            self.start = n
        else:
            n.prev = self.start.prev
            n.next = self.start
            self.start.prev.next = n
            self.start.prev = n

# serch for a element in a list...
    def search_item(self,data):
        if self.start is not None:
            temp = self.start
            if temp.next == temp:
                if temp.item == data:
                    return temp
            else:
                while temp.next is not self.start:
                    if temp.item == data:
                        return  temp
                    temp = temp.next
                if temp.item == data:
                    return temp
                return None

# inserting element after an element... 
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            temp.next.prev = n
            temp.next = n


# delete element from first.... 
    def delete_first(self):
        if not self.is_empty():
            if self.start.next is self.start:
                self.start = None
            else:
                self.start.prev.next=self.start.next
                self.start.next.prev = self.start.prev
                self.start = self.start.next

# delete element from last..... 
    def delete_last(self):
        if not self.is_empty():
            if self.start.next is self.start:
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev 


# delete a specefic element..... 
    def delete_item(self,data):
        if not self.is_empty():
            if self.start.next is self.start:
                if self.start.item == data:
                    self.start = None
            else:
                if self.start.item == data:
                    self.start.prev.next=self.start.next
                    self.start.next.prev = self.start.prev
                    self.start = self.start.next
                else:
                    temp = self.start
                    while temp.next is not self.start:
                        if temp.item == data:
                            temp.next.prev = temp.prev
                            temp.prev.next = temp.next
                            break
                        temp = temp.next
                    if temp.item == data:
                        temp.next.prev = temp.prev
                        temp.prev.next = temp.next
                        
# making a itrator function for print all elements by using for loop also....
    def __iter__(self):
        return CDLLItrator(self.start)

# making the itartor class....
class CDLLItrator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current is None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
            data = self.current.item
            self.current = self.current.next
            return data


list = DCLL()
list.insert_at_first(30)
list.insert_at_first(20)
list.insert_at_first(10)
list.inser_at_last(40)
list.inser_at_last(50)
list.inser_at_last(60)
list.print_list()
list.insert_after(list.search_item(10),15)

# list.delete_item(60)

list.print_list()

for i in list:
    print(i,end=' -> ')