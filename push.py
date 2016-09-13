import copy
import util

def flip_up(grid):
    newGrid = copy.deepcopy(grid)
    for y in range(4):
        for x in range(4):
            grid[x][y] = newGrid[y][x]
           
    return grid

def flip_up2(grid):
    newGrid = copy.deepcopy(grid) 
    for x in range(4):
        grid[x] = newGrid[3-x]
    
    return grid
    

def flip_down(grid):
    newGrid = copy.deepcopy(grid)
    for y in range(4):
        for x in range(4):
            grid[y][x] = newGrid[x][y]
            
    return grid  


def flip_down2(grid):
    newGrid = copy.deepcopy(grid) 
    for x in range(4):
        grid[3-x] = newGrid[x]
    
    return grid

def swapX(grid):
    newGrid = copy.deepcopy(grid)
    for y in range(4):
        for x in range(4):
            grid[y][x] = newGrid[y][3-x]
            
    return grid

def swapXBack(grid):
    newGrid = copy.deepcopy(grid)
    for y in range(4):
        for x in range(4):
            grid[y][3-x] = newGrid[y][x]
            
    return grid
    
    
def remove_zeros(grid):
    for x in range(4): 
        grid[x] = [value for value in grid[x] if value != 0]
        
    
    return grid

def add_zeros(grid):
    for x in range(4):
        length = len(grid[x])
        for y in range(4-length):
            grid[x].append(0)
    return grid

def add(grid):
    
    for y in range(4):
        for x in range(3):
            if(grid[y][x] == grid[y][x+1]):
                grid[y][x] = grid[y][x]*2
                grid[y][x+1] = 0
                grid = remove_zeros(grid)
                grid = add_zeros(grid)
    return grid
    
def push_up(grid):
    #util.print_grid((grid))
    #util.print_grid((flip_up(grid)))
    flip = flip_up(grid)
    removeZeros = remove_zeros(flip)
    #util.print_grid((add_zeros(removeZeros)))
    addZeros = add_zeros(removeZeros)
    #util.print_grid((add(addZeros)))
    add2 = add(addZeros)
    #util.print_grid((flip_down(add2)))
    flipDown = (flip_down(add2))
    grid = flipDown
    return grid
        
def push_left(grid):
    #util.print_grid(grid)
    removeZeros = remove_zeros(grid)
    addZeros = add_zeros(removeZeros)
    add2 = add(addZeros)
    #util.print_grid(add2)
    
    return add2
    
def push_down(grid):
    #util.print_grid((grid))
    
    flipUp2 = flip_up2(grid)
    #util.print_grid((flip_up(grid)))
    
    flip = flip_up(flipUp2)
    
    removeZeros = remove_zeros(flip)
    #util.print_grid((add_zeros(removeZeros)))
    
    addZeros = add_zeros(removeZeros)
    #util.print_grid((add(addZeros)))
    
    add2 = add(addZeros)
    #util.print_grid((flip_down(add2)))
    
    flipDown = flip_down(add2)
    flipDown2 = flip_down2(flipDown)
    #util.print_grid(flipDown2) 
    
    return flipDown2
    
def push_right(grid):
    #util.print_grid(grid)
    
    swap = swapX(grid)
    #util.print_grid(swap)
    
    removeZeros = remove_zeros(swap)
    addZeros = add_zeros(removeZeros)
    #util.print_grid(addZeros)
    
    add2 = add(addZeros)
    #util.print_grid(add2)
    
    swapBack = swapXBack(add2)
    #util.print_grid(swapBack)
    
    return swapBack
    
