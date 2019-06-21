# Definition for singly-linked list.
import math
import time


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        pre = head
        while head:
            count += 1
            head = head.next
        # for i in range(1,count+1):
        #     pre=pre.next
        i = 0
        while abs(i-(math.ceil((count-1)/2))):
            pre = pre.next
            i += 1
        return pre.val


if __name__ == '__main__':
    start=time.clock()
    # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l1.next.next.next=ListNode(7)
    l1.next.next.next.next= ListNode(8)
    # l1.next.next.next.next.next= ListNode(9)
    # 获取返回值的链表
    res = sol.middleNode(l1)
    # print(res)
    # 循环遍历出来
    print(res)
    end=time.clock()
    print('Running time: %s Seconds' % (end - start))









# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# import math
# class Solution:
#     def middleNode(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         # 首先要知道链表一共有多少个结点
#         count = 0
#         res = {}
#         while head != None:
#             count += 1
#             res[count] = head
#             head = head.next
#         #j = math.ceil(count/2)
#         #if count % 2 == 0:
#         #    return res[j+1]
#         #else:
#         #    return res[j]
#         j = math.ceil((count-1)/2) + 1
#         return res[j]
# if __name__ == '__main__':
#     start=time.clock()
#     # 创建对象Solution
#     sol = Solution()
#     # 定义l1链表
#     l1 = ListNode(2)
#     l1.next = ListNode(4)
#     l1.next.next = ListNode(3)
#     l1.next.next.next = ListNode(7)
#     l1.next.next.next.next = ListNode(8)
#     l1.next.next.next.next.next = ListNode(9)
#     # 获取返回值的链表
#     res = sol.middleNode(l1)
#     # print(res)
#     # 循环遍历出来
#
#     print(res.val)
#     end=time.clock()
#     print('Running time: %s Seconds' % (end - start))
