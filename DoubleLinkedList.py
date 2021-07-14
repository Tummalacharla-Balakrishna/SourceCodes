# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 13:37:17 2021

@author: balak
"""

#Creating a Node
class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = None
        self.prev = None

#Creating a Double Linked List 
class DoubleLinkedList:
    def __init__(self):
        self.start_node = None
        
    
    #Inserting a Node at start
    def insert_at_start(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
        else:
            self.start_node.prev = new_node
            new_node.next = self.start_node
            self.start_node = new_node
                
        
    #Inserting a Node at end    
    def insert_at_end(self,data):
        new_node = Node(data)
        
        if self.start_node is None:
            self.start_node = new_node
        else:
            n = self.start_node
            
            while n.next is not None:
                n = n.next
            new_node.prev = n
            n.next = new_node
             
    #Inserting a Node after an element
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
                new_node.prev = n
                n.next = new_node
                n.next.prev = new_node
    
    #Inserting an element before element
    def insert_before_element(self,x,data):
        new_node = Node(data)
        
        if self.start_node is None:
            return
        if self.start_node.data == x:
            new_node.next = self.start_node
            self.start_node.prev = new_node
            self.start_node = new_node
            return
        else:
            n = self.start_node
            temp = n
            while n.next is not None:
                
                if n.next.data == x:
                    new_node.next = n.next
                    n.next.prev = new_node
                    new_node.prev = n
                    n.next = new_node
                    
                    break
                n = n.next
    
    #Deleting an element
    def deleteElement(self,x):
        
        if self.start_node is None:
            return
        if self.start_node.data == x:
            self.start_node = self.start_node.next
            self.start_node.prev = None
        else:
            n = self.start_node
            
            while n.next is not None:
                
                if n.next.data == x:
                    n.next = n.next.next
                    if n.next is not None:
                        n.next.prev = n
                    break
                n= n.next
                
                    
    #Reversing a list                
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
    
    def print_list(self):
        n = self.start_node
        t = n
        while n is not None:
            print(n.data)
            t = n
            n = n.next
        #return
        #For iterating in revverse order
        while t is not None:
            print(t.data)
            t = t.prev
        
        
        
dl = DoubleLinkedList()
dl.insert_at_start(5)
dl.insert_at_start(6)
dl.insert_at_end(7)
dl.insert_at_end(8)
#dl.insert_after_element(6,10)
#dl.insert_after_element(8,10)
#dl.insert_before_element(5, 10)
dl.deleteElement(8)
dl.print_list()

        