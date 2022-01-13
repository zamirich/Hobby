import pygame
import time
import random
from pygame.locals import *

block_size = 17

class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("Snake/block17_17.jpg").convert()
        self.parent_screen = parent_screen
        self.x = block_size*4
        self.y = block_size*4


    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))
        pygame.display.update()
        
    
    def move(self):
        self.x = random.randint(1,39)*block_size
        self.y = random.randint(1,39)*block_size
        
        
class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("Snake/block17_17b.jpg").convert()
        self.x = [block_size]*length
        self.y = [block_size]*length
        self.direction = 'down'
    
    
    def draw(self):
        self.parent_screen.fill((20, 92, 21))
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.update()
        
    
    def walk(self):
        
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        if self.direction == 'up':
            self.y[0] -= block_size
        if self.direction == 'down':
            self.y[0] += block_size
        if self.direction == 'left':
            self.x[0] -= block_size
        if self.direction == 'right':
            self.x[0] += block_size
        
        self.draw()
    
    
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)
    
    def move_left(self):
        self.direction = 'left'
        self.draw()
        
    def move_right(self):
        self.direction = 'right'
        self.draw()
        
    def move_up(self):
        self.direction = 'up'
        self.draw()

    def move_down(self):
        self.direction = 'down'
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((680,680))
        self.surface.fill((20, 92, 21))
        self.snake = Snake(self.surface, 3)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()
        
    
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + block_size:
            if y1 >= y2 and y1 < y2 + block_size:
                return True
        return False
        
    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.update()
        
        if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()
            time.sleep(0.1) #TODO
       
       
    def display_score(self):
        font = pygame.font.SysFont('arial',20)
        score = font.render(f"Score: {self.snake.length-3}", True, (200,200,200))    
        self.surface.blit(score, (550,10))
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE: 
                        running = False
                    if event.key == K_UP: 
                        self.snake.move_up()
                    if event.key == K_DOWN: 
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT: 
                        self.snake.move_right()
                elif event.type == QUIT:
                    running = False
        
            self.play()
            
            time.sleep(.3)

if __name__ == "__main__":
    game = Game()
    game.run()
    