class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #create hashmaps for both s1 and s2 if values from s1 do not match s2 then false, true otherwise
        len_1, len_2 = len(s1), len(s2)
        if len_1 > len_2:
            return False 

        s1_counts = [0] * 26
        window = [0] * 26

        for i in range(len_1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if s1_counts == window:
            return True

        for i in range(len_1, len_2):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - len_1]) - ord('a')] -= 1

            if s1_counts == window:
                return True
        
        return False 
        
        