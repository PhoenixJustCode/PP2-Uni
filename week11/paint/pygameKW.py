# key-words for Pygame
'''    NOT FOR UNIVERSITY LABS      '''


import pygame

# Инициализация Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Basics")
# pygame.display.set_icon(pygame.image.load("icon.png"))  # Устанавливает иконку окна

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Загрузка ресурсов
image = pygame.image.load("player.png")  # Загружаем картинку
sound = pygame.mixer.Sound("click.wav")  # Загружаем звук
pygame.mixer.music.load("background.mp3")  # Загружаем музыку
pygame.mixer.music.play(-1)  # Включаем музыку на повторе

# Создание шрифта
font = pygame.font.SysFont("Verdana", 30)

# Таймер
clock = pygame.time.Clock()

# Координаты объекта
x, y = 100, 100
speed = 5

running = True
while running:
    screen.fill(WHITE)  # Очищаем экран

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound.play()

    # Управление стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Рисование фигур
    pygame.draw.line(screen, RED, (50, 50), (200, 200), 5)
    pygame.draw.rect(screen, BLUE, (x, y, 100, 150))
    pygame.draw.circle(screen, GREEN, (400, 300), 50)
    pygame.draw.polygon(screen, BLACK, [(300, 300), (350, 250), (400, 300)])

    # Отображение текста
    text = font.render("Привет, Pygame!", True, BLACK)
    screen.blit(text, (50, 50))

    # Отображение изображения
    screen.blit(image, (x, y))

    pygame.display.flip()  # Обновление экрана
    clock.tick(60)  # Ограничение FPS

pygame.quit()




'''
оБНОВЛЕНИЕ ЭКРАНА
pygame.display.flip()  # Полностью обновляет экран
pygame.display.update()  # Обновляет только измененные области экрана

🔹 Создание окна
screen = pygame.display.set_mode((800, 600))  # Создает окно размером 800x600 пикселей
pygame.display.set_caption("Моя игра")  # Устанавливает заголовок окна
pygame.display.set_icon(pygame.image.load("icon.png"))  # Устанавливает иконку окна


🔹 Работа с событиями
for event in pygame.event.get():  # Цикл обработки событий
    if event.type == pygame.QUIT:  # Закрытие окна
        running = False
    if event.type == pygame.KEYDOWN:  # Нажатие клавиши
        if event.key == pygame.K_SPACE:  # Проверка нажатия пробела
            print("Пробел нажат!")
    if event.type == pygame.MOUSEBUTTONDOWN:  # Нажатие кнопки мыши
        print("Клик мышью!", event.pos)  # Выводит координаты клика



🔹 Рисование фигур
pygame.draw.line(screen, RED, (100, 100), (200, 200), 5)  # Линия (цвет, начальная и конечная точка, толщина)
pygame.draw.rect(screen, BLUE, (50, 50, 100, 150))  # Прямоугольник (цвет, x, y, ширина, высота)
pygame.draw.circle(screen, GREEN, (400, 300), 50)  # Круг (цвет, центр, радиус)
pygame.draw.polygon(screen, BLACK, [(300, 300), (350, 250), (400, 300)])  # Многоугольник (цвет, список точек)




🔹 Работа со шрифтами
pygame.font.init()  # Инициализирует модуль шрифтов
font = pygame.font.SysFont("Verdana", 30)  # Загружает системный шрифт Verdana, размер 30
text = font.render("Привет, Pygame!", True, WHITE)  # Создает текст (антиалиасинг, цвет)
screen.blit(text, (50, 50))  # Отображает текст на экране по координатам (50, 50)


ИЗОБРАЖЕНИЕ
image = pygame.image.load("player.png")  # Загружает изображение
screen.blit(image, (100, 100))  # Отображает изображение в координатах (100, 100)


MOVE - ПЕРЕМЕЩЕНИЕ
x, y = 100, 100
speed = 5

keys = pygame.key.get_pressed()  # Получаем список всех нажатых клавиш
if keys[pygame.K_LEFT]:  # Если нажата стрелка влево
    x -= speed
if keys[pygame.K_RIGHT]:  # Если нажата стрелка вправо
    x += speed

    
    
MAIN LOOP
running = True
while running:
    for event in pygame.event.get():  # Обработка событий
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)  # Очищаем экран

    pygame.display.flip()  # Обновляем экран

pygame.quit()  # Выход из pygame



'''
