#refactor the code by using list comprehension
nums = [1,2,3,4,5,6,7,8,9,10]
squares = []
for i in nums:
    squares.append(i * i)
squares = [i * i for i in nums]
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
