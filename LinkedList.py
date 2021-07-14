#creating The Node
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = None

#Creating the LinkedList
class LinkedList:
    def __init__(self):
        self.start_node = None
        
    #Insert at the Start
    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node
        
    #Insert at Last
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if self.start_node is None:
            self.start_node = new_node
        else:
            n = self.start_node
            while n.next is not None:
                n = n.next
            n.next = new_node
    
    #Insert After the element
    def insert_after_element(self,x,data):
        new_node = Node(data)
        
        if self.start_node is None:
            return
        else:
            n = self.start_node
            
            while n.next is not None:
                if n.data == x:
                    break
                n = n.next
            
            if n is None:
                print("Element Not Found")
            else:
                new_node.next = n.next
                n.next = new_node
    
    #Insert before the element
    def insert_before_element(self,x,data):
        new_node = Node(data)
        
        if self.start_node is None:
            return
        if self.start_node.data == x:
            new_node.next = self.start_node
            self.start_node = new_node
        else:
            n = self.start_node
            temp = n
            while n.next is not None:
                if n.next.data == x:
                    new_node.next = n.next
                    n.next = new_node
                    break
                n = n.next
    #Delete element
    def deleteElement(self,x):
        if self.start_node is None:
            return
        if self.start_node.data == x:
            self.start_node = self.start_node.next
        else:
            n = self.start_node
            while n.next is not None:
                prev = n                   
                    
                if n.next.data == x:
                    prev.next = n.next.next
                    break
                n = n.next
                    

    #Reverse a list                
    def reverse_list(self):
        
        if self.start_node is None:
            return
        else:
            n = self.start_node
            prev = None
            while n is not None:
                Next = n.next
                n.next = prev
                prev = n
                n = Next
            self.start_node = prev
    
    #Print a list
    def print_list(self):
        n = self.start_node
        
        while n is not None:
            print(n.data)
            n = n.next
            
        
        
ll = LinkedList()
ll.insert_at_start(3)
ll.insert_at_start(2)
ll.insert_at_start(1)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.insert_at_end(6)
ll.insert_at_end(7)
#ll.insert_after_element(15, 8)
#ll.insert_before_element(15, 25)
#ll.insert_before_element(30, 25)
ll.insert_before_element(1, 30)
ll.deleteElement(7)
ll.reverse_list()
ll.reverse_list()
ll.print_list()
        