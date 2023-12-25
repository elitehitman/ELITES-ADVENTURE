import random
import sys  # sys.exit to exit the game
import pygame
from pygame.locals import *  # basic pygame imports

# Global variables throughout the  game
fps = 50
screen_width = 1296
screen_height = 648

screen = pygame.display.set_mode((screen_width, screen_height))
game_sprites = {}
game_sounds = {}
character1 = "Data/Images/character_stance-1.png"
character2 = "Data/Images/character_stance-2.png"
character3 = "Data/Images/character_stance-3.png"
character4 = "Data/Images/character_stance-4.png"
character5 = "Data/Images/character_stance-5.png"
character6 = "Data/Images/character_stance-6.png"
background1 = "Data/Images/background-1.jpg"
background2 = "Data/Images/background-2.jpg"
background3 = "Data/Images/background-3.png"
pipe = "Data/Images/pipe.png"
brick = "Data/Images/brick.png"
start_screen = "Data/Images/start_screen.jpg"
logo = "Data/Images/logo.png"
beetle1 = "Data/Images/beetle-1.png"
beetle2 = "Data/Images/beetle-2.png"
cannon = "Data/Images/Cannon.png"
cannonInverted = "Data/Images/CannonInverted.png"
bulletLeft = "Data/Images/bullet-left.png"
bulletRight = "Data/Images/bullet-right.png"
bricks3 = "Data/Images/bricks.png"
flag = "Data/Images/flag.png"
lever = "Data/Images/lever.png"
leverPull = "Data/Images/leverPull.png"
flagLift = "Data/Images/flag1.png"
drag1 = "Data/Images/images/drag1.png"
drag2 = "Data/Images/images/drag2.png"
drag3 = "Data/Images/images/drag3.png"
drag4 = "Data/Images/images/drag4.png"
drag5 = "Data/Images/images/drag5.png"
drag6 = "Data/Images/images/drag6.png"
drag7 = "Data/Images/images/drag7.png"
drag8 = "Data/Images/images/drag8.png"
drag9 = "Data/Images/images/drag9.png"
drag10 = "Data/Images/images/drag10.png"
drag11 = "Data/Images/images/drag11.png"
drag12 = "Data/Images/images/drag12.png"
drag13 = "Data/Images/images/drag13.png"
drag14 = "Data/Images/images/drag14.png"
drag15 = "Data/Images/images/drag15.png"
drag16 = "Data/Images/images/drag16.png"
drag17 = "Data/Images/images/drag17.png"
fire = "Data/Images/fire.png"
fire2 = "Data/Images/fire2.png"
end = "Data/Images/end.png"
crusher = "Data/Images/crusher.png"
restart = "Data/Images/restart.jpg"


def welcomeScreen():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_RETURN):
                return
            else:
                screen.blit(game_sprites["start_screen"], (0, 0))
                pygame.display.update()
                clock.tick(fps)


def mainGame():
    curr_stage = 1
    score = 0
    charx = int(screen_width / 10)
    chary = (
        int(screen_height - (screen_height - game_sprites["character1"].get_height()))
        * 6.2
    )  # -game_sprites['pipe'].get_height()
    # creating pipe
    # pipeHeight = game_sprites['pipe'].get_height()
    pipe1x = int(900)
    pipe1y = int(480)
    pipe2x = int(400)
    pipe2y = int(480)
    beetlex = int(random.randint(450, 850))
    beetley = int(530)
    beetle_vel_x = 5
    bullet_left_x = 573
    bullet_left_x2 = screen_width - 100
    bullet_right_x = 653
    bullet_left_vel = -5
    bullet_right_vel = 5
    cannon_x = 600
    cannon_y = 490
    beetle_dir = 1
    jump_count = 10
    flagx = 0
    flagy = 490
    Jumping = False
    flag_activated = False
    lever_activated = False
    flag_lift = False
    drag_x = 1000
    drag_y = 360
    drag_vel_y = -2
    drag_dir = 1
    fire_x = 950
    fire_x2 = 1300
    fire_vel = -5
    x = False
    crusher_y = -350
    crusher_x = 250
    crusher_vel = 10
    crusher_dir = 1

    current_char = game_sprites["character1"]
    character_rect = current_char.get_rect(topleft=(charx, chary))
    curr_beetle = game_sprites["beetle2"]

    curr_background = game_sprites["background-3"]
    curr_dragon = game_sprites["drag1"]
    fire_y = drag_y + 70
    drag_y += drag_dir * drag_vel_y

    game_font = pygame.font.Font(None, 50)
    game_name = game_font.render("Flario", False, (116, 196, 169))
    game_name_rect = game_name.get_rect(center=(648, 200))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()

        if curr_stage == 1:
            # rectangle and the collison detector
            character_rect.topleft = (charx, chary)
            beetlerect = game_sprites["beetle2"].get_rect(topleft=(beetlex, beetley))
            if character_rect.colliderect(beetlerect):
                curr_stage = 5

            curr_background = game_sprites["background-1"]
            screen.blit(curr_background, (0, 0))
            screen.blit(current_char, (charx, chary))
            screen.blit(game_sprites["pipe"], (pipe2x, pipe2y))
            screen.blit(game_sprites["pipe"], (pipe1x, pipe1y))
            screen.blit(curr_beetle, (beetlex, beetley))
            if keys[pygame.K_RIGHT]:
                if current_char == game_sprites["character1"]:
                    current_char = game_sprites["character2"]
                elif current_char == game_sprites["character2"]:
                    current_char = game_sprites["character3"]
                else:
                    current_char = game_sprites["character1"]
                if (charx <= 340 or charx >= 410) and (charx <= 840 or charx >= 910):
                    charx += 10
            if keys[pygame.K_LEFT]:
                if current_char == game_sprites["character4"]:
                    current_char = game_sprites["character5"]
                elif current_char == game_sprites["character5"]:
                    current_char = game_sprites["character6"]
                else:
                    current_char = game_sprites["character4"]
                if (
                    not (charx < 450 and charx > 370)
                    and not (charx < 950 and charx > 870)
                    and charx > 0
                ):
                    charx -= 10
            if keys[K_SPACE] and not Jumping:
                Jumping = True
            if keys[K_SPACE] and keys[pygame.K_RIGHT]:
                if charx >= 330 and charx <= 400:
                    charx = pipe2x + 50
                elif charx >= 830 and charx <= 900:
                    charx = pipe1x + 50

            if keys[K_SPACE] and keys[pygame.K_LEFT]:
                if charx <= 470 and charx > 400:
                    charx = pipe2x - 50
                elif charx <= 970 and charx > 900:
                    charx = pipe1x - 50
            if Jumping:
                if jump_count >= -10:
                    chary -= (jump_count * abs(jump_count)) * 0.5
                    # charx =+ 10
                    jump_count -= 1

                # elif abs(charx - pipe2x) > 50 and abs(charx -pipe1x)>50:
                #     chary == game_sprites['pipe'].get_height()
                else:
                    Jumping = False
                    jump_count = 10
                    chary = (
                        int(
                            screen_height
                            - (screen_height - game_sprites["character1"].get_height())
                        )
                        * 6.2
                    )

            # beetle related
            beetlex += beetle_dir * beetle_vel_x
            if beetlex >= 850:
                beetle_dir *= -1
                curr_beetle = game_sprites["beetle1"]
            if beetlex <= 450:
                beetle_dir *= -1
                curr_beetle = game_sprites["beetle2"]

            if charx > screen_width - 20:
                charx = 0
                curr_stage = 2
                # background_changed1 = True

            pygame.display.update()
            clock.tick(fps)

        elif curr_stage == 2:
            # rectangle and collison detector
            player_rect = current_char.get_rect(topleft=(charx, chary))
            bullet_left_rect = game_sprites["bullet-left"].get_rect(
                topleft=(bullet_left_x, 500)
            )
            bullet_left2_rect = game_sprites["bullet-left"].get_rect(
                topleft=(bullet_left_x2, 340)
            )
            bullet_right_rect = game_sprites["bullet-right"].get_rect(
                topleft=(bullet_right_x, 500)
            )

            if (
                player_rect.colliderect(bullet_left_rect)
                or player_rect.colliderect(bullet_left2_rect)
                or player_rect.colliderect(bullet_right_rect)
            ):
                curr_stage = 5

            curr_background = game_sprites["background-2"]
            screen.blit(curr_background, (0, 0))
            screen.blit(current_char, (charx, chary))
            if bullet_left_x < 0:
                bullet_left_x = 573
                bullet_left_x = bullet_left_x + bullet_left_vel
            if bullet_right_x > screen_width:
                bullet_right_x = 652
                bullet_right_x += bullet_right_vel
            if charx < 600:
                bullet_left_x += bullet_left_vel
                bullet_right_x = screen_width + 100
            if charx > 700:
                bullet_right_x += bullet_right_vel
                bullet_left_x = -50
            if keys[pygame.K_RIGHT]:
                if current_char == game_sprites["character1"]:
                    current_char = game_sprites["character2"]
                elif current_char == game_sprites["character2"]:
                    current_char = game_sprites["character3"]
                else:
                    current_char = game_sprites["character1"]
                if charx <= screen_width - 60:
                    charx += 10
            if keys[pygame.K_LEFT]:
                if current_char == game_sprites["character4"]:
                    current_char = game_sprites["character5"]
                elif current_char == game_sprites["character5"]:
                    current_char = game_sprites["character6"]
                else:
                    current_char = game_sprites["character4"]
                if charx >= 0:
                    charx -= 10
            if keys[K_SPACE] and not Jumping:
                Jumping = True

            if Jumping:
                if jump_count >= -10:
                    chary -= (jump_count * abs(jump_count)) * 0.5
                    # charx =+ 10
                    jump_count -= 1

                # elif abs(charx - pipe2x) > 50 and abs(charx -pipe1x)>50:
                #     chary == game_sprites['pipe'].get_height()
                else:
                    Jumping = False
                    jump_count = 10
                    chary = (
                        int(
                            screen_height
                            - (screen_height - game_sprites["character1"].get_height())
                        )
                        * 6.2
                    )
            curr_lever = game_sprites["lever"]
            if (
                charx > screen_width - 150
                and keys[pygame.K_LCTRL]
                and not lever_activated
            ):
                lever_activated = True
            if lever_activated:
                curr_lever = game_sprites["lever-pull"]
                bullet_left_x = screen_width + 500
            bullet_left_x2 += bullet_left_vel
            if bullet_left_x2 < 0:
                bullet_left_x2 = screen_width - 100
            flag1 = (game_sprites["flag"], (flagx, flagy))
            flag2 = (game_sprites["flag-lift"], (charx + 15, chary + 10))
            screen.blit(game_sprites["cannon"], (cannon_x, cannon_y))
            screen.blit(game_sprites["cannon-inverted"], (screen_width - 55, 300))
            screen.blit(game_sprites["bricks-3"], (screen_width - 180, 255))
            screen.blit(game_sprites["bullet-left"], (bullet_left_x, 500))
            screen.blit(game_sprites["bullet-left"], (bullet_left_x2, 340))
            screen.blit(game_sprites["bullet-right"], (bullet_right_x, 500))
            screen.blit(curr_lever, (screen_width - 80, 510))

            if (
                charx > screen_width - 150
                and keys[pygame.K_LCTRL]
                and not flag_activated
            ):
                flag_activated = True

            # If the flag is activated, keep drawing it at the same position
            if flag_activated and lever_activated:
                screen.blit(*flag1)
            if (
                flag_activated
                and lever_activated
                and charx < 50
                and keys[pygame.K_LCTRL]
            ):
                flag_lift = True
            if flag_lift:
                screen.blit(*flag2)
                flagx = -100
                if charx > 1200:
                    curr_stage = 3
                    # background_changed2 = True
                    charx = 0

            pygame.display.update()
            clock.tick(fps)

        elif curr_stage == 3:
            player_rect = current_char.get_rect(topleft=(charx, chary))
            crusher1_rect = game_sprites["crusher1"].get_rect(
                topleft=(crusher_x, crusher_y)
            )
            crusher2_rect = game_sprites["crusher2"].get_rect(
                topleft=(crusher_x + 250, crusher_y)
            )
            crusher3_rect = game_sprites["crusher3"].get_rect(
                topleft=(crusher_x + 500, crusher_y)
            )

            if (
                player_rect.colliderect(crusher1_rect)
                or player_rect.colliderect(crusher2_rect)
                or player_rect.colliderect(crusher3_rect)
            ):
                curr_stage = 5

            player_rect = current_char.get_rect(topleft=(charx, chary))
            dragon_rect = curr_dragon.get_rect(topleft=(drag_x, drag_y))
            fire_rect = game_sprites["fire"].get_rect(topleft=(fire_x, fire_y))
            fire2_rect = game_sprites["fire2"].get_rect(topleft=(fire_x2, fire_y))

            if player_rect.colliderect(dragon_rect):
                curr_stage = 5

            if player_rect.colliderect(fire_rect) or player_rect.colliderect(
                fire2_rect
            ):
                curr_stage = 5

            curr_background = game_sprites["background-3"]
            curr_dragon = game_sprites["drag1"]
            fire_y = drag_y + 70
            drag_y += drag_dir * drag_vel_y
            if drag_y <= 200:
                drag_dir *= -1
            if drag_y >= 400:
                drag_dir *= -1
            fire_x += fire_vel
            if fire_x < 600 and not x:
                fire_x2 = 950
                x = True
            if x:
                fire_x2 += fire_vel
            if fire_x < 0:
                fire_x = 950
            if fire_x2 < 0:
                fire_x2 = 950
            crusher_y += crusher_dir * crusher_vel
            if crusher_y > -50:
                crusher_dir *= -1
            if crusher_y < -350:
                crusher_dir *= -1

            # current_char = game_sprites["character1"]

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                current_char == game_sprites["character1"]
                if current_char == game_sprites["character1"]:
                    current_char = game_sprites["character2"]
                elif current_char == game_sprites["character2"]:
                    current_char = game_sprites["character3"]
                else:
                    current_char = game_sprites["character1"]
                if charx <= screen_width - 60:
                    charx += 10
            if keys[pygame.K_LEFT]:
                current_char == game_sprites["character4"]
                if current_char == game_sprites["character4"]:
                    current_char = game_sprites["character5"]
                elif current_char == game_sprites["character5"]:
                    current_char = game_sprites["character6"]
                else:
                    current_char = game_sprites["character4"]
                if charx >= 0:
                    charx -= 10
            if keys[K_SPACE] and not Jumping:
                Jumping = True

            if Jumping:
                if jump_count >= -10:
                    chary -= (jump_count * abs(jump_count)) * 0.5
                    # charx =+ 10
                    jump_count -= 1

                # elif abs(charx - pipe2x) > 50 and abs(charx -pipe1x)>50:
                #     chary == game_sprites['pipe'].get_height()
                else:
                    Jumping = False
                    jump_count = 10
                    chary = (
                        int(
                            screen_height
                            - (screen_height - game_sprites["character1"].get_height())
                        )
                        * 6.2
                    )
            if drag_y < 400 and drag_y > 375:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 375 and drag_y < 350:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 350 and drag_y < 325:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 325 and drag_y < 300:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 300 and drag_y < 275:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 275 and drag_y < 250:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 250 and drag_y < 225:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 225 and drag_y < 200:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 200 and drag_y < 225:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 225 and drag_y < 250:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 250 and drag_y < 275:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 275 and drag_y < 300:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 300 and drag_y < 325:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 325 and drag_y < 350:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 350 and drag_y < 375:
                curr_dragon = game_sprites["drag4"]

            elif drag_y > 375 and drag_y < 390:
                curr_dragon = game_sprites["drag6"]

            elif drag_y > 390 and drag_y < 400:
                curr_dragon = game_sprites["drag4"]

            screen.blit(curr_background, (0, 0))
            screen.blit(current_char, (charx, chary))
            screen.blit(curr_dragon, (drag_x, drag_y))
            screen.blit(game_sprites["fire"], (fire_x, fire_y))

            screen.blit(game_sprites["fire2"], (fire_x2, fire_y))

            screen.blit(game_sprites["crusher1"], (crusher_x, crusher_y))
            screen.blit(game_sprites["crusher2"], (crusher_x + 250, crusher_y))
            screen.blit(game_sprites["crusher3"], (crusher_x + 500, crusher_y))
            if charx > screen_width - 80:
                curr_stage = 4
                charx = 0
            pygame.display.update()
            clock.tick(fps)

        elif curr_stage == 4:
            curr_background = game_sprites["end"]
            screen.blit(game_sprites["end"], (0, 0))
            screen.blit(current_char, (charx, chary))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                curr_stage = 1
                charx = int(screen_width / 10)
                current_char = game_sprites["character1"]
            if keys[pygame.K_RIGHT]:
                current_char == game_sprites["character1"]
                if current_char == game_sprites["character1"]:
                    current_char = game_sprites["character2"]
                elif current_char == game_sprites["character2"]:
                    current_char = game_sprites["character3"]
                else:
                    current_char = game_sprites["character1"]
                if charx <= screen_width - 60:
                    charx += 10
            if keys[pygame.K_LEFT]:
                current_char == game_sprites["character4"]
                if current_char == game_sprites["character4"]:
                    current_char = game_sprites["character5"]
                elif current_char == game_sprites["character5"]:
                    current_char = game_sprites["character6"]
                else:
                    current_char = game_sprites["character4"]
                if charx >= 0:
                    charx -= 10
            if keys[K_SPACE] and not Jumping:
                Jumping = True

            if Jumping:
                if jump_count >= -10:
                    chary -= (jump_count * abs(jump_count)) * 0.5
                    # charx =+ 10
                    jump_count -= 1

                # elif abs(charx - pipe2x) > 50 and abs(charx -pipe1x)>50:
                #     chary == game_sprites['pipe'].get_height()
                else:
                    Jumping = False
                    jump_count = 10
                    chary = (
                        int(
                            screen_height
                            - (screen_height - game_sprites["character1"].get_height())
                        )
                        * 6.2
                    )
            pygame.display.update()
            clock.tick(fps)

        elif curr_stage == 5:
            curr_background = game_sprites["restart"]
            screen.blit(curr_background, (0, 0))
            if keys[pygame.K_RETURN]:
                curr_stage = 1
                charx = int(screen_width / 10)
                chary = (
                    int(
                        screen_height
                        - (screen_height - game_sprites["character1"].get_height())
                    )
                    * 6.2
                )
                beetlex = int(random.randint(450, 850))
                beetley = int(530)
                beetle_vel_x = 5
                bullet_left_x = 573
                bullet_left_x2 = screen_width - 100
                bullet_right_x = 653
                bullet_left_vel = -5
                bullet_right_vel = 5
                cannon_x = 600
                cannon_y = 490
                beetle_dir = 1
                jump_count = 10
                flagx = 0
                flagy = 490
                Jumping = False
                flag_activated = False
                lever_activated = False
                flag_lift = False
                drag_x = 1000
                drag_y = 360
                drag_vel_y = -2
                drag_dir = 1
                fire_x = 950
                fire_x2 = 1300
                fire_vel = -5
                x = False
                crusher_y = -350
                crusher_x = 250
                crusher_vel = 10
                crusher_dir = 1

                current_char = game_sprites["character1"]
                character_rect = current_char.get_rect(topleft=(charx, chary))
                curr_beetle = game_sprites["beetle2"]
            pygame.display.update()
            clock.tick(fps)


if __name__ == "__main__":
    # Main function from where game starts
    pygame.init()  # initializes all pygame modules
    clock = pygame.time.Clock()
    pygame.display.set_caption("Adventures By Elites")

    # Game sprites
    game_sprites["start_screen"] = pygame.image.load(start_screen).convert_alpha()
    game_sprites["pipe"] = pygame.image.load(pipe).convert_alpha()
    game_sprites["logo"] = pygame.image.load(logo).convert_alpha()
    game_sprites["background-1"] = pygame.image.load(background1).convert()
    game_sprites["background-2"] = pygame.image.load(background2).convert()
    game_sprites["background-3"] = pygame.image.load(background3).convert()
    game_sprites["character1"] = pygame.image.load(character1).convert_alpha()
    game_sprites["character2"] = pygame.image.load(character2).convert_alpha()
    game_sprites["character3"] = pygame.image.load(character3).convert_alpha()
    game_sprites["character4"] = pygame.image.load(character4).convert_alpha()
    game_sprites["character5"] = pygame.image.load(character5).convert_alpha()
    game_sprites["character6"] = pygame.image.load(character6).convert_alpha()
    game_sprites["beetle2"] = pygame.image.load(beetle2).convert_alpha()
    game_sprites["beetle1"] = pygame.image.load(beetle1).convert_alpha()
    game_sprites["cannon"] = pygame.image.load(cannon).convert_alpha()
    game_sprites["cannon-inverted"] = pygame.image.load(cannonInverted).convert_alpha()
    game_sprites["bullet-left"] = pygame.image.load(bulletLeft).convert_alpha()
    game_sprites["bullet-right"] = pygame.image.load(bulletRight).convert_alpha()
    game_sprites["bricks-3"] = pygame.image.load(bricks3).convert_alpha()
    game_sprites["flag"] = pygame.image.load(flag).convert_alpha()
    game_sprites["lever"] = pygame.image.load(lever).convert_alpha()
    game_sprites["lever-pull"] = pygame.image.load(leverPull).convert_alpha()
    game_sprites["flag-lift"] = pygame.image.load(flagLift).convert_alpha()
    game_sprites["drag1"] = pygame.image.load(drag1).convert_alpha()
    game_sprites["drag2"] = pygame.image.load(drag2).convert_alpha()
    game_sprites["drag3"] = pygame.image.load(drag3).convert_alpha()
    game_sprites["drag4"] = pygame.image.load(drag4).convert_alpha()
    game_sprites["drag5"] = pygame.image.load(drag5).convert_alpha()
    game_sprites["drag6"] = pygame.image.load(drag6).convert_alpha()
    game_sprites["drag7"] = pygame.image.load(drag7).convert_alpha()
    game_sprites["drag8"] = pygame.image.load(drag8).convert_alpha()
    game_sprites["drag9"] = pygame.image.load(drag9).convert_alpha()
    game_sprites["drag10"] = pygame.image.load(drag10).convert_alpha()
    game_sprites["drag11"] = pygame.image.load(drag11).convert_alpha()
    game_sprites["drag12"] = pygame.image.load(drag12).convert_alpha()
    game_sprites["drag13"] = pygame.image.load(drag13).convert_alpha()
    game_sprites["drag14"] = pygame.image.load(drag14).convert_alpha()
    game_sprites["drag15"] = pygame.image.load(drag15).convert_alpha()
    game_sprites["drag16"] = pygame.image.load(drag16).convert_alpha()
    game_sprites["drag17"] = pygame.image.load(drag17).convert_alpha()
    game_sprites["fire"] = pygame.image.load(fire).convert_alpha()
    game_sprites["fire2"] = pygame.image.load(fire2).convert_alpha()
    game_sprites["end"] = pygame.image.load(end).convert_alpha()
    game_sprites["crusher1"] = pygame.image.load(crusher).convert_alpha()
    game_sprites["crusher2"] = pygame.image.load(crusher).convert_alpha()
    game_sprites["crusher3"] = pygame.image.load(crusher).convert_alpha()
    game_sprites["restart"] = pygame.image.load(restart).convert_alpha()

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
