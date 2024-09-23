# 题目要求： 在给定数组中找出sum==target的两个数

# 自己的思路： 排序，遍历第一个数，将target-nums[i]的值作为二分查找key

# 复杂度分析：排序nlogn+二分查找logn-> nlogn


class Solution(object):
    def partition(self, nums, pos, left, right):
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right -= 1
            pos[left], pos[right] = pos[right], pos[left]
            nums[left], nums[right] = nums[right], nums[left]
            while left < right and nums[left] <= pivot:
                left += 1
            pos[left], pos[right] = pos[right], pos[left]
            nums[left], nums[right] = nums[right], nums[left]
        nums[left] = pivot
        return left

    def quick_sort(self, nums, pos, left, right):

        if left < right:
            pivot = self.partition(nums, pos, left, right)
            self.quick_sort(nums, pos, left, pivot - 1)
            self.quick_sort(nums, pos, pivot + 1, right)
            return nums
        else:
            return nums

    # 二分搜索

    def binary_search(self, nums, target, left, right):
        if (target < nums[left] or target > nums[right]):
            return -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pos = list(range(len(nums)))
        self.quick_sort(nums, pos, 0, len(nums) - 1)

        for i in range(len(nums)):
            target_minus = target - nums[i]
            binary_result = self.binary_search(nums, target_minus, i + 1, len(nums) - 1)
            if binary_result != -1:
                return [pos[i], pos[binary_result]]


# 示例用法：
sol = Solution()
print(sol.twoSum([2,3,5,6], 9))  # 输出: [0, 1]


# 题解思路

# 利用hsahmap建立值和对象的映射，加快查找速度

class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm={}
        for i in range(0,len(nums)):
            hm[nums[i]]=i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hm and hm[complement] != i:
                return [i, hm[complement]]



