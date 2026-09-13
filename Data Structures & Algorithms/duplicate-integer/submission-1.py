class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = []
        for i in range(len(nums)):
            if nums[i] in checker:
                return True
            else:
                checker.append(nums[i])
        return False
