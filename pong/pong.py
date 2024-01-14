import pygame
pygame.init()

# VARS
WINDOW_BGCOLOR = (0, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
BORDER_COLOR = (0, 255, 0)
BORDER_WIDTH = 20

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

top_border = pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(
    0, 0, WINDOW_WIDTH, BORDER_WIDTH))
bottom_border = pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(
    0, WINDOW_HEIGHT - BORDER_WIDTH, WINDOW_WIDTH, BORDER_WIDTH))
left_border = pygame.draw.rect(screen, BORDER_COLOR, pygame.Rect(
    0, 0, BORDER_WIDTH, WINDOW_HEIGHT))


class Ball:

    def __init__(self, surface, center, radius, velocity, color):
        self.surface = surface
        self.center = center
        self.radius = radius
        self.vel_x = self.vel_y = velocity
        self.color = color
        self.draw(self.center, self.color)

    def draw(self, center, color):
        pygame.draw.circle(self.surface, color, center, self.radius)

    def move(self):
        global paddle
        self.draw(self.center, WINDOW_BGCOLOR)
        to_move_x = self.center[0] - self.vel_x
        to_move_y = self.center[1] - self.vel_y

        to_remove_dot = 0.1
        if to_move_y < top_border.height + self.radius + to_remove_dot:
            self.vel_y = -self.vel_y
        if to_move_y > bottom_border.y - self.radius - to_remove_dot:
            self.vel_y = -self.vel_y
        if to_move_x < left_border.width + self.radius + to_remove_dot:
            self.vel_x = -self.vel_x
        if paddle.y < to_move_y < paddle.y + paddle.height and to_move_x > paddle.x - self.radius:
            self.vel_x = -self.vel_x

        self.draw((to_move_x, to_move_y), self.color)
        self.center = (to_move_x, to_move_y)


class Paddle:

    def __init__(self, surface, x, y, width, height, color):
        self.surface = surface
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.draw(self.x, self.y, self.color)

    def draw(self, x, y, color):
        pygame.draw.rect(self.surface, color, pygame.Rect(
            x, y, self.width, self.height))

    def update(self):
        y = pygame.mouse.get_pos()[1]
        upper_bound = top_border.height + self.height//2
        lower_bound = bottom_border.y - self.height // 2
        if y <= upper_bound:
            y = upper_bound
        elif y >= lower_bound:
            y = lower_bound

        self.draw(self.x, self.y, WINDOW_BGCOLOR)
        y = y - self.height//2
        self.draw(self.x, y, self.color)
        self.y = y


ball = Ball(screen, (900, WINDOW_HEIGHT // 2), 20, 1, (255,) * 3)

paddle_width = 20
paddle_height = 150
paddle_x = WINDOW_WIDTH - paddle_width - 15
paddle_y = WINDOW_HEIGHT//2 - paddle_height//2
paddle = Paddle(screen, paddle_x, paddle_y, paddle_width,
                paddle_height, (231, 255, 15))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    paddle.update()

    ball.move()

    pygame.display.flip()
