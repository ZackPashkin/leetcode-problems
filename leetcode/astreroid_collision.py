# Asteroid Collision - Stack - Leetcode 735
# Example 1:

# a = [5,10,-5]
# Output: [5,10]
# Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
# Example 2:

a = [8,-8]
# Output: []
# Explanation: The 8 and -8 collide exploding each other.
# Example 3:

a = [10,2,-5]
# Output: [10]
# Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
# Example 4:

a = [-2,-1,1,2]
# Output: [-2,-1,1,2]
# Explanation: The -2 and -1 are moving left, while the 1 and 2 are moving right. Asteroids moving the same direction never meet, so no asteroids will meet each other.

# def asteroid_collision(asteroids):
#   stack = []

#   for i,_ in enumerate(asteroids):
#     for j in range(i,len(asteroids)):
#         stack.insert(0,asteroids[i])
#         # if asteroids[i] < 0 or asteroids[j] < 0:
#         #   if abs(asteroids[i]) >  abs(asteroids[j]):
#         #     if asteroids[i] - asteroids[j]  > 0:
#         #       stack.insert(asteroids[i])
#         #     elif asteroids[i] - asteroids[j]  == 0:
#         #       continue
#         #     else:
#         #       stack.insert(asteroids[j])
#   return stack


# second try
def asteroid_collision(a):
  
  stack = []

  for e in a:
    print(stack)
    while stack and e < 0 and stack[-1] > 0:
      diff = e + stack[-1] 
      print('diff',diff)
      if diff < 0:
        stack.pop()
      elif diff > 0:
        e = 0
      else:
        stack.pop()
        e = 0
    if e:
      
      stack.append(e)
      print("stack",stack)

  return stack

  
      
  print(stack)



