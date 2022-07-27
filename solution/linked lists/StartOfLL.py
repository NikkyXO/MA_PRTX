#!/usr/bin/python3.8
"""
Problem Statement

Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
if there is no cycle , return null
Note: dont modify the linked list


Solution: 1) using two pointers  2)Brute force solution Using a hash table
"""


from tkinter.tix import ListNoteBook


class Solution:
    def StartNodeOfCylcleLL(self, head: ListNoteBook):
        slow, fast, entry = head, head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                while(entry != slow):
                    entry = entry.next
                    slow = slow.next
                return entry
        return None
