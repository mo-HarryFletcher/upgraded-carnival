import pygame
from image import image

class game_object:
    all_game_objects = []

    def __init__(self, name: str, image: image) -> None:
        self.name = name
        self.go_image = image

        self.x = 50
        self.y = 50
        self.width = 100
        self.height = 100
        

    def move(self, movement: tuple[int, int]) -> None:
        self.x += movement[0]
        self.y += movement[1]

        self.go_image.update_position(self.x, self.y)

