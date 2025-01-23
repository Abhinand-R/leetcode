class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=0,len(height)-1
        water=0
        while i<j:
            width=j-i
            h=min(height[i],height[j])
            water=max(width*h,water)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return water


        