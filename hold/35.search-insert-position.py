#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        
        if target > nums[mid]:
        
# @lc code=end
