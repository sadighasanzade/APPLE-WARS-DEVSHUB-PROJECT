#imports

import pygame
import os

PLAYER_YELLOW_MONSTER = 1
PLAYER_GREEN_MONSTER = 2

class Player(pygame.sprite.Sprite):

    def __init__(self,type) -> None:
        super().__init__()
        
        if(type == PLAYER_GREEN_MONSTER):
            self.image = pygame.image.load(os.path.abspath('apple wars project/static/player1.png'))
        else:
            self.image = pygame.image.load(os.path.abspath('apple wars project/static/player2.png'))

        self.rect = self.image.get_rect()
        self.delta_x = 0
        self.delta_y = 0
        self.has_apple = True

    def update(self) -> None:
        self.rect.x += self.delta_x
        self.rect.y += self.delta_y

    def move_left(self):
        self.delta_x = -10

    def move_right(self):
        self.delta_x = 10
    
    def move_up(self):
        self.delta_y = -10
    
    def move_down(self):
        self.delta_y = 10

    def stop(self):
        self.delta_y = 0
        self.delta_x = 0
    

def main():
    pygame.init()  
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800

    size = [SCREEN_WIDTH, SCREEN_HEIGHT]

    game_screen = pygame.display.set_mode(size)

    pygame.display.set_caption(" APPLE WARS ")

    active_sprite_list = pygame.sprite.Group()
    
    player = Player(PLAYER_GREEN_MONSTER)
 
    player.rect.x = 340
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)
 
    # Loop until the user clicks the close button.
    game_over = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                if event.key == pygame.K_RIGHT:
                    player.move_right()
                if event.key == pygame.K_UP:
                    player.move_up()
                
                if event.key == pygame.K_DOWN:
                    player.move_down()
 

 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.delta_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.delta_x > 0:
                    player.stop()

            active_sprite_list.update()
            game_screen.blit(pygame.image.load(os.path.abspath('apple wars project/static/bg.png')),(0,0))
            active_sprite_list.draw(game_screen)
            clock.tick(60)

            pygame.display.flip()

if __name__ == "__main__":
    main()