#方法一
# class Solution:
#   def twoSum(self,nums,target):
#     a=[]
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 a.append([i,j])
#     return a
# A = list(map(int,input()))
# B= eval(input())
# sol=Solution()
# print(sol.twoSum(A,B))

#方法二
# class Solution:
#   def twoSum(self,nums,target):
#     a=[]
#     for i in range(0, len(nums)):
#         if target-nums[i] in nums:
#             a.append([i,nums.index(target-nums[i])])
#     if (len(a))%2==0:
#         c=int(len(a)/2)
#         # print(len(a))
#         return a[:c]
#     else:
#         c=int((len(a)+1)/2)
#         return a[:c]
# A = list(map(int,input()))
# B= eval(input())
# sol=Solution()
# print(sol.twoSum(A,B))

#方法三
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         d={}
#         size=0
#         while size < len(nums):
#             if target-nums[size] in d:
#                 if d[target-nums[size]] < size:
#                     return [d[target-nums[size]],size]
#             else:
#                 d[nums[size]] = size
#             size = size + 1
# A = list(map(int,input()))
# B= eval(input())
# sol=Solution()
# print(sol.twoSum(A,B))



