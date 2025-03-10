# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r :
            mid  = (l+r)

            if target == nums[mid]:
                return mid
        
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1
        return l
        