#The first time that my code is accepted in my first try
#Yeah!

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        list=[]
        flag=0
        while not (l1==None and l2==None and flag==0):
            sumnode,flag=self.addTwoListNode(l1, l2, flag)
            list.append(sumnode)
            if not l1==None:
                l1=l1.next
            if not l2==None:
                l2=l2.next
        for i in range(0,len(list)):
            if i==len(list)-1:
                break
            list[i].next=list[i+1]
        return list[0]
    def addTwoListNode(self,l1,l2,flag):
        answer = ListNode(0)
        answer.next = None
        returnflag = 0
        val1=0
        val2=0
        if l1==None:
            val1=0
        else:
            val1=l1.val
        if l2==None:
            val2=0
        else:
            val2=l2.val
        sum=val1+val2+flag
        if sum>=10:
            answer.val=sum-10
            returnflag=1
        else:
            answer.val=sum
        
        return answer,returnflag
    
if __name__ == '__main__':
    a=ListNode(9)
    #b=ListNode(9)
    b=None
    #a.next=b
    c=ListNode(1)
    s=Solution()
    list=s.addTwoNumbers(b,c)
    print list.val
