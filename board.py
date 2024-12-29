import pygame
import random
from utils import Colors, DEFAULT_BOARD_ROWS, DEFAULT_BOARD_COLS, DEFAULT_WINDOW_SIZE

class Board: 

    def __init__(self, screen, rows = DEFAULT_BOARD_ROWS, cols = DEFAULT_BOARD_COLS):
        self.grid = []
        self.rows = rows
        self.cols = cols
        self.height = int(DEFAULT_WINDOW_SIZE[0] / DEFAULT_BOARD_ROWS) - 10
        self.width = int(DEFAULT_WINDOW_SIZE[1] / DEFAULT_BOARD_COLS) - 10
        self.row_margin = int((DEFAULT_WINDOW_SIZE[0] - DEFAULT_BOARD_ROWS * self.height) / (self.rows + 1))
        self.col_margin = int((DEFAULT_WINDOW_SIZE[1] - DEFAULT_BOARD_COLS * self.width) / (self.cols + 1))
        self.screen = screen
        self.turn = random.choice([-1, 1])
    
    def create(self):

        # Set the background of the grid
        self.screen.fill(Colors.DARK_GREEN.value)

        # Initialize the grid with zeros
        for row in range(self.rows):        
            self.grid.append([])
            for col in range(self.cols):
                self.grid[row].append(0)

    def is_square_available(self, row, col):
        return self.grid[row][col] == 0

    def mark_square(self, row, col):
        self.grid[row][col] = self.turn

        self.draw_board()

    def restart(self):
        self.screen.fill(Colors.DARK_GREEN.value)

        self.turn = random.choice([-1, 1])

        for row in range(self.rows):
            for col in range(self.cols):
                self.grid[row][col] = 0
    
        self.draw_board()

    def change_turn(self):
        if self.turn == -1:
            self.turn = 1
        else:
            self.turn = -1
    
    def is_winning(self):
        for col in range(self.cols):
            if all(self.grid[row][col] == self.turn for row in range(self.rows)):
                self.draw_vertical_winning_line(col)
                return True

        for row in range(self.rows):
            if all(self.grid[row][col] == self.turn for col in range(self.cols)):
                self.draw_horizontal_winning_line(row)
                return True

        if all(self.grid[i][i] == self.turn for i in range(min(self.rows, self.cols))):
            self.draw_asc_diagonal()
            return True

        if all(self.grid[self.rows - 1 - i][i] == self.turn for i in range(min(self.rows, self.cols))):
            self.draw_desc_diagonal()
            return True

        return False
    
    def draw_vertical_winning_line(self, col):
        posX = (self.col_margin + self.width) * col + self.col_margin + self.width // 2

        pygame.draw.line(
            self.screen,
            Colors.LIGHT_GREY.value,
            (posX, self.col_margin),
            (posX, self.screen.get_height() - self.col_margin),
            10
        )

    def draw_horizontal_winning_line(self, row):
        posY = (self.row_margin + self.height) * row + self.row_margin + self.height // 2

        pygame.draw.line(
            self.screen,
            Colors.LIGHT_GREY.value,
            (self.row_margin, posY),
            (self.screen.get_width() - self.row_margin, posY),
            10
        )

    def draw_desc_diagonal(self):
        pygame.draw.line(
            self.screen,
            Colors.LIGHT_GREY.value,
            (self.row_margin, self.screen.get_height() - self.row_margin),
            (self.screen.get_width() - self.col_margin, self.col_margin),
            10
        )

    def draw_asc_diagonal(self):
        pygame.draw.line(
            self.screen,
            Colors.LIGHT_GREY.value,
            (self.col_margin, self.row_margin),
            (self.screen.get_width() - self.col_margin, self.screen.get_height() - self.row_margin),
            10
        )
    
    def draw_board(self):
        for row in range(self.rows):
            for column in range(self.cols):

                # Calculate rectagular
                rect_x = (self.col_margin + self.width) * column + self.col_margin
                rect_y = (self.row_margin + self.height) * row + self.row_margin

                # Draw the rectangle
                pygame.draw.rect(
                    self.screen,
                    Colors.GREEN.value,
                    [rect_x, rect_y, self.width, self.height]
                )

                # Draw a circle or "X" if the grid value is 1 or -1
                if self.grid[row][column] == 1:
                    pygame.draw.circle(
                        self.screen,
                        Colors.BEIGE.value,
                        (rect_x + self.width // 2, rect_y + self.height // 2),
                        min(self.width, self.height) // 2,
                        6
                    )
                elif self.grid[row][column] == -1:
                    pygame.draw.line(
                        self.screen,
                        Colors.LIGHT_BLACK.value,
                        (rect_x + 10, rect_y + 10),
                        (rect_x + self.width - 10, rect_y + self.height - 10),
                        10
                    )
                    pygame.draw.line(
                        self.screen,
                        Colors.LIGHT_BLACK.value,
                        (rect_x + self.width - 10, rect_y + 10),
                        (rect_x + 10, rect_y + self.height - 10),
                        10
                    ) 
