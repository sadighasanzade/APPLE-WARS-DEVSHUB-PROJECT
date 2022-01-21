#imports

import pygame
import os

from pygame.display import flip

PLAYER_YELLOW_MONSTER = 1
PLAYER_GREEN_MONSTER = 2

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

class Player(pygame.sprite.Sprite):

    def __init__(self,type) -> None:
        super().__init__()
        self.type = type
        
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
        self.stop()

    def move_left(self):
        if self.rect.x > 0:
            self.delta_x = -10

    def move_right(self):
        if self.rect.x< SCREEN_WIDTH - 128:
            self.delta_x = 10
    
    def move_up(self):
        if self.rect.y > 0:
            self.delta_y = -10
    
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT  - 128:
            self.delta_y = 10

    def stop(self):
        self.delta_y = 0
        self.delta_x = 0

class Apple(pygame.sprite.Sprite):


    # TODO: any better practice ?
    def __init__(self, player : Player, enemy: Player) -> None:
        super().__init__()
        
        self.image = pygame.image.load(os.path.abspath('apple wars project/static/apple.png'))
        self.player = player
        self.rect = self.image.get_rect()
        self.delta_x = 0
        self.is_throwed = False
        self.enemy = enemy
        self.isShooted = False
        self.delta_y = 2
        if(self.player.type == PLAYER_GREEN_MONSTER):
            self.delta_x = 20
        else:
            self.delta_x = -20

    def update(self) -> None:
        if not self.is_throwed:
            self.rect.x = self.player.rect.x + 32
            self.rect.y = self.player.rect.y + 32
            pass
        else:
            self.rect.x += self.delta_x
            self.rect.y += self.delta_y

        if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
            self.reset()
        elif self.rect.y> SCREEN_HEIGHT or self.rect.y<0:
            self.reset()
        hit = pygame.sprite.collide_rect(self, self.enemy)
        if hit:
            # TODO set game over screen instead of print
            print(Player, "is winner")
            self.isShooted = True
        
    def throw(self):
        if(self.player.type == PLAYER_GREEN_MONSTER):
            self.delta_x = 20
        else:
            self.delta_x = -20
        self.delta_y = 2
        self.is_throwed = True


    def reset(self):
        self.delta_x = 0
        self.delta_y = 0
        self.rect.x = self.player.rect.x + 32
        self.rect.y = self.player.rect.y + 32
        self.is_throwed = False
    

def main():
    pygame.init()  


    size = [SCREEN_WIDTH, SCREEN_HEIGHT]

    game_screen = pygame.display.set_mode(size)

    pygame.display.set_caption(" APPLE WARS ")

    active_sprite_list = pygame.sprite.Group()
    
    player = Player(PLAYER_GREEN_MONSTER)
    player2 = Player(PLAYER_YELLOW_MONSTER)
 
    player.rect.x = 100
    player.rect.y = SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    
    player2.rect.x = 700
    player2.rect.y = SCREEN_HEIGHT - player2.rect.height
    active_sprite_list.add(player2)

    apple1 = Apple(player, player2)
    apple2 = Apple(player2, player)

    active_sprite_list.add(apple1)
    active_sprite_list.add(apple2)

 
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
                
                if event.key == pygame.K_p:
                    apple1.throw()
                if event.key == pygame.K_q:
                    apple2.throw()
                
                if event.key == pygame.K_a:
                    player2.move_left()
                if event.key == pygame.K_d:
                    player2.move_right()
                if event.key == pygame.K_w:
                    player2.move_up()
                
                if event.key == pygame.K_s:
                    player2.move_down()                
                    
 

 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.delta_x < 0:
                    player.stop()
                    player2.stop()
                if event.key == pygame.K_RIGHT and player.delta_x > 0:
                    player.stop()
                    player2.stop()

            if(apple1.isShooted or apple2.isShooted):
                game_over = True

        active_sprite_list.update()
        game_screen.blit(pygame.image.load(os.path.abspath('apple wars project/static/bg.png')),(0,0))
        active_sprite_list.draw(game_screen)
        clock.tick(60)

        pygame.display.flip()

if __name__ == "__main__":
    main()