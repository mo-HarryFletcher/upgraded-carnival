import pygame
from colour import colour as all_colours

class image:
    all_images = []
    graphics_path = "graphics"
    fonts_path = "fonts"

    def __init__(
        self, size: tuple[int, int],
        position: tuple[int, int],
        colour: all_colours,
        graphic_file_name: str=None,
        text: str=None,
        font_name: pygame.font.Font=None,
        font_size: int=1,
    ) -> None:
        """
        An image to be displayed on the screen

        Args:
            size (tuple[int, int]): the size of the image (width, height)
            position (tuple[int, int]): the position of the image on the screen (x, y)
            colour (colour): colour of the image
        """

        self.width: int = size[0]
        self.height: int = size[1]

        self.x: int = position[0]
        self.y: int = position[1]

        self.text = None
        self.text_font = None
        self.graphic = None
        self.colour = all_colours.BLACK

        if text != None:
            self.text = text
            self.font_name = font_name
            self.font_size = font_size
        elif graphic_file_name != None:
            self.graphic = graphic_file_name

        self.colour: colour = colour

        # Add image to list of all instances of image
        image.add_image(self)

    def size(self) -> tuple[int, int]:
        return self.width, self.height

    def position(self) -> tuple[int, int]:
        return self.x, self.y

    def move(self, movement :tuple[int, int]) -> None:
        """
        Args:
            movement (tuple[int, int]): change in position (x, y)
        """
        self.x += movement[0]
        self.y += movement[1]

    def add_image(new_image):
        image.all_images.append(new_image)

    def is_image(self):
        return self.graphic != None

    def is_text(self):
        return self.text != None

    def display_colour(self):
        surface = pygame.Surface(self.size())
        surface.fill(self.colour)

        return surface
    
    def display_image(self):
        return pygame.image.load(f"{image.graphics_path}/{self.graphic}")
    
    def display_text(self):
        font = pygame.font.Font(f"{image.fonts_path}/{self.font_name}", self.font_size)
        return font.render(self.text, True, self.colour)

    def get_surface(self):
        if self.is_text():
            surface = self.display_text()
        elif self.is_image():
            surface = self.display_image()
        else:
            surface = self.display_colour()

        return surface

    def draw(self, screen):
        screen.blit(
            self.get_surface(),
            self.position()
        )

    def blit_all(screen):
        for image_instance in image.all_images:
            image_instance.draw(screen)

