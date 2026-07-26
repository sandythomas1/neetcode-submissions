class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_set = set()
        l = 0
        max_count = 0

        for r in range(len(s)):
            while s[r] in sub_set:
                sub_set.remove(s[l])
                l += 1
            sub_set.add(s[r])

            max_count = max(max_count, r - l + 1)
            
        return max_count
        