import pygame
from sys import exit
from colour import colour
from image import image
from game_object import game_object

class game_manager:
    def __init__(self) -> None:
        self.initialize()
        self.game_loop()

    def setup_variables(self):
        self.window_width = 800
        self.window_height = 400

        self.framerate = 60
        self.font_size = 50

    def initialize(self) -> None:
        pygame.init()
        
        self.setup_variables()

        # Display screen
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))

        # Set window text
        pygame.display.set_caption('Example Name')

        # Create clock
        self.clock = pygame.time.Clock()

        # Create surface
        backgroud = image(
            size=(self.window_width, self.window_height),
            position=(0, 0),
            colour=colour.BLACK,
            graphic_file_name="grid.png"
        )

        player = game_object()
        
        image(
            size=(100, 100),
            position=(50, 100),
            colour=colour.CYAN,
            graphic_file_name="grid.png"
        )
        image(
            size=(50, 50),
            position=(0,0 ),
            colour=colour.BLUE
        )
        self.text_image = image(
            size=(300, 10),
            position=(100, 100),
            colour=colour.WHITE,
            text="hello world",
            font_name="Roboto-Regular.ttf",
            font_size=50
        )

    def game_loop(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Run custom on_quit code
                    self.on_quit()

                    # Cancel pygame.init
                    pygame.quit()

                    # Stop running the code
                    exit()
            
            # Update game objects
            self.on_update()

            image.blit_all(screen=self.screen)

            pygame.display.update()
            self.clock.tick(60)

    def on_update(self) -> None:
        self.text_image.move((1, 1))

    def on_quit(self) -> None:
        print("Goodbye for now!")

game_manager()
