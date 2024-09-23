# 题目要求：给定一个数组，把数组中的零全部移到最后

# 自己的思路：结合题目设定 利用双指针双向遍历数组

# 边界条件考虑:
    # 开始写的是不等于，结果发现在移动过程中会出现p1移动到p2后的情况，所以改成了小于，
    # 一个易错点应该是在使用我的方法时，如果p1指针移动了零，会使得p2在数值不变的情况下指向的值后移一位，所以当p1移动时应该一起移动p2

# 复杂度分析：时间复杂度N，空间复杂度0
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        # sol1 似乎更快一些
        p, q = 0, (len(nums)-1)
        while (p <= q):
            if(nums[p]==0):
                nums.pop(p)
                nums.append(0)
                q-=1
            else:
                p+=1
            if(nums[q]==0):
                nums.pop(q)
                nums.append(0)
                q-=1
            else:
                q-=1

        print(nums)

        # sol2
        p,q=0,0
        while(q!=len(nums)):
            if(nums[q]!=0):
                nums[p],nums[q]=nums[q],nums[p]
                p+=1
                q+=1
            else:
                q+=1
        print(nums)

sol=Solution()
sol.moveZeroes([0,1,0,3,12])
sol.moveZeroes([0])
sol.moveZeroes([1])
sol.moveZeroes([0,0,1])


# leetcode官方题解思路

# 双指针，左指针指向已经处理好的序列的尾部，右指针指向待处理序列的头部，可以理解为分治法，当前为零不动，右指针右移，不为零左右指针交换，两个指针均右移

# python list function
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
