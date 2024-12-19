import os
import sys
import pygame
from random import randrange

def main():
    # pygame setup
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)
    # Начинаем добавлять спрайты
    all_sprites = pygame.sprite.Group()
    image = load_image("bomb.png")
    for _ in range(100):
        sprite = pygame.sprite.Sprite(all_sprites)
        sprite.image = image
        sprite.rect = sprite.image.get_rect()
        sprite.rect.x = randrange(width)
        sprite.rect.y = randrange(height)
        all_sprites.add(sprite)

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
        # RENDER YOUR GAME HERE
        screen.fill("purple")
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()  # создаёт новую копию изображения с таким же форматом пикселей, как у экрана
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()  # метод для преобразования изображения с сохранением информации о прозрачности
    return image


if __name__ == '__main__':
    main()
