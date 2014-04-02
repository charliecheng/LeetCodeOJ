class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        xb=x
        if x==0:
            return True
        if x<0:
            return False
        if x%10==0:
            return False
        a=0
        while not x==0:
            a=a*10+x%10
            x=x/10
        if a==xb:
            return True
        else:
            return False
        
if __name__=='__main__':
    a=Solution()
    print a.isPalindrome(10301)
