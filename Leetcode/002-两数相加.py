#方法一
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:  # 定义两个链表中的对应结点相加
#         root = ListNode(0)  # 新链表结点进行结果存储
#         new = root
#         carry = 0  # 十进制计算，进位值，初始化为0
#         while l1 or l2:  # 进行计算的两个结点非空
#             v1 = v2 = 0  # 定义v1、v2变量，同时使某一个链表结束后依然可以进行加和操作
#             if l1:  # 遍历链表直至尾结点
#                 v1 = l1.val  # 将l1结点的值赋给v1进行计算
#                 l1 = l1.next  # 指向下一个结点
#             if l2:
#                 v2 = l2.val
#                 l2 = l2.next
#             sum = v1 +v2 + carry  # 两个链表对应值相加
#             carry = sum // 10  # 和值求除取整做下次进位值
#             sum = sum % 10  # 和值求除取余为新链表的结点值
#             new.next = ListNode(sum)
#             new = new.next  # 指向下一个新链表下一个结点
#         if carry:  # 原始两个链表全部遍历后，若最后一次加和有进位1，则需要在新链表中加入一个结点存储该进位值
#             new.next = ListNode(1)
#         return root.next



#方法二
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmp = ListNode(0)
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val
                l2 = l2.next
            tmpres = ((tmpsum + flag) % 10)
            flag = ((tmpsum + flag) // 10)
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        del tmp
        return res
if __name__ == '__main__':
    # 创建对象Solution
    sol = Solution()
    # 定义l1链表
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    # 定义l2链表
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    # 获取返回值的链表
    res = sol.addTwoNumbers(l1, l2)
    # print(res)
    # 循环遍历出来
    while res:
        print(res.val)
        res = res.next



#方法三
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         # 这里一开始不做l1、l2非空判断，题意表明非空链表
#         # 记录是否需要增加新节点，或在链表下一个节点是否需要加1，同时记录链表同级节点的和
#         carry = 0
#         # 这里的执行顺序是res = ListNode(0), pre = res
#         res = pre = ListNode(0)
#         # 判断l1、l2、carry是否有值，carry有值的话需要增加新节点，或在链表下一个节点需要加1
#         while l1 or l2 or carry:
#             # 判断l1是否有值
#             if l1:
#                 carry += l1.val
#                 l1 = l1.next
#             # 判断l2是否有值
#             if l2:
#                 carry += l2.val
#                 l2 = l2.next
#             # carry有同级节点的和
#             # divmod返回商与余数的元组，拆包为carry和val
#             # carry有值的话需要增加新节点，或在链表下一个节点需要加1,在循环中会用到
#             carry, val = divmod(carry, 10)
#             # 新建链表节点
#             # 这里是n.next = ListNode(val), n = n.next()
#             pre .next = pre  = ListNode(val)
#         # res等价于pre，res.val=0，所以返回res.next
#         return res.next
#
#
# if __name__ == '__main__':
#     # 创建对象Solution
#     sol = Solution()
#     # 定义l1链表
#     l1 = ListNode(2)
#     l1.next = l11 = ListNode(4)
#     l11.next = l12 = ListNode(5)
#     # 定义l2链表
#     l2 = ListNode(5)
#     l2.next = l21 = ListNode(6)
#     l21.next = l22 = ListNode(4)
#     # 获取返回值的链表
#     res = sol.addTwoNumbers(l1, l2)
#     # 循环遍历出来
#     while res:
#         print(res.val)
#         res = res.next