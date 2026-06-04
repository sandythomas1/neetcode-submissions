class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # start with an array of just 1's for the length of nums for placeholders
        # if any zero is in any number being multiplied return 0 automatically
        # keep in track of the current index value(if 0) as the value that is being tracked 
        arr = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            arr[i] = left
            left *= nums[i]

        right = 1
        for i in range(len(nums) -1, -1, -1):
            arr[i] *= right
            right *= nums[i]
        
        return arr
        