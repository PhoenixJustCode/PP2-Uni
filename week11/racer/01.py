import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Размеры окна
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Загрузка изображений и их масштабирование
image_background = pygame.image.load('resources/AnimatedStreet.png')
image_background = pygame.transform.scale(image_background, (WIDTH, HEIGHT))
image_player = pygame.image.load('resources/Player.png')
image_player = pygame.transform.scale(image_player, (50, 100))
image_enemy = pygame.image.load('resources/Enemy.png')
image_enemy = pygame.transform.scale(image_enemy, (50, 100))
image_coin = pygame.image.load('resources/Coin.png')
image_coin = pygame.transform.scale(image_coin, (30, 30))

# Звуки
pygame.mixer.music.load('resources/background.wav')
pygame.mixer.music.play(-1)
sound_crash = pygame.mixer.Sound('resources/crash.wav')

# Шрифт для отображения очков
font = pygame.font.SysFont("Verdana", 30)

# Количество монет для ускорения врага
COINS_FOR_SPEEDUP = 5  # После сбора 5 монет враг становится быстрее


class Player(pygame.sprite.Sprite):
    """Класс игрока (машина)"""

    def __init__(self):
        super().__init__()
        self.image = image_player
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 70))
        self.speed = 5
        self.coins_collected = 0  # Счетчик монет

    def move(self):
        """Движение игрока влево и вправо"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        self.rect.clamp_ip(screen.get_rect())  # Ограничение внутри экрана


class Enemy(pygame.sprite.Sprite):
    """Класс врага (другая машина)"""

    def __init__(self):
        super().__init__()
        self.image = image_enemy
        self.rect = self.image.get_rect()
        self.speed = 7  # Начальная скорость врага
        self.generate_random_rect()

    def generate_random_rect(self):
        """Генерация новой позиции для врага"""
        self.rect.left = random.randint(0, max(0, WIDTH - self.rect.w))
        self.rect.bottom = 0

    def move(self):
        """Движение врага вниз"""
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


class Coin(pygame.sprite.Sprite):
    """Класс монеты"""

    def __init__(self):
        super().__init__()
        self.image = image_coin
        self.rect = self.image.get_rect()
        self.speed = 3  # Скорость падения монеты
        self.value = random.choice([1, 2, 3])  # Разный вес монет
        self.generate_random_rect()

    def generate_random_rect(self):
        """Генерация новой позиции монеты"""
        self.rect.left = random.randint(0, max(0, WIDTH - self.rect.w))
        self.rect.bottom = 0
        self.value = random.choice([1, 2, 3])  # Генерация нового веса монеты

    def move(self):
        """Движение монеты вниз"""
        self.rect.move_ip(0, self.speed)
        if self.rect.top > HEIGHT:
            self.generate_random_rect()


# Основной цикл игры
running = True
clock = pygame.time.Clock()
FPS = 60

# Создание игровых объектов
player = Player()
enemy = Enemy()
coin = Coin()

# Группы спрайтов
all_sprites = pygame.sprite.Group(player, enemy, coin)
enemy_sprites = pygame.sprite.Group(enemy)
coin_sprites = pygame.sprite.Group(coin)

while running:
    # Проверка событий (закрытие окна)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Движение объектов
    player.move()
    enemy.move()
    coin.move()

    # Отображение фона
    screen.blit(image_background, (0, 0))

    # Отрисовка всех спрайтов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Проверяем столкновение с врагом
    if pygame.sprite.spritecollideany(player, enemy_sprites):
        sound_crash.play()
        time.sleep(1)
        running = False
        screen.fill("red")
        game_over_text = font.render("Game Over", True, "black")
        screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(3)

    # Проверяем сбор монеты
    if pygame.sprite.spritecollideany(player, coin_sprites):
        player.coins_collected += coin.value  # Добавляем вес монеты
        coin.generate_random_rect()

        # Увеличение скорости врага
        if player.coins_collected % COINS_FOR_SPEEDUP == 0:
            enemy.speed += 1  # Каждые 5 монет враг становится быстрее

    # Отображаем количество монет
    coin_text = font.render(f"Coins: {player.coins_collected}", True, "blue")
    screen.blit(coin_text, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
