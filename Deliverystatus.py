#Importing modules
import pygame, sys
from pygame import mixer

#Importing user-defined modules
import Endingwindow
def Pacmanplayer(file):
    global file_name
    file_name=file
    #Initializing pygame and pygame mixer
    pygame.init()  
    mixer.init()

    #Creating screen for animation
    screen = pygame.display.set_mode((1298, 800))

    #Setting the title
    pygame.display.set_caption("Bite o'Clock - Delivery Status")

    #Setting icon
    pygame.display.set_icon(pygame.image.load('ChefLogo.png')) 

    #Boundary lines
    lines_img = pygame.image.load('lines.png')
    linesx = 100
    linesy = 185
    lines_img2 = pygame.image.load('lines.png')
    linesy2 = 195
    lines_img3 = pygame.image.load('lines.png')
    linesy3 = 445
    lines_img4 = pygame.image.load('lines.png')
    linesy4 = 455

    #Function to display the lines on the screen
    def lines():
        screen.blit(lines_img, (linesx,linesy))
        screen.blit(lines_img2, (linesx, linesy2))
        screen.blit(lines_img3, (linesx, linesy3))
        screen.blit(lines_img4, (linesx, linesy4))

    #Ghosts
    ghostx = 400
    ghosty = 300

    #Red ghost
    red_list=[]
    red_list.append(pygame.image.load('red0.gif'))
    red_list.append(pygame.image.load('red1.gif'))
    red_list.append(pygame.image.load('red2.gif'))
    red_list.append(pygame.image.load('red3.gif'))
    red_list.append(pygame.image.load('red4.gif'))
    red_list.append(pygame.image.load('red5.gif'))
    red_list.append(pygame.image.load('red6.gif'))
    red_list.append(pygame.image.load('red7.gif'))
    red_list.append(pygame.image.load('red8.gif'))
    red_steps=9
    frame_red=0

    #Blue ghost
    blue_list=[]
    blue_list.append(pygame.image.load('blue0.gif'))
    blue_list.append(pygame.image.load('blue1.gif'))
    blue_list.append(pygame.image.load('blue2.gif'))
    blue_list.append(pygame.image.load('blue3.gif'))
    blue_list.append(pygame.image.load('blue4.gif'))
    blue_list.append(pygame.image.load('blue5.gif'))
    blue_list.append(pygame.image.load('blue6.gif'))
    blue_list.append(pygame.image.load('blue7.gif'))
    blue_list.append(pygame.image.load('blue8.gif'))
    blue_steps=9
    frame_blue=0

    #Pink ghost
    pink_list=[]
    pink_list.append(pygame.image.load('pink0.gif'))
    pink_list.append(pygame.image.load('pink1.gif'))
    pink_list.append(pygame.image.load('pink2.gif'))
    pink_list.append(pygame.image.load('pink3.gif'))
    pink_list.append(pygame.image.load('pink4.gif'))
    pink_list.append(pygame.image.load('pink5.gif'))
    pink_list.append(pygame.image.load('pink6.gif'))
    pink_list.append(pygame.image.load('pink7.gif'))
    pink_list.append(pygame.image.load('pink8.gif'))
    pink_steps=9
    frame_pink=0

    #Yellow ghost
    yellow_list=[]
    yellow_list.append(pygame.image.load('yellow0.gif'))
    yellow_list.append(pygame.image.load('yellow1.gif'))
    yellow_list.append(pygame.image.load('yellow2.gif'))
    yellow_list.append(pygame.image.load('yellow3.gif'))
    yellow_list.append(pygame.image.load('yellow4.gif'))
    yellow_list.append(pygame.image.load('yellow5.gif'))
    yellow_list.append(pygame.image.load('yellow6.gif'))
    yellow_list.append(pygame.image.load('yellow7.gif'))
    yellow_list.append(pygame.image.load('yellow8.gif'))
    yellow_steps=9
    frame_yellow=0
            
    #Pac-man
    animation_list = []
    animation_list.append(pygame.image.load('pac0r.png'))
    animation_list.append(pygame.image.load('pac1r.png'))
    animation_list.append(pygame.image.load('pac3r.png'))
    animation_list.append(pygame.image.load('pac4r.png'))
    animation_steps=4
    last_update=pygame.time.get_ticks()
    animation_cooldown=60
    frame=0

    #Displaying Text
    text = pygame.image.load('msg1.png')
    text2 = pygame.image.load('msg2.png')
    text3 = pygame.image.load('msg3.png')
    text4 = pygame.image.load('msg4.png')
    text5 = pygame.image.load('thanks.png')

    #Pac-man sounds
    collide=mixer.Sound('eating.mp3')
    collide.set_volume(0.3)

    #Running the game (all constant features in this loop)
    run = True
    pacx=200


    while run:
        
        transparent=(0,0,0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #Close if user clicks cross (got all events)
                run = False
                sys.exit()


        if int(pacx)<1090:
            current_time = pygame.time.get_ticks()
            if current_time - last_update >= animation_cooldown:
                frame += 1
                frame_red += 1
                frame_blue += 1
                frame_pink += 1
                frame_yellow += 1
                last_update = current_time
                if frame >= len(animation_list):
                    frame = 0
                if frame_red>=len(red_list):
                    frame_red=0
                if frame_blue>=len(blue_list):
                    frame_blue=0
                if frame_pink>=len(pink_list):
                    frame_pink=0
                if frame_yellow>=len(yellow_list):
                    frame_yellow=0


            if int(pacx)==ghostx-30:
                for i in red_list:
                    i.fill(transparent)
                screen.blit(text, (350,600))
                collide.play()

            elif int(pacx)==ghostx+170:
                for i in blue_list:
                    i.fill(transparent)
                screen.fill((0, 0,0), (0, 600, screen.get_width(), 170))
                screen.blit(text2, (340, 600))
                collide.play()


            elif int(pacx)==ghostx+370:
                for i in pink_list:
                    i.fill(transparent)
                screen.fill((0, 0, 0), (0, 600, screen.get_width(), 170))
                screen.blit(text3, (390, 600))
                collide.play()


            elif int(pacx)==ghostx+580:
                for i in yellow_list:
                    i.fill(transparent)
                screen.fill((0, 0, 0), (0, 600, screen.get_width(), 170))
                screen.blit(text4, (350, 600))
                collide.play()
                
                
            elif int(pacx)==1080:
                run = False
                pygame.quit()
                Endingwindow.endwin(file_name)
                sys.exit()
                
            
            screen.fill((0,0,0), (100, 225, screen.get_width(), 270))
            screen.blit(text5, (325, 100))
            lines()
            screen.blit(red_list[frame_red],(ghostx,ghosty))
            screen.blit(blue_list[frame_blue],(ghostx+200,ghosty))
            screen.blit(pink_list[frame_pink],(ghostx+400,ghosty))
            screen.blit(yellow_list[frame_yellow],(ghostx+600,ghosty))
            screen.blit(animation_list[frame], (pacx, 293))
            
            pacx += 0.28
            if ghosty<=312:
                ghosty+=0.15
            if ghosty>=308:
                ghosty=300
            
        #Updates all events
        pygame.display.update() 



