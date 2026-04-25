import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-понг")

BG_COLOR = (30, 30, 30)
PADDLE_COLOR = (200, 200, 200)
BALL_COLOR = (255, 100, 100)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20

PADDLE_SPEED = 5
BALL_SPEED = 4

left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - PADDLE_WIDTH - 10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_dx, ball_dy = BALL_SPEED, BALL_SPEED

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_e] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_d] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    ball.x += ball_dx
    ball.y += ball_dy

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy

    if ball.colliderect(left_paddle) and ball_dx < 0:
        ball_dx = -ball_dx
    if ball.colliderect(right_paddle) and ball_dx > 0:
        ball_dx = -ball_dx

    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx = BALL_SPEED * (-1 if ball_dx > 0 else 1)


    WIN.fill(BG_COLOR)
    pygame.draw.rect(WIN, PADDLE_COLOR, left_paddle)
    pygame.draw.rect(WIN, PADDLE_COLOR, right_paddle)
    pygame.draw.ellipse(WIN, BALL_COLOR, ball)

    pygame.display.flip()
    clock.tick(60)
