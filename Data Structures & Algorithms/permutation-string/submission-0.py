class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freqs1 = [0] * 26
        freqs2 = [0] * 26

        for i in range(len(s1)):
            freqs1[ord(s1[i]) - ord('a')] += 1
            freqs2[ord(s2[i]) - ord('a')] += 1

        if freqs1 == freqs2:
            return True

        left = 0

        # Indented the logic below so it runs inside the sliding window loop
        for right in range(len(s1), len(s2)):
            freqs2[ord(s2[right]) - ord('a')] += 1

            if (right - left + 1) > len(s1):
                freqs2[ord(s2[left]) - ord('a')] -= 1
                left += 1
            
            # Directly compare arrays instead of using a broken 26-step loop
            if freqs1 == freqs2:
                return True
                
        return False
