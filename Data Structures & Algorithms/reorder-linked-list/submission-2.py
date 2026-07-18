# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # -------------------------------
        # 1. FIND THE MIDDLE OF THE LIST
        # -------------------------------
        # use slow/fast pointers
        # slow moves 1 step, fast moves 2 steps
        # when fast reaches the end, slow is at the middle

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # -------------------------------
        # 2. SPLIT + REVERSE SECOND HALF
        # -------------------------------
        # split the list into two parts:
        # first half: head -> ... -> slow
        # second half: slow.next -> end

        second = slow.next
        slow.next = None   # break the list into two halves

        prev = None

        # reverse the second half
        # standard reverse linked list pattern
        while second:
            tmp = second.next       # store next node
            second.next = prev      # reverse pointer
            prev = second           # move prev forward
            second = tmp            # move forward

        # after this:
        # prev = head of reversed second half


        # -------------------------------
        # 3. MERGE BOTH HALVES
        # -------------------------------
        # now we merge like:
        # first -> second -> first -> second...
        # alternating nodes

        first = head
        second = prev   # reversed second half

        while second:
            tmp1 = first.next
            tmp2 = second.next
            # store next pointers before changing links

            first.next = second
            # link node from first half to second half

            second.next = tmp1
            # link back to first half

            first = tmp1
            second = tmp2
            # move both pointers forward


        # no return because problem says modify in-place