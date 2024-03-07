import pygame
import random

# Oyun alanı boyutları
WIDTH = 300
HEIGHT = 600
CELL_SIZE = 30

# Renkler
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0), (75, 0, 130), (255, 105, 180)]

# Şekiller
SHAPES = [
    [[1, 1, 1],
     [0, 1, 0]],
    
    [[0, 2, 2],
     [2, 2, 0]],
    
    [[3, 3],
     [3, 3]],
    
    [[4, 4, 4, 4]],
    
    [[0, 0, 5],
     [5, 5, 5]],
    
    [[0, 6, 0],
     [6, 6, 6]],
    
    [[7, 0],
     [7, 0],
     [7, 7]]
]

class Tetris:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0] * (WIDTH // CELL_SIZE) for _ in range(HEIGHT // CELL_SIZE)]
        self.current_piece = None
        self.current_piece_x = 0
        self.current_piece_y = 0
        self.score = 0
        self.game_over = False
        self.generate_piece()
    
    def generate_piece(self):
        shape = random.choice(SHAPES)
        color = random.choice(COLORS)
        self.current_piece = {'shape': shape, 'color': color}
        self.current_piece_x = len(self.grid[0]) // 2 - len(shape[0]) // 2
        self.current_piece_y = 0
    
    def draw_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.current_piece['color'], (self.current_piece_x * CELL_SIZE + x * CELL_SIZE, self.current_piece_y * CELL_SIZE + y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, COLORS[cell - 1], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
                pygame.draw.rect(self.screen, GRAY, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    
    def collide(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    if self.current_piece_y + y >= len(self.grid) or self.current_piece_x + x < 0 or self.current_piece_x + x >= len(self.grid[0]) or self.grid[self.current_piece_y + y][self.current_piece_x + x]:
                        return True
        return False
    
    def freeze_piece(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece_y + y][self.current_piece_x + x] = self.current_piece['color']
        self.clear_lines()
        self.generate_piece()
        if self.collide():
            self.game_over = True
    
    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for line in lines_to_clear:
            del self.grid[line]
            self.grid.insert(0, [0] * (WIDTH // CELL_SIZE))
        self.score += len(lines_to_clear)
    
    def run(self):
        while not self.game_over:
            self.screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_piece_x -= 1
                        if self.collide():
                            self.current_piece_x += 1
                    if event.key == pygame.K_RIGHT:
                        self.current_piece_x += 1
                        if self.collide():
                            self.current_piece_x -= 1
                    if event.key == pygame.K_DOWN:
                        self.current_piece_y += 1
                        if self.collide():
                            self.current_piece_y -= 1
                    if event.key == pygame.K_SPACE:
                        while not self.collide():
                            self.current_piece_y += 1
                        self.current_piece_y -= 1
            if not self.collide():
                self.current_piece_y += 1
            else:
                self.freeze_piece()
            self.draw_grid()
            self.draw_piece()
            pygame.display.flip()
            self.clock.tick(5)
        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()
