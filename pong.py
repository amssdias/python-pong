import pygame

def ball_animation():
    global ball_speed_x, ball_speed_y, player_1_score, player_2_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.y >= screen_height or ball.y <= 0:
        ball_speed_y *= -1
    if ball.right >= screen_width:
        player_2_score += 1
        ball_restart()
    if ball.left <= 0:
        player_1_score += 1
        ball_restart()

    if ball.colliderect(player_1) or ball.colliderect(player_2):
        ball_speed_x *= -1


def player_animation():
    player_1.y += player_1_speed
    if player_1.top <= 0:
        player_1.top = 0
    if player_1.bottom >= screen_height:
        player_1.bottom = screen_height


def player_2_animation():
    if player_2.top < ball.y:
        player_2.top += player_2_speed
    if player_2.bottom > ball.y:
        player_2.bottom -= player_2_speed
    if player_2.top <= 0:
        player_2.top = 0
    if player_2.bottom >= screen_height:
        player_2.bottom = screen_height


def ball_restart():
    ball.center = (screen_width/2, screen_height/2)


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

# Set size of window
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Create rectangles
player_1 = pygame.Rect(0, (screen_height/2 - 75), 14, 150)
player_2 = pygame.Rect((screen_width - 14), (screen_height/2 - 75), 14, 150)
ball = pygame.Rect(screen_width/2 - 10, screen_height/2 - 10, 20, 20)

ball_speed_x = 4
ball_speed_y = 4
player_1_speed = 0
player_2_speed = 7

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

# Text variables
player_1_score = 0
player_2_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)


running = True
while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_1_speed = 5
            elif event.key == pygame.K_UP:
                player_1_speed = -5
        if event.type == pygame.KEYUP:
            player_1_speed = 0

    ball_animation()
    player_animation()
    player_2_animation()

    # Fill the screen with a background-color
    screen.fill(bg_color)

    # Draw into the screen
    pygame.draw.rect(screen, light_grey, player_1)
    pygame.draw.rect(screen, light_grey, player_2)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    player_1_text = game_font.render(f"{player_1_score}", False, light_grey)
    screen.blit(player_1_text, (screen_width/2 + 15, screen_height/2 - 16))

    player_2_text = game_font.render(f"{player_2_score}", False, light_grey)
    screen.blit(player_2_text, (screen_width/2 - 30, screen_height/2 - 16))

    # Updates the contents of the display to the screen
    pygame.display.flip()
    clock.tick(60)