grid = []
import push
import copy

def create_grid(grid):
    for x in range(4):
        grid.append([])
        for y in range(4):  
            grid[x].append(0)
                        
            
def print_grid(grid):
    print("+--------------------+")
    for x in range(4):
        print("|", end="")
        for y in range(4): 
            spaces = 5
            if(grid[x][y] > 0):
                spaces = spaces - len(str(grid[x][y]))
                print(grid[x][y], end="")
            for p in range(spaces):
                print(" ", end="")
        print("|")
        
    print("+--------------------+")
        
def check_lost(grid):
    check = 0
    returnHolder = True
    
    check5 = copy.deepcopy(grid)
    check1 = copy.deepcopy(grid)
    check2 = copy.deepcopy(grid)
    check3 = copy.deepcopy(grid)
    check4 = copy.deepcopy(grid)
    
    if(push.push_up(check1) != check5):
        returnHolder = False
    elif(push.push_down(check2) != check5):
        returnHolder = False
    elif(push.push_left(check3) != check5):
        returnHolder = False    
    elif(push.push_right(check4) != check5):
        returnHolder = False

    for x in range(4):
        for y in range(4):     
            if(check5[x][y] == 0):
                check = check + 1   
                
            
                
    if (check == 0) and (returnHolder == True):
        return True
    else: 
        return False

def check_won(grid):
    returnHolder = False
    for x in range(4):
        for y in range(4):     
            if(grid[x][y] >= 32):   
                returnHolder = True
                
    return returnHolder

def copy_grid(grid):
    grid2 = []
    for x in range(4):
        grid2.append([])
        for y in range(4):  
            grid2[x].append(grid[x][y])
    
    return grid2

def grid_equal(grid, grid2):
    returnHolder = True
    for x in range(4):
        for y in range(4):     
            if(grid[x][y] != grid2[x][y]):  
                returnHolder = False
                break
    
    return returnHolder