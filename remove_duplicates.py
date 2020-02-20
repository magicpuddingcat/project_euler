"""Remove duplicates from sorted list in-place and return the final length. Needs some serious optimization, as the
runtime is currently at 80ms and could be slower. Space efficiency of O(1) and time efficiency of O(n). Danielle, February 2020."""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        previous = 0
        current = 1

        while current < len(nums):
            if nums[previous] == nums[current]:
                nums.pop(current)
            else:
                current += 1
                previous += 1

        return len(nums)