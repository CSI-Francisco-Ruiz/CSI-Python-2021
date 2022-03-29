import pygame

#Begin pygame, which has been imported beforehand
pygame.init()

#Colors are defined with the use of variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

#Window size is set thanks to the use of the variable dis
dis = pygame.display.set_mode((800, 600))

#Snake game caption is set
pygame.display.set_caption('Snake Game by Edureka')

#A variable is created called game_over which will be used in the while loop, which is defined as false. 
game_over = False

#x1 and y1 are defined as a fixed ammount, 300 wide and 300 tall 
x1 = 300
y1 = 300

#New variables are created that continuously update the snake's location
x1_change = 0       
y1_change = 0

#New variable called clock is created, and its purpose is to keep track of time during the game
clock = pygame.time.Clock()

#A new while loop is created
while not game_over:

    #The purpose of this line of code is to check the current events and renew the locations with the use of keys and for logic
    for event in pygame.event.get():

        #Using if logic, in an event where the user hits the X, the game will close
        if event.type == pygame.QUIT:
            game_over = True
        
        #The following block of code used if logic for every situation where a key is selected
        if event.type == pygame.KEYDOWN:

            #When the left key is pressed, the snake will move -10 coordinates to the left
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            
            #When the right key is pressed, the snake will move +10 coordinates to the right
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            
            #When the up key is pressed, the snake will move -10 coordinates upwards
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            
            #When the down key is pressed, the snake will move +10 coordinates downwards
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    #New coordinate values are created in order to change coordinates of the snake head. 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)

    #A rectangle is created using the variables dis and black, as well as coordinate values
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
    
    #The display is updated 
    pygame.display.update()
    
    #The clock is ticked using a fixed amount of integers
    clock.tick(30)

#All current windows quit
pygame.quit()

#The entirety of pygames is quit
quit()