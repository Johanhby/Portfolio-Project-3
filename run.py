import random

# Define game board.

column = []
row = []
for y in range(5):
    for x in range(5):
        row.append('O')
    column.append(row)

# Define amount of ships, grid parameters and list to contain ship placements.

grid_width = 5
grid_height = 5
num_ships = 4
ships = []

#