import pygame
import os

# Инициализация Pygame и микшера
pygame.init()
pygame.mixer.init()

# Настройки окна
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]  
current_track = 0


def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()


def stop_music():
    pygame.mixer.music.stop()


def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()


def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_music()
            elif event.key == pygame.K_s:  # Stop
                stop_music()
            elif event.key == pygame.K_n:  # Next track
                next_track()
            elif event.key == pygame.K_b:  # Previous track
                prev_track()

pygame.quit()
