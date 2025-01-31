#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Printing Spiral Matrix 
def print_Spiral_matrix(arr, top, down, left, right):
 
    # base case
    if left > right:
        return
 
    # print top row
    for i in range(left, right + 1):
        print(arr[top][i], end=' ')
 
    top += 1
 
    if top > down:
        return
 
    # print right column
    for i in range(top, down + 1):
        print(arr[i][right], end=' ')
 
    right -= 1
 
    if left > right:
        return
 
    # print bottom row
    for i in range(right, left - 1, -1):
        print(arr[down][i], end=' ')
 
    down -=  1
 
    if top > down:
        return
 
    # print left column
    for i in range(down, top - 1, -1):
        print(arr[i][left], end=' ')
 
    left += 1
 
    print_Spiral_matrix(arr, top, down, left, right)
 

 
if __name__ == '__main__':
    arr = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    
    top = 0
    down = len(arr) - 1
    left = 0
    right = len(arr[0]) - 1
    
    print_Spiral_matrix(arr, top, down, left, right)

