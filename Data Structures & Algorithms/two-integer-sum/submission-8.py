class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        maap = {}

        for i, num in enumerate(nums):
            diff = target - nums[i]
            if diff in maap:
                return [maap[diff], i]
            else:
                maap[num] = i
        