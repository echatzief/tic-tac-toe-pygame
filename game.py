import pygame
import sys

from utils import DEFAULT_WINDOW_SIZE
from board import Board

class Game:
    
    def __init__(self):
        self.game_over = False
        self.grid = []
        self.board = None
        self.screen = None
        self.clock = pygame.time.Clock()

    def run(self):
    
        # Initialize the pygame engine
        pygame.init()

        # Setup the size of the screen
        self.screen = pygame.display.set_mode(DEFAULT_WINDOW_SIZE)

        # Set the title of the window
        pygame.display.set_caption("Tic Tac Toe")
        
        # Create the board
        self.create_board()

        self.board.draw_board()
        
        while True:

            # Listen for board events
            self.listen_for_events()

            pygame.display.update()
    
    def listen_for_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1] 

                clicked_row = int(mouseY // self.board.width)
                clicked_col = int(mouseX // self.board.height)
                
                if self.board.is_square_available(clicked_row, clicked_col):

                    # Mark the clicked square with the player's symbol
                    self.board.mark_square(clicked_row, clicked_col)

                    # Check if a player has won
                    if self.board.is_winning():
                        self.game_over = True
                    
                    # Change the turn
                    self.board.change_turn()
        
            # Restart the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.board.restart()
                    self.game_over = False



    def create_board(self):
        self.board = Board(self.screen)
        self.board.create() 
