import sys
import pygame

from scripts.tilemap import Tilemap
from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images


class Game():
    def __init__(self):

        #Initialize Pygame
        pygame.init()

        #Setting pygame variables

        pygame.display.set_caption('Ninja Game')
        self.window = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        self.assets = {
            'decor' : load_images('tiles/decor'),
            'grass' : load_images('tiles/grass'),
            'large_decor' : load_images('tiles/large_decor'),
            'stone' : load_images('tiles/stone'),
            'player': load_image('entities/player.png')
        }

        self.tilemap = Tilemap(self, tile_size=16)

        self.movement = [False, False, False, False]
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

    def run(self):
        #Render graphics & getting input
        while True:
            self.display.fill((14, 219, 248))         

            self.tilemap.render(self.display)

            self.player.update((self.movement[1] - self.movement[0], 0))
            self.player.render(self.display)

            print(self.tilemap.tiles_around(self.player.pos))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                #Want to make a dictionary to abstract these 
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_LEFT: self.movement[0] = True
                        case pygame.K_RIGHT: self.movement[1] = True
                if event.type == pygame.KEYUP:
                    match event.key:    
                        case pygame.K_LEFT: self.movement[0] = False
                        case pygame.K_RIGHT: self.movement[1] = False

            self.window.blit(pygame.transform.scale(self.display, self.window.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()


