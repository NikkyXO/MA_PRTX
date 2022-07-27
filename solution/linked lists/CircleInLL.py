#!/usr/bin/python3.8
"""
Problem Statement # LINKED LIST CYCLE

Given the head of a Singly LinkedList, write a function to 
determine if the LinkedList has a cycle in it or not
Return true if there is a cycle in the list, otherwise return false
Time Complexity = O(n)
"""


from tkinter.tix import ListNoteBook


class Solution:
    def HasCycle(self, head: ListNoteBook) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
