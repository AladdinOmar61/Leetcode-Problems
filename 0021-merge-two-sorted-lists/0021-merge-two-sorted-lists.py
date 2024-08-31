# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # making a new linked list first
        sorted_list = ListNode(0)
        ## line 11 adds the whole list FROM THE BEGINNING back over to this variable
        merged = sorted_list
        # make two pointers, one starting at the head of each linked list
        current_1 = list1
        current_2 = list2

        # we will compare the values, and add the smaller one to the new list
        while current_1 is not None or current_2 is not None:
            if current_1 is not None and current_2 is not None:
                if current_1.val <= current_2.val:
                    sorted_list.next = ListNode(current_1.val)
                    current_1 = current_1.next
                else:
                    sorted_list.next = ListNode(current_2.val)
                    current_2 = current_2.next
            elif current_1:
                sorted_list.next = ListNode(current_1.val)
                current_1 = current_1.next
            elif current_2:
                sorted_list.next = ListNode(current_2.val)
                current_2 = current_2.next
            sorted_list = sorted_list.next
        ## since the merged list started at 0, we call next to ignore that initial 0 fromm the list
        return merged.next
        # keep checking until end of both lists, return new head

        # edgecases
        # 1) both lens are none (return None)
        # 2) one ll longer than another (make a check for seeing if the pointer is at the last node)

        ## = extra notes taken post-attempt