#Spiral Matrix Leetcode 54 mid
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]


def spiral_matrix(matrix):
  l,r = 0 , len(matrix[0])
  top, bottom = 0,0
  while l < r:
    print(matrix[0][0])
    print(matrix[top][l])
    
    # print(matrix[bottom][r])
    if top < len(matrix) and bottom < len(matrix):
      l += 1
      r -= 1
      top += 1
      bottom += 1




print(spiral_matrix(matrix))
