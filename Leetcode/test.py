# a = ['a','b']
# s = ''
# k=[]
# s = a[0]+a[1]
# k.append(s)
# print(s)
# print(k)
# print(type(k))i
import heapq
nums=[1,2,3,4,5,7,11,-89,-9,0]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))
