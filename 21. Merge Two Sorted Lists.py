"""
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution():
    def merge_two_sortedlists(self, l1, l2):
        # Created to point to a new list
        new_list = ListNode(-100)

        """Copy of the above list to point at the required beginning of the list, 
        If not present then only the last two items will be returned
        It should be done everytime."""
        head = new_list

        # This loop terminates if one of the list runs out of elements
        while(l1 and l2):
            if (l1.val <= l2.val):
                new_list.next = l1
                l1 = l1.next
            else:
                new_list.next = l2
                l2 = l2.next
            new_list = new_list.next
        if(l1):
            new_list.next = l1
        else:
            new_list.next = l2

        return (head.next)

    def create_linklist(self, li):
        head = ListNode(li[0])
        prev = head
        for i in range(1, len(li)):
            prev.next = ListNode(li[i])
            prev = prev.next
        return head


# Test Run
a = Solution()
list1 = a.create_linklist([-1, 1, 2, 4, 10])
list2 = a.create_linklist([1, 3, 4])
ans = a.merge_two_sortedlists(list1, list2)
print("done")

# Displaying the linked list as String.
s_ans = ""
while(ans):
    s_ans += str(ans.val) + " --> "
    ans = ans.next
s_ans += "None\n"
print(s_ans)
