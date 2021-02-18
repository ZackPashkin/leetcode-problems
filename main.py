import os
import sys 
print("here is running from main.py!")
print(os.path.join(os.getcwd(),"leetcode"))
sys.path.append(os.path.join(os.getcwd(),"leetcode"))

from spiral_matrix import spiral_matrix
from permutations import permutations


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# print(spiral_matrix(matrix))

nums = [1,1,2]
print(permutations(nums))