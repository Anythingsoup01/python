import pygame

def keycode(key, movement):
    match key:
        case pygame.K_LEFT: movement[0] = True
        case pygame.K_RIGHT: movement[1] = True
        




