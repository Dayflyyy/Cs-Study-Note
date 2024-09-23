# 思路：以nums创建hash，当hash不为空时，寻找当前k+1的值，找到了count++,更新k=k+1，弹出当前k，直到找不到，比较最大值和当前count，更大更新，

class Solution(object):
    def longestConsecutive(self, nums):
        hm = {i: i for i in nums}
        count = 1
        max = 0
        while (len(hm)):
            now = hm.popitem()
            k = now[0]
            while (k + 1 in hm):
                count += 1
                hm.pop(k+1)
                k += 1
            k = now[0]
            while (k - 1 in hm):
                count += 1
                hm.pop(k-1)
                k -= 1
            if count > max:
                max = count
            count = 1

        print(max)
        return max


sol = Solution()
sol.longestConsecutive([100, 4, 200, 1, 3, 2])
sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])

