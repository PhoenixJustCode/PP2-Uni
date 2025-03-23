import pygame
import random
from color_palette import *

pygame.init()

# Размеры экрана и ячейки
WIDTH, HEIGHT = 600, 600
CELL = 30

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Шрифты
font = pygame.font.SysFont("Verdana", 20)

# Функция отрисовки шахматной сетки


def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(WIDTH // CELL):
        for j in range(HEIGHT // CELL):
            pygame.draw.rect(
                screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 1, 0
        self.score = 0
        self.level = 1
        self.speed = 5

    def move(self):
        new_x = self.body[0].x + self.dx
        new_y = self.body[0].y + self.dy

        # Проверка выхода за границы экрана
        if new_x < 0 or new_x >= WIDTH // CELL or new_y < 0 or new_y >= HEIGHT // CELL:
            return False

        # Проверка столкновения с самим собой
        for segment in self.body:
            if new_x == segment.x and new_y == segment.y:
                return False

        self.body.insert(0, Point(new_x, new_y))
        self.body.pop()
        return True

    def grow(self):
        tail = self.body[-1]
        self.body.append(Point(tail.x, tail.y))
        self.score += 1
        if self.score % 3 == 0:  # Уровень повышается каждые 3 очка
            self.level += 1
            self.speed += 1

    def draw(self):
        pygame.draw.rect(
            screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW,
                             (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow()
            return True
        return False


class Food:
    def __init__(self, snake):
        self.generate_random_position(snake)

    def generate_random_position(self, snake):
        while True:
            self.pos = Point(random.randint(0, (WIDTH // CELL) - 1),
                             random.randint(0, (HEIGHT // CELL) - 1))
            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x *
                         CELL, self.pos.y * CELL, CELL, CELL))


# Инициализация объектов
snake = Snake()
food = Food(snake)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    draw_grid_chess()

    if not snake.move():
        running = False  # Остановка игры при столкновении

    if snake.check_collision(food):
        food.generate_random_position(snake)

    snake.draw()
    food.draw()

    # Отображение счета и уровня
    score_text = font.render(f"Score: {snake.score}", True, colorBLACK)
    level_text = font.render(f"Level: {snake.level}", True, colorBLACK)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(snake.speed)

pygame.quit()
