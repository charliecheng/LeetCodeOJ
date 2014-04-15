'''
http://oj.leetcode.com/problems/valid-parentheses/
Using Iteration
Check if there is {}[]() in string, if true remove then check again. If false then return False
'''
class Solution:
    # @return a boolean
    def isValid(self, s):
        s=list(s)
        if s==[]:
            return True
        flag=False
        for i in xrange(len(s)-1):
            if s[i]=='{' and s[i+1]=='}' or s[i]=='[' and s[i+1]==']' or s[i]=='(' and s[i+1]==')':
                flag=True
                break
        if flag==False:
            return False
        else:
            s.pop(i)
            s.pop(i)
            return self.isValid(s)
