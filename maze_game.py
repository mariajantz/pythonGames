def blank_grid(height, width):
    return [['#' for i in range(height)] for i in range(width)]

def start(height, width):
    maze = blank_grid(height, width)
    maze[0][0] = 'x'
    return maze

def import_maze(filename):
    maze = open(filename, 'r')
    maze_list = []
    for row in maze:
        maze_list.append(row.split())
    return [maze_list, start(len(maze_list[0]), len(maze_list))]

def get_input():
    direction = raw_input("Direction? ").lower()
    if direction == "":
        return
    else:
        direction = direction[0]
    if direction == "e":
        print("Exiting. Thanks for playing!")
        return direction
    elif direction!="l" and direction!="r" and direction!="u" and direction!="d":
        print("Not a valid direction.")
        get_input()
    else:
        return direction

def print_maze(maze):
    print("\n")*30
    for i in maze:
        temp = ""
        for j in i:
            temp = temp + " " + j
        print(temp)

def islegal(newrow, newcol, showmaze):
    if newcol==len(showmaze[0]): #check to the right
        return False #means not a valid direction
    if newcol<0: #check left
        return False 
    if newrow==len(showmaze): #check down
        return False 
    if newrow<0: #check up
        return False 
    if showmaze[newrow][newcol] == '|':
        return False
    return True #means you AREN'T at the edge

def unfog(row, col, showmaze, fullmaze):
    height, width = len(showmaze), len(showmaze[0])
    for arow in range(-1, 2):
        for acol in range(-1, 2):
            if [arow, acol] != [0, 0]:
                if islegal(row+arow, col+acol, showmaze):
                    showmaze[row+arow][col+acol] = fullmaze[row+arow][col+acol]
    return showmaze

def run_puzzle(showmaze=import_maze("amaze.txt")[1], fullmaze = import_maze("amaze.txt")[0], row=0, col=0, valid=True):
    showmaze = unfog(row, col, showmaze, fullmaze)
    if valid:
        print_maze(showmaze)
    if showmaze[row][col] == 'e':
        print("You win!")
        return
    direction = get_input()
    valid=True
    newrow, newcol = row, col
    if direction == "e":
        return
    elif direction=="r":
        if not islegal(row, col+1, showmaze):
            valid=False
        else:
            newcol+=1
    elif direction=="l":
        if not islegal(row, col-1, showmaze):
            valid=False
        else:
            newcol-=1
    elif direction=="d":
        if not islegal(row+1, col, showmaze):
            valid=False
        else:
            newrow+=1
    elif direction=="u":
        if not islegal(row-1, col, showmaze):
            valid=False
        else:
            newrow-=1
    if valid:
        if showmaze[newrow][newcol] == 'e':
            showmaze[newrow][newcol] = 'x'
            showmaze = unfog(newrow, newcol, showmaze, fullmaze)
            print_maze(showmaze)
            print("You win!")
            return
        showmaze[newrow][newcol] = 'x'

    else:
        print("Not a valid move.")

    run_puzzle(showmaze, fullmaze, newrow, newcol, valid)

run_puzzle()
