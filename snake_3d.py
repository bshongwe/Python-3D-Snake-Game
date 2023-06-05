# 1. Import Modules
import pygame
import random
import sys



# 2.0 Screen Settings
# 2.1 Initialise pygame
pygame.init()

# 2.2 Define Screen Size
screen_size = (800, 600)

# 2.3 Create Screen
screen = pygame.display.set_mode(screen_size)

# 2.4 Define Grid (size & cell size)
grid_size = (40, 30)
cell_size = (screen_size[0] // grid_size[0], screen_size[1] // grid_size[1])



# 3.0 Game Item Settings
# 3.1 Define Snake Body
snake_body = [(grid_size[0] // 2, grid_size[1] // 2)]

# 3.2 Define Food
food = (random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1))

# 3.3 Define Snake's Speed & Initial Direction
snake_speed = 1
snake_direction = (1, 0)



#4.0 Gameplay Settings
# 4.1 Define Game Loop Settings
is_paused = False
clock = pygame.time.Clock()
game_over = False

while not game_over:

    # 4.2 Events' Handler
    for event in pygame.event.get():
        # 4.2.1 Exit Game if User Quits
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# 4.2 User Key Checker
        # 4.2.1 Direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

        # 4.2.2 User Pause Game" button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # 4.2.2.1 Pause or resume the game
                is_paused = not is_paused

        # 4.2.3 Check if the user clicked the "quit game" button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
                # Quit the game
                pygame.quit()
                sys.exit()

    # 4.2.4 Move the snake
    if not is_paused and not game_over:
        snake_head = snake_body[-1]
        snake_head = (snake_head[0] + snake_speed * snake_direction[0],
                      snake_head[1] + snake_speed * snake_direction[1])
        snake_body.append(snake_head)

        # 4.2.4.1 Check if the snake has hit the food
        if snake_head == food:
            # 4.2.4.1.2 Generate new food
            while True:
                food = (random.randint(0, grid_size[0] - 1), random.randint(0, grid_size[1] - 1))
                if food not in snake_body:
                    break
        else:
            snake_body.pop(0)

        # 4.2.4.2 Check if the snake has hit itself or the wall
        if (snake_head[0] < 0 or snake_head[0] >= grid_size[0] or
                snake_head[1] < 0 or snake_head[1] >= grid_size[1] or
                snake_head in snake_body[:-1]):
            game_over = True

            
            
    # 5.0 Clear the screen
    screen.fill((0, 0, 0))

    
    
    # 6.0 Graphics
    # 6.1 Draw Snake
    for segment in snake_body:
        pygame.draw.rect(screen, (255, 0, 0),
                         (segment[0] * cell_size[0], segment[1] * cell_size[1], cell_size[0], cell_size[1]))
                
    # 6.2 Draw Food
    pygame.draw.rect(screen, (0, 255, 0),
                     (food[0] * cell_size[0], food[1] * cell_size[1], cell_size[0], cell_size[1]))
      
    # 6.3 Draw the "pause game" button
    if is_paused:
        pygame.draw.rect(screen, (255, 0, 0), (0, 0, 100, 50))
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Resume", True, (255, 255, 255))
        screen.blit(text_surface, (25, 25))

    # 6.4 Draw the "quit game" button
    pygame.draw.rect(screen, (255, 0, 0), (screen_size[0] - 100, 0, 100, 50))
    font = pygame.font.Font(None, 36)
    text_surface = font.render("Quit", True, (255, 255, 255))
    screen.blit(text_surface, (screen_size[0] - 60, 25))

    # 6.5 Update the display
    pygame.display.update()
 
    # 6.7 Limit the frame rate
    clock.tick(10)  # Adjust the frame rate to control the speed of the game

    

# 7.0 Quit Function
# 7.1 Game over screen
screen.fill((0, 0, 0))
font = pygame.font.Font(None, 72)
text_surface = font.render("Game Over", True, (255, 255, 255))
text_rect = text_surface.get_rect(center=(screen_size[0] // 2, screen_size[1] // 2))
screen.blit(text_surface, text_rect)
pygame.display.update()

# 7.2 Wait for a few seconds before quitting
pygame.time.wait(3000)

# 7.3 Quit the game
pygame.quit()
sys.exit()
