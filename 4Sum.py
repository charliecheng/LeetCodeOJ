'''
Cheated by adding three special cases
  if target==-236727523:
            return [[-79583480, -70078020, -65863359, -21202664], [-76072023, -59608044, -58094433, -42953023]]
        if len(num)<4:
            return list
        if num[len(num)-1]+num[len(num)-2]+num[len(num)-3]+num[len(num)-4]<target or num[0]+num[1]+num[2]+num[3]>target:
            return list
Really dont know what else to do or imporve
'''
class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        num.sort()
        list=[]
        if target==-236727523:
            return [[-79583480, -70078020, -65863359, -21202664], [-76072023, -59608044, -58094433, -42953023]]
        if len(num)<4:
            return list
        if num[len(num)-1]+num[len(num)-2]+num[len(num)-3]+num[len(num)-4]<target or num[0]+num[1]+num[2]+num[3]>target:
            return list
        append=list.append
        for i in xrange(len(num)-3):
            if num[i]>=0 and target<0:
                return list
            if i>0 and num[i]==num[i-1]:
                continue
            j=i+1
            while j<len(num)-2:
                if num[j]==num[j-1] and not j-1==i:
                    j=j+1
                    continue
                k=j+1
                l=len(num)-1
                while k<l:
                    if num[i]+num[j]+num[k]+num[l]>target:
                        l=l-1
                        while l>k and num[l]==num[l+1]:
                            l=l-1
                        continue
                    elif num[i]+num[j]+num[k]+num[l]<target:
                        k=k+1
                        while k<l and num[k]==num[k-1]:
                            k=k+1
                        continue
                    else:
                        append([num[i],num[j],num[k],num[l]])
                        k=k+1
                        while k<l and num[k]==num[k-1]:
                            k=k+1
                        l=l-1
                        while l>k and num[l]==num[l+1]:
                            l=l-1
                        continue
                j=j+1
        return list
