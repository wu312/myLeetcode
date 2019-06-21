#方法一
'''
from functools import reduce
import heapq
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        j = 0

        s = list(s)
        list1 = []
        for i in range(0,len(s)):
            str1 = ''
            #i = j
            if i==len(s)-1:
                if list1 == []:
                    list1.append(s[0])
                return list1
            if ( s[i] != s[i+1] ):
                while (s[i] != s[i+1]) and (s[i+1] not in str1):
                    str1 += s[i]
                    i += 1
                    j = i
                    if i>=(len(s)-1):
                        break
                if (s[i]!=s[i-1]) and (s[i] not in str1):
                    str1 += s[i]
            if str1 != '':
                list1.append(str1)


sol=Solution()
a='bbvsfbhgbbgvvvv'
# k=[]
c=sol.lengthOfLongestSubstring(a)
# print(c)
temp=''
for i in range(len(c)):
    if len(temp) < len(c[i]):
        temp = c[i]
print(temp)

# print(len(c[2]))
# print(c)
# print(len(list(c)))
#
# print(heapq.nlargest(1,c))
#
# print(type(c))
# k=[]

def sortlist(x,y):
    a=len(str(x))
    # print(a)
    # print(str(x))
    b=len(str(y))
    if b>a:
        temp=str(y)
    else:
        temp=str(x)
    return temp
d=reduce(sortlist,c)
print(d)
'''


#方法二  这段代码看起来真舒服
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = ''
        maxlen = 0
        for ch in s:
            if ch not in res:
                res += ch  #去遍历找出所有连续不同字符的字符串
            else:#当下一个字符出现再前一个res里面的时候，找到该字符在前一个res里面的索引位置和该索引位置之和的字符组成新的res再返回到上面的if去判断
                maxlen = max(maxlen, len(res))
                index = res.index(ch)
                res = res[index + 1:] + ch
        return max(maxlen, len(res))
sol=Solution()
a="bbccdvda"
n=sol.lengthOfLongestSubstring(a)
print(n)
'''


#方法三   滑动窗口

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0   #左移left位
        lookup = set()
        n = len(s)   #字符串长度
        max_len = 0   #符合条件的最大子字符串长度
        cur_len = 0   #当前符合条件的子字符串长度(不断变化)
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:    #在一开始都不符合条件，就需要把元素字符添加到lookup里面
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
            print(lookup)
        return max_len
sol=Solution()
a="abbccd"
n=sol.lengthOfLongestSubstring(a)
print(n)