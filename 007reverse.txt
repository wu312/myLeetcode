#方法一
'''
class Solutio:
    def reverse(self,x:int) ->int:
        if -2**31 <= x <0:
            x=str(x)[1:]
            x=x[::-1].lstrip('0')
            if int(x) > 2**31:
                return 0
            else:
                return int('-'+x)
        elif x==0:
            return 0
        elif x<2**31:
            x=str(x)[::-1].lstrip('0')
            if int(x) >=2**31:
                return 0
            else:
                return int(x)
sol=Solutio()
print(sol.reverse(-1230))
'''

#方法二
class Solution(object):
    def reverse(self, x):
        maxi=2147483647
        mini=-2147483648
        res=0
        judge=True
        if x<0:
            x=-x
            judge=False
        while x!=0:
            res=res*10+x%10
            x=int(x/10)
        if judge==False: res=-res
        if res>maxi or res<mini : return 0
        else : return res



