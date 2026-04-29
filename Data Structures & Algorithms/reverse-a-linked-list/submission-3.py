# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # def reverse(curr, prev):
        #     if curr is None:
        #         return prev

        #     else:
        #         next = curr.next
        #         curr.next = prev
        #         return reverse(next, curr)

        # return reverse(head, None)

        # prev will become the new head
        prev = None

        # start at the current head
        curr = head

        while curr:
            # store next node before breaking the link
            temp = curr.next

            # reverse the pointer
            curr.next = prev

            # move prev forward
            prev = curr

            # move curr forward
            curr = temp

        # prev is the new head of reversed list
        return prev