import pygame

#Begin pygame, which has been imported beforehand
pygame.init()

#Window size is set thanks to the use of the variable dis
dis=pygame.display.set_mode((400,300))

#Snake game caption is set
pygame.display.set_caption('Snake game by Edureka')
 
#Colors are defined with the use of variables
blue=(0,0,255)
red=(255,0,0)

#A variable is created called game_over which will be used in the while loop, which is defined as false. 
game_over=False

#While loop is created with the use of game_over 
while not game_over:

    #Events are checked using for logic
    for event in pygame.event.get():

        #Using if logic, in an event where the user hits the X, the game will close
        if event.type==pygame.QUIT:

            #Since the game has ended, game_over will be defined as true
            game_over=True

    #A rectangle is created using the variable dis and blue
    pygame.draw.rect(dis,blue,[200,150,10,10])

    #The display is updated 
    pygame.display.update()

#All current windows quit
pygame.quit()

#The entirety of pygames is quit
quit()