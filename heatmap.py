import numpy as np

board_size = 5
match_size = 5

hits = np.zeros((board_size, board_size))

# X axis
for x in range(board_size):
    for sy in range(board_size - match_size + 1):
        for dy in range(match_size):
            hits[x][sy + dy] += 1

# Y axis
for y in range(board_size):
    for sx in range(board_size - match_size + 1):
        for dx in range(match_size):
            hits[sx + dx][y] += 1

# XY diag
for sx in range(board_size - match_size + 1):
    for sy in range(board_size - match_size + 1):
        for d in range(match_size):
            hits[sx + d][sy + d] += 1

# YX diag
for sx in range(board_size - match_size + 1):
    for sy in range(board_size - match_size + 1):
        for d in range(match_size):
            hits[sx + d][board_size - 1 - sy - d] += 1

# How many win scenarios each field contributes to
print(hits)
