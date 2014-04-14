class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        list=[]
        num.sort()
        i=0
        #print num
        for i in range(0,len(num)-2):
            if i>0 and num[i]==num[i-1]:
                continue
            j=i+1
            k=len(num)-1
            while j<k:
                if num[j]==num[j-1] and not j-1==i:
                    j=j+1
                    continue
                if num[i]+num[j]+num[k]>0:
                    k=k-1
                    continue
                elif num[i]+num[j]+num[k]<0:
                    j=j+1
                    continue
                else:
                    list.append([num[i],num[j],num[k]])
                    j=j+1
                    k=k-1
                    continue

        return list
