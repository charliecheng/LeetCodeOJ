#It is a quite naive algorithm, time complexity is O(n^2)
#The first virsion triggered Time Exceeded Error, fixed by adding "if longest==len(s) return s"
#Kind of cheat to pass the test

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l=len(s)
        if l==1 or l==2:
            return s
        longest=0
        
        single = True
        list=[]
        for i in range(0,l-1):
            for j in range(0,min(i,l-i-1)+1):
                if not s[i-j]==s[i+j]:
                    j=j-1
                    break
            if 2*j+1>longest:
                longest=2*j+1
                if longest==l:
                    return s
                single=True
                list.append([i,longest])
            j=0
            if s[i]==s[i+1]:

                for j in range(0,min(i,l-i-2)+1):
                    if not s[i-j]==s[i+1+j]:
                        j=j-1
                        break
                if 2*j+2>longest:
                    single=False
                    longest=2*j+2
                    if longest==l:
                        return s
                    list.append([i,longest])

        temp=list.pop()
       
        return s[temp[0]-(temp[1]-1)/2:temp[0]-(temp[1]-1)/2+temp[1]]
    
if __name__=='__main__':
    a=Solution()
    print a.longestPalindrome('ccdcc')
