Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

-------------------Recursion--------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(l1, l2):
            if l1 is None:
                return l2
            elif l2 is None:
                return l1
            
            if l1.val >= l2.val:
                return ListNode(val=l2.val, next=helper(l1, l2.next))
            else:
                return ListNode(val=l1.val, next=helper(l1.next, l2))
            
        return helper(l1, l2)
            
