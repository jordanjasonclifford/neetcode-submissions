# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # -------------------------------
        # 1. SET UP DUMMY + TWO POINTERS
        # -------------------------------
        # dummy helps handle edge cases (like removing the head)
        # left will lag behind right by n nodes

        dummy = ListNode(0, head)
        left = dummy
        right = head


        # -------------------------------
        # 2. MOVE RIGHT POINTER n STEPS
        # -------------------------------
        # this creates a gap of n between left and right
        # so when right hits the end, left is right before the node to delete

        while n > 0 and right:
            right = right.next
            n -= 1


        # -------------------------------
        # 3. MOVE BOTH POINTERS TOGETHER
        # -------------------------------
        # move both until right reaches the end
        # left will stop right BEFORE the node we want to remove

        while right:
            left = left.next
            right = right.next


        # -------------------------------
        # 4. DELETE THE TARGET NODE
        # -------------------------------
        # left.next is the node we want to remove
        # so we "skip" it by pointing to the next node

        left.next = left.next.next

        # example:
        # left -> 1 -> 2 -> 3
        #            ^
        #         delete this (2)
        #
        # becomes:
        # left -> 1 ------> 3


        # -------------------------------
        # 5. RETURN RESULT
        # -------------------------------
        # return the real head (skip dummy)

        return dummy.next