class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxpd=nums[0]
        curmax,curmin=1,1
        for i in nums:
            tmax=curmax*i
            curmax=max(tmax,curmin*i,i)
            curmin=min(tmax,curmin*i,i)
            maxpd=max(maxpd,curmax)
        return maxpd
