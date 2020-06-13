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


class SinglyLinkedList:

    def __init__(self, li):
        self.head = ListNode(li[0])
        prev = self.head
        for i in range(1, len(li)):
            prev.next = ListNode(li[i])
            prev = prev.next

    def reverse_SLL_iterative(self):
        # to store previous node
        prev = None
        # to store current node
        head = self.head
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

    def reverse_SLL_recursive(self, head, prev=None):
        if not head:
            return prev
        tmp = head.next
        head.next = prev
        prev = head

        return reverse_SLL_recursive(tmp, prev)


# Test Run
a = SinglyLinkedList([-1, 1, 2, 4, 10])
ans = a.reverse_SLL_iterative()

# Displaying the linked list as String.
s_ans = ""
while(ans):
    s_ans += str(ans.val) + " --> "
    ans = ans.next
s_ans += "None\n"
print(s_ans)
