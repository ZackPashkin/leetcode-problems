import os
import sys 
print("here is running from main.py!")
print(os.path.join(os.getcwd(),"leetcode"))
sys.path.append(os.path.join(os.getcwd(),"leetcode"))

from spiral_matrix import *
from permutations import *
from astreroid_collision import *
from good_pairs_arrays import *



# print(spiral_matrix(matrix))

# print(permutations(nums))


# print(asteroid_collision(a))


print(good_pairs(nums))