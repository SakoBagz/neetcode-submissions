class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

   
        x = True

        for letter in t:
            if t.count(letter) != s.count(letter):
                x = False
        
        return x

