# 47. Permutations II

# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# Example 1:
nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]

# Example 2:
# nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# def permutations(nums):
#   ans = 0
#   def factorial(l):
#     if l <= 1:
#       return l
#     return l * factorial(l-1) 

#   counter = 0
#   for i in range(len(nums)):
#     print(nums[i])
#     for j in range(i,len(nums)):
#       print(nums[i],nums[j])
#       if nums[i] == nums[j]:
#         counter += 1 
   
#   if counter - len(nums) == 0:
#     ans = factorial(len(nums))
#   else:
#     print(len(nums)-(counter - len(nums)))
#     ans = factorial(len(nums)-(counter - len(nums)))

#   return ans

def permutations(nums):
  res = []
  permutations = []
  d = {n:0 for n in nums}
  print(d)
  
  # count occurrences 
  for i in nums:
    d[i] += 1
  # print(d)

  def dfs():
    if len(permutations) == len(nums):
      res.append(permutations.copy())
    

    for n in d:
      print(d)

  dfs() 
    

  
  