import random
import sys  #sys.exit to exit the game
import pygame
from pygame.locals import * #basic pygame imports

#Global variables throughout the  game
fps = 50
screen_width = 1296
screen_height = 648

screen = pygame.display.set_mode((screen_width,screen_height))
game_sprites = {}
game_sounds = {}
character1 = 'Data/Images/character_stance-1.png'
character2 = 'Data/Images/character_stance-2.png'
character3 = 'Data/Images/character_stance-3.png'
character4 = 'Data/Images/character_stance-4.png'
character5 = 'Data/Images/character_stance-5.png'
character6 = 'Data/Images/character_stance-6.png'
background1 = 'Data/Images/background-1.jpg'
background2 = 'Data/Images/background-2.jpg'
background3 = 'Data/Images/background-3.png'
pipe ='Data/Images/pipe.png'
brick = 'Data/Images/brick.png'
start_screen = 'Data/Images/start_screen.jpg'
logo = 'Data/Images/logo.png'
beetle1 = 'Data/Images/beetle-1.png'
beetle2 = 'Data/Images/beetle-2.png'

def welcomeScreen():
    
    while True:
        for event in pygame.event.get():
            if event.type ==  QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == KEYDOWN and (event.key == K_KP_ENTER):
                return
            else:
                screen.blit(game_sprites['start_screen'], (0,0))
                pygame.display.update()
                clock.tick(fps)
                

def mainGame():
   score = 0
   charx = int(screen_width/10)
   chary = int(screen_height-(screen_height-game_sprites['character1'].get_height()))*6.2 #-game_sprites['pipe'].get_height() 
    #creating pipe   
    # pipeHeight = game_sprites['pipe'].get_height()
   pipe1x = int(900)
   pipe1y = int(480)
   pipe2x = int(400)
   pipe2y = int(480)
   beetlex = int(random.randint(450,850))
   beetley = int(530)
   beetle_vel_x = 5
   beetle_dir = 1
   jump_count = 10
   Jumping = False
   
   current_char = game_sprites['character1']
   curr_beetle = game_sprites['beetle2']
   
   while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        keys = pygame.key.get_pressed()         
        if keys[pygame.K_RIGHT]:
            if current_char == game_sprites['character1']:
                current_char = game_sprites['character2']
            elif current_char == game_sprites['character2']:
                current_char = game_sprites['character3']
            else:
                current_char = game_sprites['character1']    
            if (charx <= 340 or charx>=410) and (charx <=840 or charx >=910):
                    charx += 10
        if keys[pygame.K_LEFT]:
            
            if current_char == game_sprites['character4']:
                current_char = game_sprites['character5']
            elif current_char == game_sprites['character5']:
                current_char = game_sprites['character6']
            else:
                current_char = game_sprites['character4']
            if not (charx < 450 and charx>370) and not (charx < 950 and charx >870) and charx > 0:
                charx -= 10
        if keys[K_SPACE] and not Jumping:
                    Jumping =True
        if keys[K_SPACE] and keys[pygame.K_RIGHT]:
            if charx >=330 and charx <=400:
                charx = pipe2x + 50
            elif charx >= 830 and charx<=900:
                charx = pipe1x + 50    
                    
        if keys[K_SPACE] and keys[pygame.K_LEFT]:
            if charx <=470 and charx>400: 
                charx = pipe2x - 50
            elif charx <=970 and charx >900:
                charx = pipe1x -50        
        if Jumping:
            if jump_count >=-10:
                chary -= (jump_count * abs(jump_count))*0.5
                # charx =+ 10
                jump_count -= 1 
            
            # elif abs(charx - pipe2x) > 50 and abs(charx -pipe1x)>50:
            #     chary == game_sprites['pipe'].get_height()
            else:
             Jumping = False    
             jump_count = 10
             chary = int(screen_height-(screen_height-game_sprites['character1'].get_height()))*6.2 
        
        
        #beetle related 
        beetlex += beetle_dir * beetle_vel_x
        if beetlex >= 850:
            beetle_dir *= -1
            curr_beetle = game_sprites['beetle1']
        if beetlex <= 450: 
            beetle_dir *= -1
            curr_beetle = game_sprites['beetle2']

        screen.blit(game_sprites['background-1'], ( 0,0))
        screen.blit(game_sprites['pipe'], ( pipe2x,pipe2y))
        screen.blit(game_sprites['pipe'], ( pipe1x,pipe1y))
        
        screen.blit(current_char, (charx, chary))
        
        
        screen.blit(curr_beetle, (beetlex, beetley))
        pygame.display.update()
        clock.tick(fps)
                
                
if __name__ == "__main__":
    #Main function from where game starts
    pygame.init() #initializes all pygame modules
    clock = pygame.time.Clock()
    pygame.display.set_caption('Adventures By Elites')
    
    # Game sprites
    game_sprites['start_screen'] = pygame.image.load(start_screen).convert_alpha()
    game_sprites['pipe'] = pygame.image.load(pipe).convert_alpha()
    game_sprites['logo'] = pygame.image.load(logo).convert_alpha()
    game_sprites['background-1'] = pygame.image.load(background1).convert()
    game_sprites['background-2'] = pygame.image.load(background2).convert()
    game_sprites['background-3'] = pygame.image.load(background3).convert()
    game_sprites['character1'] = pygame.image.load(character1).convert_alpha()
    game_sprites['character2'] = pygame.image.load(character2).convert_alpha()
    game_sprites['character3'] = pygame.image.load(character3).convert_alpha()
    game_sprites['character4'] = pygame.image.load(character4).convert_alpha()
    game_sprites['character5'] = pygame.image.load(character5).convert_alpha()
    game_sprites['character6'] = pygame.image.load(character6).convert_alpha()
    game_sprites['beetle2'] = pygame.image.load(beetle2).convert_alpha()
    game_sprites['beetle1'] = pygame.image.load(beetle1).convert_alpha()
    
    # Game Sounds     
    # game_sounds['game-over'] = pygame.mixer.Sound('Data/Music/game-over.wav')
    # game_sounds['hit'] = pygame.mixer.Sound('Data/Music')
    # game_sounds['coins'] = pygame.mixer.Sound('Data/Music')
    # game_sounds['jump'] = pygame.mixer.Sound('Data/Music')
    # game_sounds['something'] = pygame.mixer.Sound('Data/Music')
    

# Game Loop    
while True:
    welcomeScreen() 
    mainGame()