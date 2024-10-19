import pygame
import time
import random

snake_speed = 15

# Application window size
window_x = 720
window_y = 480

# Define colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)  # Fruit color
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize pygame
pygame.init()

# Initialize window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS controller
fps = pygame.time.Clock()

# Define initial snake position
snake_position = [100, 50]

# Define initial snake body
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Fruit position
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Default snake direction (right)
direction = 'RIGHT'
change_to = direction

# Init score
score = 0

# Function for displaying the score
def show_score(choice, color, font, size, score):
    # Font object
    score_font = pygame.font.SysFont(font, size)

    # Display for surface object
    score_surface = score_font.render('Score: ' + str(score), True, color)

    # Text rectangle surface object
    score_rect = score_surface.get_rect()

    # Display text
    game_window.blit(score_surface, score_rect)

# Function for game over
def game_over():
    # Create font object
    my_font = pygame.font.SysFont('times new roman', 50)

    # Create a text surface
    game_over_surface = my_font.render('Your score is: ' + str(score), True, red)

    # Create rectangle object for text
    game_over_rect = game_over_surface.get_rect()

    # Setting position of text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # Blit will draw text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # After 2 seconds we will quit the program
    time.sleep(2)

    # Deactivate pygame library
    pygame.quit()

    # Quit the program
    quit()

# The main function!
def main():
    global change_to, direction, score, fruit_spawn, fruit_position, snake_body, snake_position

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # Snake direction logic
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Move the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Growing mechanics for the snake
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        # Fruit spawning
        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                              random.randrange(1, (window_y // 10)) * 10]
            fruit_spawn = True

        # Drawing
        game_window.fill(black)  # Fill the game window with black
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        # Drawing the fruit in red
        pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
        
        # Game over conditions
        if (snake_position[0] < 0 or snake_position[0] > window_x - 10 or
            snake_position[1] < 0 or snake_position[1] > window_y - 10):
            game_over()

        # Check collision with self
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # Displaying score
        show_score(1, white, 'times new roman', 20, score)

        # Refresh game screen
        pygame.display.update()
        fps.tick(snake_speed)

if __name__ == "__main__":
    main()
