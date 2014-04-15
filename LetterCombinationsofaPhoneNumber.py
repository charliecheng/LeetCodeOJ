'''
http://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
class Solution:
    # @return a list of strings, [s1, s2]
    def __init__(self):
        self.dict={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}
    def letterCombinations(self, digits):
        digits=list(digits)
        if len(digits)==0:
            return ['']
        if len(digits)==1:
            return self.dict[digits[0]]
        templist=self.letterCombinations(digits[1:])
        lists=[]
        for i in self.dict[digits[0]]:
            for j in templist:
                lists.append(i+j)
        return lists
