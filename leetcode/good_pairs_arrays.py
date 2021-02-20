# 1512. Number of Good Pairs
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# Return the number of good pairs.
# Example 1:
nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# nums = [1,2,3]
# Output: 0
# first try

# def good_pairs(nums):
#   good = []
#   for i in range(len(nums)-1):
#     for j in range(i,len(nums)):
      
#       if i != j and nums[i] == nums[j]:
#         good.append((i,j))

#   return len(good)


def good_pairs(nums):
  good = 0
  for i in range(len(nums)-1):
    for j in range(i,len(nums)):
      
      if i != j and nums[i] == nums[j]:
        good +=1

  return good

# def good_pairs(nums):
#   l,r = 0, len(nums) - 1

#   while l < r:
#     good = 0
#     if nums[l] == nums[r]:
#       good += 1
#     if nums[l] != nums[r]:
#       l += 1

#     r -= 1

#   return good



  