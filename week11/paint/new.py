import pygame
import math

pygame.init()

# Горячие клавиши:
# 1 – Линия
# 2 – Прямоугольник
# 3 – Круг
# 4 – Квадрат
# 5 – Прямоугольный треугольник
# 6 – Равносторонний треугольник
# 7 – Ромб
# E – Ластик
# R – Красный цвет
# B – Синий цвет
# K – Черный цвет
# + – Увеличить толщину
# - – Уменьшить толщину

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Переменные состояния
drawing = False
tool = "line"  # "line", "rect", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus", "eraser"
color = BLACK
thickness = 5
start_pos = (0, 0)

# Фоновый слой
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(WHITE)

running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Обработка выбора инструмента и цвета
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                tool = "line"
            elif event.key == pygame.K_2:
                tool = "rect"
            elif event.key == pygame.K_3:
                tool = "circle"
            elif event.key == pygame.K_4:
                tool = "square"
            elif event.key == pygame.K_5:
                tool = "right_triangle"
            elif event.key == pygame.K_6:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_7:
                tool = "rhombus"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK
            elif event.key == pygame.K_EQUALS:
                thickness += 1
            elif event.key == pygame.K_MINUS and thickness > 1:
                thickness -= 1

        # Обработка рисования
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                end_pos = event.pos
                if tool == "line":
                    pygame.draw.line(background, color,
                                     start_pos, end_pos, thickness)
                elif tool == "rect":
                    pygame.draw.rect(background, color, pygame.Rect(
                        *start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), thickness)
                elif tool == "circle":
                    radius = int(
                        math.sqrt((end_pos[0] - start_pos[0])**2 + (end_pos[1] - start_pos[1])**2))
                    pygame.draw.circle(background, color,
                                       start_pos, radius, thickness)
                elif tool == "square":
                    side = min(abs(end_pos[0] - start_pos[0]),
                               abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(
                        background, color, (start_pos[0], start_pos[1], side, side), thickness)
                elif tool == "right_triangle":
                    pygame.draw.polygon(background, color, [
                                        start_pos, (start_pos[0], end_pos[1]), (end_pos[0], end_pos[1])], thickness)
                elif tool == "equilateral_triangle":
                    height = (end_pos[1] - start_pos[1])
                    base = height * math.sqrt(3)
                    pygame.draw.polygon(background, color, [
                                        start_pos, (start_pos[0] + base / 2, end_pos[1]), (start_pos[0] - base / 2, end_pos[1])], thickness)
                elif tool == "rhombus":
                    center_x, center_y = start_pos
                    width, height = abs(
                        end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(background, color, [(center_x, center_y - height // 2), (center_x + width //
                                        2, center_y), (center_x, center_y + height // 2), (center_x - width // 2, center_y)], thickness)
                elif tool == "eraser":
                    pygame.draw.circle(background, WHITE, start_pos, thickness)
                drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "eraser":
                pygame.draw.circle(background, WHITE, event.pos, thickness)

    pygame.display.flip()

pygame.quit()
