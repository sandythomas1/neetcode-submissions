class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0

        for num in hash_set:
            if num - 1 not in hash_set:
                curr = num
                length = 1

                while curr + 1 in hash_set:
                    curr += 1
                    length += 1

                longest = max(longest, length)
        
        return longest

