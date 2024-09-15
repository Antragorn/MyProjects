import random

def initialize_grid(rows, cols):
    """Initializes a grid with random live or dead cells."""
    grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]
    return grid

def count_neighbors(grid, row, col):
    """Counts the number of live neighbors for a given cell."""
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i >= 0 and i < rows and j >= 0 and j < cols and (i != row or j != col):
                count += grid[i][j]
    return count

def update_grid(grid):
    """Updates the grid based on the rules of the Game of Life."""
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            neighbors = count_neighbors(grid, i, j)
            if grid[i][j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i][j] = 0
            elif grid[i][j] == 0 and neighbors == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = grid[i][j]
    return new_grid

def print_grid(grid):
    """Prints the grid in a readable format."""
    print(" " + "--"*len(grid[0]))
    for row in grid:
          line = "|"
          for cell in row:
              line += "██" if cell == 1 else "  "
          print(line + "|")
    print(" " + "--"*len(grid[0]))

def play_game_of_life(rows, cols, display):
    """Plays the Game of Life for a given number of generations."""
    generation = 1
    grid = initialize_grid(rows, cols)
    grid_history = []
    going = True
    while going:
        if display:
            print(f"Generation {generation}:")
            print_grid(grid)
        grid1 = update_grid(grid)
        if grid1 == grid:
            going = False
        else:
            if grid in grid_history:
                going = False
            else:
                grid_history.append(grid)
                grid = grid1
                generation += 1
    return generation

if __name__ == "__main__":
    rows = 15
    cols = 15
    display = False
    runs = 1000
    generations = []
    for _ in range(runs):
        generations.append(play_game_of_life(rows, cols, display))
    
    average = sum(generations)/len(generations)
    maximum = max(generations)
    minimum = min(generations)
    print("The maximum number of generations is", maximum)
    print("The minimum number of generations is", minimum)
    print("The average number of generations for {} runs on a {} by {} grid is {}".format(runs, rows, cols, average))
