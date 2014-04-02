class Solution:
    # @return an integer
    def reverse(self, x):
        flag = True
        if x<0:
            flag = False
            x=0-x
        y=0
        while not x==0:
            y=y*10+x%10
            x=x/10
        if flag:
            return y
        else:
            return 0-y
    
if __name__=='__main__':
    a=Solution()
    print a.reverse(12345678901234567890)
