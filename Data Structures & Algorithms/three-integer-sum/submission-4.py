class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TODO: Handle the base case. What is the minimum length nums needs to be?
        if len(nums) < 3:
            return []
            
        nums.sort()
        result = []
        
        # Iterate through the array. 'i' is the index of our fixed number.
        # We only need to go up to the 3rd to last element.
        for i in range(len(nums) - 2):
            
            # TODO: Check for duplicates of the fixed number. 
            # If 'i' is greater than 0 AND nums[i] is the same as the previous number, skip it.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # TODO: Initialize your two pointers.
            # 'left' starts immediately after the fixed number.
            # 'right' starts at the last index of the array.
            left, right = i + 1, len(nums) - 1
            
            # Use the pointers to find the remaining two numbers
            while left < right:
                
                # TODO: Calculate the sum of the three current numbers
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == 0:
                    # TODO: Found a valid triplet! Append it to your result list.
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # TODO: Move both pointers inward to keep looking for other combinations
                    left += 1
                    right -= 1
                    
                    # TODO: Skip duplicates for the 'left' pointer.
                    # While left < right AND the new left number is the same as the old left number, keep incrementing left.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
                    # (You can also do the same duplicate check for the right pointer here, 
                    # but just checking left is technically enough to prevent identical triplets since 'i' is fixed).

                elif current_sum < 0:
                    # TODO: The sum is too small. Move the pointer that will INCREASE the sum.
                    left += 1
                    
                else:
                    # TODO: The sum is too large. Move the pointer that will DECREASE the sum.
                    right -= 1
                    
        return result