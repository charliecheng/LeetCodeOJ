'''
http://oj.leetcode.com/problems/swap-nodes-in-pairs/
add a pseudo head before head node to avoid special edge cases
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        prehead=ListNode(0)
        prehead.next=head
        node=prehead
        while node.next and node.next.next:
            node.next=self.swap(node.next,node.next.next)
            node=node.next.next
        return prehead.next
    def swap(self,node1,node2):
        node1.next=node2.next
        node2.next=node1
        return node2

if __name__=='__main__':
    a1=ListNode(1)
    a2=ListNode(2)
    a1.next=a2
    a=Solution()
    print a.swapPairs(a1).next.val
