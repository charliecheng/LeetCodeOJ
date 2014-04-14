'''
It is the area of the rectangle, not the trapezoid
'''
class Solution:
    # @return an integer
    def maxArea(self, height):
        right=len(height)-1
        left=0
        area=0
        while left<right:
            if height[left]==0:
                left=left+1
                continue
            if height[right]==0:
                right=right-1
                continue
            area=max(area,min(height[left],height[right])*(right-left))
            if height[left]<=height[right]:
                left=left+1
            else:
                right=right-1
        return area

if __name__=='__main__':
    a=Solution()
    print a.maxArea([1,1])
            
