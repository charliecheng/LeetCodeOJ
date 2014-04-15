'''
http://oj.leetcode.com/problems/generate-parentheses/
Iteration again.
Bad Algorithm actually.
'''
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        if n==0:
            return []
        if n==1:
            return ['()']
        templist=self.generateParenthesis(n-1)
        lists=[]
        for str in templist:
            strlist=list(str)
            for i in xrange(len(strlist)):
                temp=strlist[:]
                temp.insert(i,'()')
                if not (''.join(temp) in lists):
                    lists.append(''.join(temp))
        return lists
