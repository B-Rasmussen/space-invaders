import pygame

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()

playerImg = pygame.image.load("images/PlayerTank.png")
player_width = 50

alienTypeOne = pygame.image.load("images/AlienTypeOne.png")
alien_width = 50



def player_tank(x,y):
    gameDisplay.blit(playerImg, (x, y))

def alien_type_one(x, y):
    gameDisplay.blit(alienTypeOne, (x, y))

def game_loop():
    # player movement and weapon
    player_x = (display_width * 0.45)
    player_y = (display_height * 0.8)
    player_weapon_x = player_x
    player_weapon_y = player_y

    player_x_change = 0

    alien_x = (display_width * 0.45)
    alien_y = (display_height * 0.2)


    land = False

    while not land:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player_x_change = -5
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player_x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player_x_change = 0
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        player_x = player_x + player_x_change

        gameDisplay.fill(white)

        player_tank(player_x, player_y)

        alien_type_one(alien_x, alien_y)

        if player_x > display_width - player_width or player_x < 0:
            player_x_change = 0

        if alien_y > 0:
            if alien_x > display_width - alien_width or alien_x < 0:
                alien_y = alien_y - 75



        pygame.display.update()
        clock.tick(30)

game_loop()
pygame.quit()
quit()