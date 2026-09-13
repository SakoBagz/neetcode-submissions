class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = []
        x = False
        for i in nums: 
            if i in temp:
                x = True
            temp.append(i)
        return x

         