x = 0
y = 0
count = 0
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

while x != 9:
    y = 0
    print(grid[x][y], end='')
    while y != 6:
        y += 1
    x += 1

# b = 0
# while b <= 10:
#     x = 0
#     print(b)
#     while x <= 15:
#         print(x, end='')
#         x += 1
#     b += 1