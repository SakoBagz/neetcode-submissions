class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pairs = {}
        for num in nums:
            if num in pairs.keys():
                return True 
            pairs[num] = None
        return False 
            