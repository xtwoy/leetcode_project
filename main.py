from collections import defaultdict

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = max(res, self.findMaxAverage(nums[i+k]-nums[i],k))