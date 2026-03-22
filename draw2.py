# задание 3

import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Уровень 3: Творчество и Прозрачность')

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (139, 69, 19)
SKY_BLUE = (135, 206, 235)
ORANGE = (255, 165, 0)

DISPLAY_SURF.fill(SKY_BLUE) # Фон - небо

# ЗАДАНИЕ: Домик (комбинация примитивов)
# Основание дома (квадрат)
pygame.draw.rect(DISPLAY_SURF, (200, 200, 200), (50, 200, 150, 150))
# Крыша (треугольник через polygon)
pygame.draw.polygon(DISPLAY_SURF, BROWN, ((40, 200), (210, 200), (125, 120)))
# Дверь (прямоугольник)
pygame.draw.rect(DISPLAY_SURF, BLACK, (100, 270, 40, 80))
# Окно (круг)
pygame.draw.circle(DISPLAY_SURF, WHITE, (125, 230), 15)

# ЗАДАНИЕ: Снеговик
# Тело (три круга)
pygame.draw.circle(DISPLAY_SURF, WHITE, (350, 300), 50) # Нижний
pygame.draw.circle(DISPLAY_SURF, WHITE, (350, 230), 35) # Средний
pygame.draw.circle(DISPLAY_SURF, WHITE, (350, 180), 25) # Голова
# Глаза
pygame.draw.circle(DISPLAY_SURF, BLACK, (340, 175), 3)
pygame.draw.circle(DISPLAY_SURF, BLACK, (360, 175), 3)
# Нос (линия или маленький полигон)
pygame.draw.line(DISPLAY_SURF, ORANGE, (350, 180), (370, 185), 3)

# ЗАДАНИЕ: Работа с прозрачностью (Альфа-канал)

# 1. Создаем специальную поверхность такого же размера, как окно
# Флаг SRCALPHA позволяет использовать 4-е число в цвете (прозрачность)
alpha_surf = pygame.Surface((500, 400), pygame.SRCALPHA)

# 2. Рисуем два пересекающихся круга с прозрачностью (128 - это 50% прозрачности)
# Цвет: (R, G, B, Alpha)
pygame.draw.circle(alpha_surf, (255, 0, 0, 150), (100, 80), 40) # Красный
pygame.draw.circle(alpha_surf, (0, 0, 255, 0), (140, 80), 40) # Синий

# 3. Накладываем прозрачную поверхность на основное окно
DISPLAY_SURF.blit(alpha_surf, (0, 0))

# ГЛАВНЫЙ ЦИКЛ
while True:
   for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
   pygame.display.update()
