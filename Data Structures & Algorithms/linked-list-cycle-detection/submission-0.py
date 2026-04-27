# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        # moves 1 step at a time

        fast = head
        # moves 2 steps at a time

        # loop while fast pointer can move
        while fast and fast.next:

            slow = slow.next
            # move slow by 1

            fast = fast.next.next
            # move fast by 2

            # if they ever meet, there's a cycle
            if slow == fast:
                return True

        # if fast reaches the end, no cycle
        return False