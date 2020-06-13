"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class SinglyLinkedList:

    def create_SLL(self, li):
        # Making the first node with the first element of the list.
        head = LinkedNode(li[0])
        """As the head will finally point to the last node, 
        hence its used to point at the starting of the linked list."""
        prev = head
        # Continuing it till the list ends.
        for i in range(1, len(li)):
            head.next = LinkedNode(li[i])
            head = head.next
        # Adding 'None' to the end of the list.
        head.next = None
        # Returning the first element of the list.
        return prev

    def reverse_it(self, l):
        prev = None
        head = l
        while(head):
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev

    def to_nums(self, l):
        # Changing it to string.
        s = ""
        while(l):
            s += str(l.val)
            l = l.next
        # Converting the string to integer.
        s = int(s)
        return s

    def add_them(self, l1, l2):
        # First reverse each SLL
        li1 = self.reverse_it(l1)
        li2 = self.reverse_it(l2)

        # Convert to nums
        li1 = self.to_nums(li1)
        li2 = self.to_nums(li2)

        ans = list(map(int, str(li1+li2)))
        return self.reverse_it(self.create_SLL(ans))

    def print_SLL(self, l):
        s = ""
        while(l):
            s += str(l.val)+" -> "
            l = l.next
        s = s[:-4]
        print(f"\n{s}\n")


a = SinglyLinkedList()
l1 = a.create_SLL([2, 4, 3])
l2 = a.create_SLL([5, 6, 4])
answer = a.add_them(l1, l2)
a.print_SLL(answer)
