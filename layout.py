#layout must be symmetrical according to these rules:
#size x size square (often 15?)
#black squares are reflected diagonally - so mathematically:
# in an nxn square, a black box at (i, j) will be at (n-i, n-j)
# there are ?? black squares in a typical crossword - click to place?
# squares are number-incremented if the square above and/or to the left is a border or black square

#Initialization: input as many words as desired for auto placement and size of the crossword
# common letters in these words are found and words that don't fit are placed toward edge
# can click to cycle through placement options (or click "back")
# clear a word by clicking on the slot and deleting or clicking space
# clues are auto-generated and assume format of "answer: word" for default initial value

import pygame
pygame.init()
pygame.display.set_caption('Crossword Maker')

#function definitions!
def init_game(screen, dimensions):
    print('do init stuff')
    #TODO: load saved game option (popup)
    #otherwise input words if desired
    #input size of board
    size = 15
    #call a function to find possible intersections of words
    #lay out the board
    rectlist = [[0 for x in range(size)] for y in range(size)]
    numlist = [[0 for x in range(len(rectlist))] for y in range(len(rectlist))]
    rectlist = do_layout(screen, rectlist, numlist)
    update_nums(screen, numlist, rectlist)
    #place the
    return rectlist, numlist

def do_layout(screen, rectlist, numlist):
    dimensions = [screen.get_width()-20, screen.get_height()-20, 10]
    #place buttons: click for black box, click for 
    #lay out the boxes
    startx = dimensions[0]-dimensions[1]+dimensions[2]
    starty = dimensions[2]
    boxsize = dimensions[1]/len(rectlist)
    for nx in range(len(rectlist)):
        for ny in range(len(rectlist)):
            if numlist[nx][ny] == 0:
                rectlist[nx][ny] = pygame.draw.rect(screen, (0, 0, 0), (startx+nx*boxsize, starty+ny*boxsize, boxsize, boxsize), 1)
            else:
                rectlist[nx][ny] = pygame.draw.rect(screen, (0, 0, 0), (startx+nx*boxsize, starty+ny*boxsize, boxsize, boxsize))
    pygame.draw.rect(screen, (0, 0, 0), (startx, starty, boxsize*len(rectlist), boxsize*len(rectlist)), 3)
    return rectlist
    
def reflect_black(screen, numlist, rectlist, rx, ry):
    numlist[rx][ry] = 1
    numlist[len(rectlist)-rx-1][len(rectlist)-ry-1] = 1
    return update_nums(screen, numlist, rectlist)

def update_nums(screen, numlist, rectlist):
    screen.fill((250, 250, 250))
    do_layout(screen, rectlist, numlist)
    #given a list of where there are black squares
    #number anything that is below or right of a border or black square
    count = 1
    num_font = pygame.font.SysFont("arial", 10)
    for ry in range(len(numlist)):
        for rx in range(len(numlist)):
            if numlist[rx][ry] == 0: #if white square
                if ry == 0 or rx ==0: #edges
                    text = num_font.render(str(count), True, (0, 0, 0))
                    screen.blit(text, (rectlist[rx][ry].x+4, rectlist[rx][ry].y+4))
                    count += 1
                elif numlist[rx-1][ry] == 1 or numlist[rx][ry-1] == 1:
                    text = num_font.render(str(count), True, (0, 0, 0))
                    screen.blit(text, (rectlist[rx][ry].x+4, rectlist[rx][ry].y+4))
                    count += 1
    pygame.display.flip()
    return numlist
    #return a list of where there are numbers now

if __name__=='__main__':

    height = 600;
    width = 800; #clues are to the left + add scroll bar later!
    border = 10
    screen = pygame.display.set_mode((width+border*2, height+border*2))

    #choose what font and size to use
    clue_font = pygame.font.SysFont("arial", 14)
    cross_font = pygame.font.SysFont("arial", 16)

    #make an object with that font, certain words and certain color
    text = clue_font.render("Hello, World", True, (0, 0, 0))
    screen.fill((250, 250, 250))

    running = 1 #1 = init, 2 = run, 0 = stop
    while running:
        #check if exit from game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #TODO: add save method
                #TODO: add ctrl-Q and ctrl-W
                running = 0
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for rx in range(len(rectlist)):
                        for ry in range(len(rectlist)):
                            if rectlist[rx][ry].collidepoint(pygame.mouse.get_pos()):
                                numlist = reflect_black(screen, numlist, rectlist, rx, ry)
                                break
                        else:
                            continue
                        break
        
        #initialize the game if this is the first run through
        if running == 1:
            rectlist, numlist = init_game(screen, [width, height, border]) #TODO: not sure if I can pass these objects and they'll get saved...
            
            running += 1
        else:
            
            #update screen, check for events, etc.
            pass
        
        #TODO: button to increase clue font size + size of whole crossword
        #TODO: click on a square to turn it black and call "reflect" method
        #TODO: add suggestions for words that fit
        screen.blit(text, (border, border))
        
        pygame.display.flip()


    pygame.quit()

