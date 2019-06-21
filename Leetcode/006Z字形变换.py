#方法一
'''
import numpy as np
n=0
i=0
a=list(input())
numRows=eval(input())
strlen=round(len(a)/2)+1
print(strlen)

b=[[0 for k in range(strlen)]for j in range(numRows)]
# b=np.zeros([numRows,strlen])
# print(np.reshape(b))
# print(a[len(a)-1])
while(i<len(a)):
    for m in range(numRows):
        if n>=strlen or i>=len(a):
            break
        b[m][n] = a[i]
        i = i+1
        if (m==numRows-1):
            while m!=0:
                m = m - 1
                n = n + 1
                if m==0 or i>=len(a):
                    break
                b[m][n]=a[i]
                i=i+1
A=[y for x in b for y in x]
B=(list(filter(lambda x:x!=0,A)))
print(''.join(B))
'''

#方法二
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:#只有一行的情况下直接返回
            return s

        rows = ['']* min(numRows, len(s))#定义了几个列表用来存放每行的非空值
        print(rows)
        print(type(rows))
        godown = False
        currow = 0
        for c in s:
            rows[currow] += c
            if currow == 0 or currow == numRows-1:
                godown = not godown
            if godown:
                currow += 1
            else:
                currow -= 1
        return ''.join(rows)
sol=Solution()
c='LEETCODEISHIRING'
print(sol.convert(c,4))








