class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = {}
        for num in s:
            counter[num] = counter.get(num, 0) + 1
        for num in t:
            counter[num] = counter.get(num, 0) - 1
        for value in counter.values():
            if value != 0:
                return False
        return True