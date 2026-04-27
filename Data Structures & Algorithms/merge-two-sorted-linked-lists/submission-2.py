# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        node = ListNode()
        # this will move forward as we build the merged list

        dummy = node 
        # keep a reference to the start so we can return it later

        # edge cases: if one list is empty, return the other
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # loop while both lists still have nodes
        while list1 and list2:

            # take the smaller value node
            if list1.val < list2.val:
                node.next = list1
                # attach list1 node
                list1 = list1.next
                # move list1 forward
            else:
                node.next = list2
                # attach list2 node
                list2 = list2.next
                # move list2 forward

            node = node.next
            # move result pointer forward

        # one of the lists is now empty
        # attach the remaining nodes from the other list
        if list1:
            node.next = list1

        elif list2:
            node.next = list2

        # return merged list (skip dummy node)
        return dummy.next