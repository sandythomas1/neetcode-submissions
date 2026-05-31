class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in hash_map:
                index = hash_map[diff]
                return [index, i]
            hash_map[num] = i
        