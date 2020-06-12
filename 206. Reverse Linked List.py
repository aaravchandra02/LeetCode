"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. 
Could you implement both?
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class SingleLinkedList:
    def __init__(self):
        pass


class Solution:
    def reverse_SLL_iterative(self, lst):
        # to store previous node
        prev = None

        # to store current node
        head = lst

        # used as extra container
        tmp = None

        # Running till head is not None
        while(head):
            # Storing current node's next to tmp
            tmp = head.next
            # Assiging current node's next to previous node
            head.next = prev
            # Storing current node's address as previous node
            prev = head
            # Making the current node to point to next node in the linked list
            head = tmp
        # As now prev points to the reversed list, hence returning it.
        return prev

    def reverse_SLL_recursive(self, list):
        pass
