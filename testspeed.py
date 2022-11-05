import pygame

pygame.init()
pygame.display.set_mode((400, 300))

key_pressed = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print("This should be zero!", key_pressed)
            raise SystemExit()

        if event.type == pygame.KEYDOWN:
            key_pressed += 1
            print(event)

        if event.type == pygame.KEYUP:
            key_pressed -= 1
            print(event)