#Imports
import pygame
import random
import sys

#Intialise pygame
pygame.init()

#Define Screen Size
screen_size = (800, 600)

#Create Screen
screen = pygame.display.set_mode(screen_size)

# Define the grid size and cell size
grid_size = (40, 30)
cell_size = (screen_size[0] // grid_size[0], screen_size[1] // grid_size[1])

# Define the snake body
snake_body = [(grid_size[0] // 2, grid_size[1] // 2)]

# Define the food
food = (random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1))

# Define Snake's Speed & Initial Direction
snake_speed = 1
snake_direction = (1, 0)

#Define Gameloop
is_paused = False
clock = pygame.time.Clock()
game_over = False
