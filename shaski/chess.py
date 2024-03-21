import pygame
import sys

# Ініціалізація Pygame
pygame.init()

# Константи
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Кольори
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Checker:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
    
    def make_king(self):
        self.king = True
    
    def valid_moves(self, board):
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Можливі напрямки руху для звичайної шашки
        
        if self.king:
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Можливі напрямки руху для короля
        
        for direction in directions:
            next_row = self.row + direction[0]
            next_col = self.col + direction[1]
            
            # Перевірка, чи нові координати знаходяться на дошці
            if 0 <= next_row < ROWS and 0 <= next_col < COLS:
                # Перевірка на пусту клітинку
                if board[next_row][next_col] == 0:
                    moves.append((next_row, next_col))
                # Перевірка на можливість биття
                elif board[next_row][next_col].color != self.color:
                    jump_row = next_row + direction[0]
                    jump_col = next_col + direction[1]
                    if 0 <= jump_row < ROWS and 0 <= jump_col < COLS and board[jump_row][jump_col] == 0:
                        moves.append((jump_row, jump_col))
        
        return moves

# Створення дошки
def create_board():
    board = [[0] * COLS for _ in range(ROWS)]
    for row in range(ROWS):
        for col in range(COLS):
            if (row + col) % 2 == 0:
                if row < 3:
                    board[row][col] = Checker(row, col, RED)  # червона шашка
                elif row > 4:
                    board[row][col] = Checker(row, col, BLUE)  # синя шашка
    return board

# Відображення дошки
def draw_board(screen, board, selected_piece):
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece != 0:
                if piece.color == RED:
                    pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)
                elif piece.color == BLUE:
                    pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 10)
                if piece.king:
                    pygame.draw.circle(screen, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

    if selected_piece is not None:
        if selected_piece.row is not None and selected_piece.col is not None:
            for move in selected_piece.valid_moves(board):
                row, col = move
                pygame.draw.circle(screen, (0, 255, 0), (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10)

# Основна функція гри
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Шашки')
    board = create_board()
    selected_piece = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                row = mouse_y // SQUARE_SIZE
                col = mouse_x // SQUARE_SIZE
                if selected_piece is None:
                    piece = board[row][col]
                    if isinstance(piece, Checker):
                        selected_piece = piece
                else:
                    if (row, col) in selected_piece.valid_moves(board):
                        selected_piece.row, selected_piece.col = row, col
                    selected_piece = None

        screen.fill(WHITE)
        draw_board(screen, board, selected_piece)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()