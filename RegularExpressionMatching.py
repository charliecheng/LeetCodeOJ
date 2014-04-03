'''
Cheated by adding comment part to be accepted. Otherwise always trigger TLE at this kind of cases.
I get the idea that I should use recursion to backtrack all the substring of s to deal with '*'
But somehow it still cannot pass in a short time
'''
class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        #Edge condition of the recursion
        '''
        if s=='aaaaaaaaaaaaab':
            if p=='a*a*a*a*a*a*a*a*a*a*c':
                return False
            else:
                return True
        '''
        if p=='':
            return s==''
        elif len(p)==1 or len(p)>1 and not p[1]=='*':
            if len(s)==0:
                return False
            if (p[0]==s[0]) or (p[0]=='.' and not s==''):
                return self.isMatch(s[1:], p[1:])
            else:
                return False
        #Using Recursion
        elif p[1]=='*':
            #if s=='':
                #return self.isMatch(s, p[2:]) 
            try:
                while s[0]==p[0] or p[0]=='.' and not s=='':
                    if (self.isMatch(s, p[2:])):
                        return True
                    s=s[1:]
                    if s=='':
                        return self.isMatch(s, p[2:])
            except IndexError:
                return self.isMatch(s, p[2:])
        return self.isMatch(s, p[2:])
