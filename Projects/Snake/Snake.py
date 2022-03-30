import pygame
import time

#Begin pygame, which has been imported beforehand
pygame.init()

#Colors are defined with the use of variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
#The distance of the width and the height are set as fixed integers
dis_width = 800
dis_height  = 600

#Window size is set thanks to the use of the variable dis as well as the previously defined dis_width
dis = pygame.display.set_mode((dis_width, dis_width))

#Snake game caption is set
pygame.display.set_caption('Snake Game by Edureka')

#A variable is created called game_over which will be used in the while loop, which is defined as false. 
game_over = False

#The x1 and y1 coordinate values are defined as the halves of the previously defined dis_width and dis_height
x1 = dis_width/2
y1 = dis_height/2

#The snake block's amount of space taken take is defined 
snake_block=10

#The x1_change and y1_change variables are created that continuously update the snake's location
x1_change = 0
y1_change = 0

#The game's clock is created in order to track the time that has passed
clock = pygame.time.Clock()

#The snake's speed is set as a fixed integer
snake_speed=30

#Font style is set although no font has been chosen yet, leaving only the size
font_style = pygame.font.SysFont(None, 50)

#A new function called message is defined 
def message(msg,color):

    #The message's font style and color is rendered, as well as its dimensions
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

#A while loop using the variable game_over is created
while not game_over:
    #The purpose of this line of code is to check the current events and renew the locations with the use of keys and for logic
    for event in pygame.event.get():

        #Using if logic, in an event where the user hits the X, the game will close
        if event.type == pygame.QUIT:
            game_over = True
        
         #The following block of code used if logic for every possible event where a key is selected
        if event.type == pygame.KEYDOWN:

            #When the left key is pressed, the snake will move -10 coordinates to the left
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            
            #When the right key is pressed, the snake will move +10 coordinates to the right
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            
            #When the up key is pressed, the snake will move -10 coordinates upwards
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            
            #When the down key is pressed, the snake will move +10 coordinates downwards
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    
    #Everytime that the height and width's borders are exceeded, game_over will take effect
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
    
    #Coordinate values are created in order to change coordinates of the snake head, as well as its coloration. 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)

    #A rectangle is created using the variables dis and black, as well as coordinate values
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
 
    #The display is updated 
    pygame.display.update()
    
    #The clock now ticks at the snake's movement speed, instead of a fixed amount
    clock.tick(snake_speed)

#The previously created message function is used to print "You lost" in red
message("You lost",red)

#The diplay is updated
pygame.display.update()

#The time value is set to "sleep" using the sleep function
time.sleep(2)

#All current windows quit
pygame.quit()

#The entirety of pygames is quit
quit()