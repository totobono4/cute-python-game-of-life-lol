from typing import List
from typing import Tuple
import pygame
import time

GAME_OF_LIFE_SIZE = 100
GAME_OF_LIFE_CELL = 4

PYGAME_SCREEN_WIDTH = GAME_OF_LIFE_CELL * GAME_OF_LIFE_SIZE
PYGAME_SCREEN_HEIGHT = GAME_OF_LIFE_CELL * GAME_OF_LIFE_SIZE

pygame.init()
screen = pygame.display.set_mode((PYGAME_SCREEN_WIDTH, PYGAME_SCREEN_HEIGHT))

init = [
    [0,1,0],
    [0,0,1],
    [1,1,1]
]

def insert(coordinates : Tuple[int, int], insert_matrix : List[List], base_matrix : List[List]):
    for ix in range(len(insert_matrix[0])):
        for iy in range(len(insert_matrix)):
            base_matrix[coordinates[0]+iy][coordinates[1]+ix] = insert_matrix[iy][ix]

def get_nb_neighbors(matrix : List[List], coordinates : Tuple[int, int]):
    neighbors = 0
    for x in range(coordinates[0]-1, coordinates[0]+2):
        for y in range(coordinates[1]-1, coordinates[1]+2):
            if not (x == coordinates[0] and y == coordinates[1]):
                neighbors += matrix[y%len(matrix[0])][x%len(matrix)]
    return neighbors

doubleBuffer = [
    [[0 for _ in range(GAME_OF_LIFE_SIZE)] for _ in range(GAME_OF_LIFE_SIZE)],
    [[0 for _ in range(GAME_OF_LIFE_SIZE)] for _ in range(GAME_OF_LIFE_SIZE)]
]
insert((2,2), init, doubleBuffer[0])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for x in range(len(doubleBuffer[0][0])):
        for y in range(len(doubleBuffer[0])):
            pygame.draw.rect(
                screen,
                (0,0,100) if doubleBuffer[0][y][x] == 0 else (0,200,200),
                (x * GAME_OF_LIFE_CELL, y * GAME_OF_LIFE_CELL, GAME_OF_LIFE_CELL, GAME_OF_LIFE_CELL)
            )
            neighbors = get_nb_neighbors(doubleBuffer[0], (x, y))
            doubleBuffer[1][y][x] = doubleBuffer[0][y][x] if neighbors == 2 else 1 if neighbors == 3 else 0

    doubleBuffer[0], doubleBuffer[1] = doubleBuffer[1], doubleBuffer[0]

    pygame.display.flip()
    time.sleep(.01)

pygame.quit()