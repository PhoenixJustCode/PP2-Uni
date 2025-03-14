import pygame

import pygame
import math
import time

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

# Загрузка изображения Микки
mickey = pygame.image.load("mickey.png")
mickey = pygame.transform.scale(mickey, (300, 300))
clock_center = (WIDTH // 2, HEIGHT // 2)

minute_hand = pygame.image.load("right_hand.png")  # Стрелка минут
second_hand = pygame.image.load("left_hand.png")  # Стрелка секунд



def rotate_hand(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect


running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(mickey, (clock_center[0] - 150, clock_center[1] - 150))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    min_angle = - (minutes * 6)  # 360/60 = 6 градусов на минуту
    sec_angle = - (seconds * 6)  # 360/60 = 6 градусов на секунду

    # Отображение стрелок
    rotated_min_hand, min_rect = rotate_hand(
        minute_hand, min_angle, clock_center)
    rotated_sec_hand, sec_rect = rotate_hand(
        second_hand, sec_angle, clock_center)

    screen.blit(rotated_min_hand, min_rect.topleft)
    screen.blit(rotated_sec_hand, sec_rect.topleft)

    pygame.display.flip()
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
