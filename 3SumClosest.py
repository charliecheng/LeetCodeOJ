    def threeSumClosest(self, num, target):
        num.sort()
        sum=num[0]+num[1]+num[2]
        x_abs=abs(sum-target)
        i=0
        for i in range(0,len(num)-2):
            if i>0 and num[i]==num[i-1]:
                continue
            j=i+1
            k=len(num)-1
            while j<k:
                if num[j]==num[j-1] and not j-1==i:
                    j=j+1
                    continue
                temp_sum=num[i]+num[j]+num[k]
                if abs(temp_sum-target)<x_abs:
                    sum=temp_sum
                    x_abs=abs(temp_sum-target)
                if temp_sum==target:
                    return target
                if temp_sum>target:
                    k=k-1
                else:
                    j=j+1
        return sum
