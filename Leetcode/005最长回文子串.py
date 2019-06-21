#方法一
'''
class Solution:
    def longestPalindrome(self, s: str):
        """
        :param s:
        :return:
        """
        n = len(s)
        for i in range(n):
            start = 0
            end = n - i
            while end <= n:
                sub_string = s[start:end]
                if self.is_palindromic_string(sub_string):
                    return sub_string
                start += 1
                end += 1
    def is_palindromic_string(self, s):
        return s == s[::-1]
sol=Solution()
str2="abcddcba"
str1=sol.longestPalindrome(str2)
print(str1)
'''


#方法二
'''
首先枚举回文串的中心 i，然后分两种情况向两边扩展边界，直到遇到不同字符为止：

aba型：回文串长度是奇数，依次判断 s[i−k]==s[i+k]，k=0,1,2,3,…

abba型：回文串长度是偶数，依次判断 s[i−k]==s[i+k+1]，k=0,1,2,3,…'''

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :param s:
        :return:
        """
        n = len(s)
        count = 0  # 记录最大回文串的长度
        res = ''
        for i in range(n):
            # aba型 初始j,k都指向b,然后j往左扩展 k往右扩展
            j, k = i, i
            while (j >= 0 and k < n):
                if s[j] == s[k]:
                    if k - j + 1 > count:
                        count = k - j + 1
                        res = s[j:k + 1]
                    j -= 1
                    k += 1
                else:
                    break
            # abba型 初始j指向第一个b,k指向第二个b, 然后j往左扩展 k往右扩展
            j, k = i, i + 1
            while (j >= 0 and k < n):
                if s[j] == s[k]:
                    if k - j + 1 > count:
                        count = k - j + 1
                        res = s[j:k + 1]
                    j -= 1
                    k += 1
                else:
                    break
        return res

    # def is_palindromic_string(self, s):
    #     return s == s[::-1]
sol=Solution()
str2="aabcb"
str1=sol.longestPalindrome(str2)
print(str1)
'''
