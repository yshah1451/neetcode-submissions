from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            char_dict_s = Counter(s)
            char_dict_t = Counter(t)
            if char_dict_s == char_dict_t:
                return True
            else:
                return False
