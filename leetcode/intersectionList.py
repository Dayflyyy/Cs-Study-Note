# 自己的思路超时了


# 题解思路：先遍历两个链表求长度差值，减去差值后同步移动比较指针是否相同


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        curA, curB = headA, headB

        while (curA != None):
            curA = curA.next
            lenA += 1
        while (curB != None):
            curB = curB.next
            lenB += 1

        curA, curB = headA, headB

        if (lenA > lenB):
            min = lenA - lenB
            while (min != 0):
                curA = curA.next
                min -= 1
        else:
            min = lenB - lenA
            while (min != 0):
                curB = curB.next
                min -= 1

        while (curA != None):
            if (curA == curB):
                return curA.val
            else:
                curA = curA.next
                curB = curB.next

        return None


# 评测系统 的输入如下（你设计的程序 不适用 此输入）：
#
# intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
# listA - 第一个链表
# listB - 第二个链表
# skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
# skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
# 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。
sol = Solution()
