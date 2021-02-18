import os
import sys 
print(os.path.join(os.getcwd(),"leetcode"))
sys.path.append(os.path.join(os.getcwd(),"leetcode"))

from spiral_matrix import spiral_matrix


matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiral_matrix(matrix))