

# creating a grid using 2 demansional lists
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# accessing number 1 in first list
print(number_grid[0][0])

# nested for loop
# printing all of the elements of all of the array 2d way
for row in number_grid:
    for col in row:
        print(col)
