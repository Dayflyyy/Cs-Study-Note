# 思路： 该数字的最大和 = 他的左最大和 or 0 + 它本身 + 它的右最大和 or 0

# 问题：原本的递归解法，看似用了分治法，实际每次+1，是一种遍历，在完成了栈空间的要求上同时时间复杂度和遍历相同


############################# 仔细思考如何分治，分治法是怎么运行的 ##############################
# 题解分治法
class Solution(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self._maxSubArray(nums)

    def _maxSubArray(self, nums):
        if (len(nums) == 1):
            return nums[0]
        if (len(nums) == 0):
            return float("-inf")
        mid = len(nums) >> 1
        return max(self.across(nums,mid),self._maxSubArray(nums[:mid]),self._maxSubArray(nums[mid+1:]))

    def across(self, nums, mid):
        leftmax = rightmax = 0
        left = right = 0
        leftp=mid
        while(leftp):
            left += nums[leftp-1]
            if left > leftmax: leftmax = left
            leftp-=1
        for i in nums[mid+1:]:
            right += i
            if right > rightmax: rightmax = right
        return nums[mid] + leftmax + rightmax


sol = Solution()
print(sol.maxSubArray([-2, 1, -1]))
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sol.maxSubArray([-2, -1]))
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5,4,-1,7,8]))
