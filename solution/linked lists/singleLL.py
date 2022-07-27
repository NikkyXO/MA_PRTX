#!/usr/bin/python3.8

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def PrintList(self):
        if self.head is None:
            print("List is Empty")
        else:
            n = self.head
            while n is not None:
                print("n.data -->", end="")
                n = n.next

    def Add_beginning(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node = self.head
        self.head = new_node

    def Add_ending(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n = n.next
            n.next = new_node

    def insert_middle(self, data, index):
        if self.head is None:
            print("Linked list is empty")
            return
        if self.head == index:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        n = self.head
        while n is not None:
            if n.data == index:
                break
            n = n.next
        if n.next is None:
            print("Node Doesnt exist in LL")
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def delete_Begin(self):
        if self.head is None:
            print("LL is empty so we cant delete Nodes")
        else:
            self.head = self.head.next

    def delete_End(self):
        if self.head is None:
            print("LL is empty so we cant delete Nodes")
        elif self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n is not None:
                n = n.next
            n.next = None

    def delete_By_index(self, index):
        if self.head is None:
            print("LL is empty so we cant delete Nodes")
            return
        if self.head.data == index:
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if n.next.data == index:
                break
            n = n.next

        if n.next is None:
            print("Node is not present")
        else:
            n.next = n.next.next
