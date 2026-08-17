class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        m=sorted(nums)
        for i in range(len(nums)):
            if i!=m[i]:
                return i   
        return len(nums)