class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position of the next non-zero element
        last_non_zero_found_at = 0

        # Move non-zero elements forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero_found_at] = nums[i]
                last_non_zero_found_at += 1

        # Fill the rest with zeroes
        for i in range(last_non_zero_found_at, len(nums)):
            nums[i] = 0
